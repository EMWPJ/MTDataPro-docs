#!/bin/bash
# Build Word document from markdown with Mermaid diagram support
# This script:
# 1. Copies source files to temp directory
# 2. Converts Mermaid diagrams to PNG images
# 3. Converts markdown to Word document using pandoc

set -e

SOURCE_DIR="source"
BUILD_DIR="_build"
TEMP_SOURCE="_build/temp_source"
OUTPUT_FILE="_build/MTDataPro中文手册.docx"

# Clean up previous builds
rm -rf "$TEMP_SOURCE"
rm -rf "$BUILD_DIR/images"
rm -f "$OUTPUT_FILE"

# Create build directory
mkdir -p "$BUILD_DIR"

# Copy source files to temp directory
echo "Copying source files..."
cp -r "$SOURCE_DIR" "$TEMP_SOURCE"

# Preprocess mermaid diagrams
echo "Converting Mermaid diagrams to images..."
python scripts/preprocess_mermaid.py "$TEMP_SOURCE"

# Collect all markdown files in order
echo "Building Word document..."

# Build the document using pandoc
# Order: intro files first, then chapters
pandoc \
    "$TEMP_SOURCE/intro/index.md" \
    "$TEMP_SOURCE/intro/install.md" \
    "$TEMP_SOURCE/intro/quickstart.md" \
    "$TEMP_SOURCE/chapters/chapter1.md" \
    "$TEMP_SOURCE/chapters/chapter2.md" \
    "$TEMP_SOURCE/chapters/chapter3.md" \
    "$TEMP_SOURCE/chapters/chapter4.md" \
    "$TEMP_SOURCE/chapters/chapter5.md" \
    "$TEMP_SOURCE/chapters/chapter6.md" \
    "$TEMP_SOURCE/chapters/chapter7.md" \
    "$TEMP_SOURCE/chapters/chapter8.md" \
    "$TEMP_SOURCE/chapters/chapter9.md" \
    -o "$OUTPUT_FILE" \
    --reference-doc=_build/reference.docx \
    --extract-media="_build/media" \
    --wrap=none \
    -f markdown-auto_identifiers

# Copy images to build media folder
cp -r "$TEMP_SOURCE/images" "$BUILD_DIR/"

echo "Done! Word document created: $OUTPUT_FILE"
