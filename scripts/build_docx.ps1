# Build Word document from markdown with Mermaid diagram support
# This script:
# 1. Copies source files to temp directory
# 2. Converts Mermaid diagrams to PNG images
# 3. Converts markdown to Word document using pandoc

$ErrorActionPreference = "Stop"

$SourceDir = "source"
$BuildDir = "_build"
$TempSource = "_build\temp_source"
$OutputFile = "_build\MTDataPro_Manual.docx"

# Clean up previous builds
if (Test-Path "_build") {
    Remove-Item -Recurse -Force "_build"
}
New-Item -ItemType Directory -Path "_build" -Force | Out-Null

# Copy source files to temp directory
Write-Host "Copying source files..."
Copy-Item -Recurse $SourceDir $TempSource

# Preprocess mermaid diagrams
Write-Host "Converting Mermaid diagrams to images..."
python scripts/preprocess_mermaid.py $TempSource

# Copy central images folder to build directory (for pandoc to find)
if (Test-Path "$TempSource\images") {
    Copy-Item -Recurse "$TempSource\images" "$BuildDir\"
}

# Build the document using pandoc
Write-Host "Building Word document..."

# Order: intro files first, then chapters
$mdFiles = @(
    "intro\index.md",
    "intro\install.md",
    "intro\quickstart.md",
    "chapters\chapter1.md",
    "chapters\chapter2.md",
    "chapters\chapter3.md",
    "chapters\chapter4.md",
    "chapters\chapter5.md",
    "chapters\chapter6.md",
    "chapters\chapter7.md",
    "chapters\chapter8.md"
)

# Change to temp source directory so pandoc can find images with relative paths
Push-Location $TempSource
$mdFiles | ForEach-Object { Write-Host "  Adding: $_" }
& pandoc $mdFiles -o "..\..\$OutputFile" --resource-path=. --wrap=none -f markdown-auto_identifiers
Pop-Location

Write-Host "Done! Word document created: $OutputFile"
