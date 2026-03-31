#!/usr/bin/env python3
"""
Pre-process markdown files to convert Mermaid diagrams to PNG images.
This enables Mermaid diagrams to display in Word documents.
"""

import re
import os
import subprocess
import hashlib
from pathlib import Path


def find_mermaid_blocks(content):
    """Find all Mermaid code blocks in markdown content."""
    # Match ```mermaid blocks
    pattern = r"```mermaid\s*\n(.*?)```"
    matches = list(re.finditer(pattern, content, re.DOTALL))
    return matches


def generate_image_name(mermaid_code):
    """Generate a unique filename based on mermaid code hash."""
    hash_val = hashlib.md5(mermaid_code.encode()).hexdigest()[:8]
    return f"mermaid_{hash_val}.png"


def convert_mermaid_to_png(mermaid_code, output_dir, image_name):
    """Convert Mermaid code to PNG using mmdc."""
    import platform

    input_file = os.path.join(output_dir, f"{image_name}.mmd")
    output_file = os.path.join(output_dir, image_name)

    # Write mermaid code to file
    with open(input_file, "w", encoding="utf-8") as f:
        f.write(mermaid_code.strip())

    # Run mmdc to convert to PNG
    try:
        # On Windows, mmdc.cmd is the actual command
        if platform.system() == "Windows":
            cmd = [
                "mmdc.cmd",
                "-i",
                input_file,
                "-o",
                output_file,
                "-s",
                "2",
                "-b",
                "white",
                "-w",
                "1200",
            ]
        else:
            cmd = [
                "mmdc",
                "-i",
                input_file,
                "-o",
                output_file,
                "-s",
                "2",
                "-b",
                "white",
                "-w",
                "1200",
            ]
        subprocess.run(cmd, check=True, capture_output=True, shell=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error converting mermaid: {e}")
        return False
    finally:
        # Clean up .mmd file
        if os.path.exists(input_file):
            os.remove(input_file)


def process_markdown_file(filepath, output_dir, central_img_dir, img_subdir="images"):
    """Process a single markdown file, converting Mermaid blocks to images."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Find all mermaid blocks
    blocks = find_mermaid_blocks(content)
    if not blocks:
        return []

    # Create image directory in central location
    os.makedirs(central_img_dir, exist_ok=True)

    converted = []
    # Process blocks in reverse order to maintain correct positions
    for match in reversed(blocks):
        mermaid_code = match.group(1).strip()
        image_name = generate_image_name(mermaid_code)

        # Convert to PNG
        if convert_mermaid_to_png(mermaid_code, central_img_dir, image_name):
            converted.append(image_name)
            # Replace mermaid block with image
            # Use relative path from source root
            image_rel_path = os.path.join(img_subdir, image_name).replace(os.sep, "/")
            image_markdown = f"![Mermaid diagram]({image_rel_path})"
            content = content[: match.start()] + image_markdown + content[match.end() :]
            print(f"  Converted: {image_name}")
        else:
            print(f"  Failed: {image_name}")

    # Write updated content
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    return converted


def main():
    import sys

    if len(sys.argv) < 2:
        print("Usage: python preprocessor.py <source_dir>")
        sys.exit(1)

    source_dir = sys.argv[1]
    md_files = list(Path(source_dir).rglob("*.md"))

    # Central images directory (relative to source_dir)
    central_img_dir = os.path.join(source_dir, "images")

    print(f"Found {len(md_files)} markdown files")
    print(f"Images will be stored in: {central_img_dir}")

    total_converted = 0
    for md_file in md_files:
        print(f"Processing: {md_file}")
        converted = process_markdown_file(
            str(md_file), os.path.dirname(str(md_file)), central_img_dir
        )
        total_converted += len(converted)

    print(f"Done! Converted {total_converted} Mermaid diagrams to images.")


if __name__ == "__main__":
    main()
