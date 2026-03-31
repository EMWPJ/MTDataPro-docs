#!/usr/bin/env python3
"""
Post-process Sphinx-generated LaTeX to enable equation numbering.

NEW APPROACH (MyST separated format):
- MyST now produces: equation* + separate \sphinxstyleemphasis{(N.M)} paragraph
- This script:
  1. Converts \begin{equation*} to \begin{equation} (numbered)
  2. Inserts \hfill\tag{N.M} before \end{equation}
  3. Removes the separate \sphinxstyleemphasis{(N.M)} paragraph
  4. Handles \label{...}\begin{equation*} on the same line

Usage: python scripts/fix_equation_numbering.py [path/to/mtdatapro.tex]
"""

import sys
from pathlib import Path

BS = chr(92)  # single backslash

# LaTeX markers
SPHX_START = BS + "sphinxAtStartPar"
SPHX_STYLE = BS + "sphinxstyleemphasis"
EQ_BEGIN_STAR = BS + "begin{equation*}"
EQ_END_STAR = BS + "end{equation*}"
SPLIT_BEGIN = BS + "begin{split}"
SPLIT_END = BS + "end{split}"
LABEL_CMD = BS + "label"


def find_matching_brace(text: str, start: int) -> int:
    """Find the matching closing brace for an opening brace at `start`.
    Handles nested braces properly.
    Returns position of matching '}', or -1 if not found.
    """
    if start >= len(text) or text[start] != "{":
        return -1
    depth = 0
    i = start
    while i < len(text):
        c = text[i]
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return i
        i += 1
    return -1


def process_latex_file(tex_path: Path) -> int:
    """Process LaTeX for numbered equations."""
    content = tex_path.read_text(encoding="utf-8")
    original = content
    changes = 0

    search_start = 0
    while True:
        eq_start = content.find(EQ_BEGIN_STAR, search_start)
        if eq_start == -1:
            break

        eq_end_pos = content.find(EQ_END_STAR, eq_start)
        if eq_end_pos == -1:
            break

        # Find sphinxAtStartPar after \end{equation*}
        sphinx_start = content.find(SPHX_START, eq_end_pos)
        if sphinx_start == -1:
            break

        # Find \sphinxstyleemphasis{(N.M)} after sphinxAtStartPar
        sphinx_style_start = content.find(SPHX_STYLE + "{(", sphinx_start)
        if sphinx_style_start == -1 or sphinx_style_start > sphinx_start + 50:
            search_start = eq_end_pos + 1
            continue

        # Extract the equation number
        num_start = sphinx_style_start + len(SPHX_STYLE + "{(")
        num_end = content.find(")}", num_start)
        if num_end == -1:
            search_start = eq_end_pos + 1
            continue

        number = content[num_start:num_end]

        # Sanity check - sphinxstyleemphasis should be within reasonable distance
        if sphinx_style_start - eq_end_pos > 200:
            search_start = eq_end_pos + 1
            continue

        # Find split content
        split_start = content.find(SPLIT_BEGIN, eq_start)
        split_end = content.find(SPLIT_END, eq_start)

        if split_start == -1 or split_end == -1 or split_start > eq_end_pos:
            search_start = eq_end_pos + 1
            continue

        split_content = content[split_start : split_end + len(SPLIT_END)]

        # Check for \label{...} on the same line before \begin{equation*}
        line_start = content.rfind("\n", 0, eq_start) + 1
        line_before_eq = content[line_start:eq_start]

        label_text = ""
        label_pos = line_before_eq.find(LABEL_CMD + "{")
        if label_pos >= 0:
            label_end = find_matching_brace(line_before_eq, label_pos)
            if label_end >= 0:
                label_text = line_before_eq[label_pos : label_end + 1]

        tag = BS + "hfill" + BS + "tag{" + number + "}"

        # Build new equation block
        if label_text:
            new_eq = (
                label_text
                + BS
                + "begin{equation}"
                + split_content
                + tag
                + BS
                + "end{equation}"
            )
        else:
            new_eq = BS + "begin{equation}" + split_content + tag + BS + "end{equation}"

        # Find the block to replace: from eq_start (or line_start for labeled)
        # to end of sphinxstyleemphasis paragraph
        style_end = content.find(")}", sphinx_style_start)
        if style_end == -1:
            search_start = eq_end_pos + 1
            continue

        # Include )\n\n after )
        replace_end = style_end + 2
        while replace_end < len(content) and content[replace_end] == "\n":
            replace_end += 1

        # Find the sphinxAtStartPar before sphinxstyleemphasis
        at_start_search = content.rfind(SPHX_START, eq_end_pos, sphinx_start)
        if at_start_search >= eq_end_pos and (sphinx_start - at_start_search) < 30:
            replace_start = at_start_search
        else:
            replace_start = eq_start

        # For labeled equations, include the entire line from \label
        if label_text:
            replace_start = line_start

        old_block = content[replace_start:replace_end]
        content = content.replace(old_block, new_eq, 1)
        changes += 1
        search_start = replace_start + len(new_eq)

    print(f"Changed {changes} equations")

    # Remove any remaining separate sphinxstyleemphasis paragraphs
    remaining = content.count(SPHX_STYLE + "{(")
    print(f"Remaining separate sphinxstyleemphasis: {remaining}")

    if remaining > 0:
        idx = 0
        removed = 0
        while True:
            idx = content.find(SPHX_START, idx)
            if idx == -1:
                break
            style_pos = content.find(SPHX_STYLE + "{(", idx)
            if style_pos == -1 or style_pos > idx + 50:
                idx += 1
                continue

            # Check this is a separate sphinxstyleemphasis (not part of equation)
            eq_end_search = content.rfind(EQ_END_STAR, idx - 200, idx)
            if eq_end_search == -1:
                idx += 1
                continue

            # Remove the paragraph
            style_end = content.find(")}", style_pos)
            if style_end == -1:
                idx += 1
                continue

            para_start = content.rfind("\n\n", idx - 50, idx)
            if para_start == -1:
                para_start = idx - 10

            remove_end = style_end + 2
            while remove_end < len(content) and content[remove_end] == "\n":
                remove_end += 1

            content = content[:para_start] + content[remove_end:]
            removed += 1
            idx = para_start

        print(f"Removed {removed} separate paragraphs")

    tex_path.write_text(content, encoding="utf-8")
    print(f"Saved: {tex_path}")
    return changes


def main():
    tex_path = Path("_buildlatex/mtdatapro.tex")
    if len(sys.argv) > 1:
        tex_path = Path(sys.argv[1])

    if not tex_path.exists():
        print(f"ERROR: LaTeX file not found: {tex_path}")
        sys.exit(1)

    print(f"Processing: {tex_path.absolute()}")
    count = process_latex_file(tex_path)
    print(f"\nDone. {count} equations processed.")
    print("Run 'xelatex mtdatapro.tex' twice to rebuild the PDF.")


if __name__ == "__main__":
    main()
