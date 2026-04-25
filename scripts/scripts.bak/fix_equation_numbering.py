#!/usr/bin/env python3
"""
Post-process Sphinx-generated LaTeX to enable equation numbering.

MyST separated format produces:
  \\begin{equation*}
    \\begin{split}...\\end{split}
  \\end{equation*}
  \\sphinxAtStartPar
  \\sphinxstyleemphasis{(2.1)}

This script:
  1. Converts \\begin{equation*} to \\begin{equation}
  2. Inserts \\hfill\\tag{N.M} before \\end{equation}
  3. Removes the \\sphinxAtStartPar + \\sphinxstyleemphasis{(N.M)} lines

Usage: python scripts/fix_equation_numbering.py [path/to/mtdatapro.tex]
"""

import sys
from pathlib import Path

BS = chr(92)  # single backslash


def process_latex(content):
    """
    Pattern to find:
      \\begin{equation*}
        \\begin{split}...\\end{split}
      \\end{equation*}
      \\sphinxAtStartPar\n
      \\sphinxstyleemphasis{(N.M)}

    Transform to:
      \\begin{equation}\\begin{split}
      ...math content...
      \\end{split}\\hfill\\tag{N.M}\\end{equation}

    And remove the \\sphinxAtStartPar + \\sphinxstyleemphasis{(N.M)} lines.
    """

    output = []
    i = 0
    equations_processed = 0

    while i < len(content):
        # Look for \begin{equation*}
        eq_start_marker = BS + "begin{equation*}"
        eq_start = content.find(eq_start_marker, i)
        if eq_start == -1:
            output.append(content[i:])
            break

        # Append everything before this equation*
        output.append(content[i:eq_start])

        # Find the matching \end{equation*}
        end_marker = BS + "end{equation*}"
        eq_end = content.find(end_marker, eq_start)
        if eq_end == -1:
            output.append(content[eq_start:])
            break

        # Find end of the line containing \end{equation}
        line_end = content.find("\n", eq_end)
        if line_end == -1:
            line_end = len(content)

        # After \end{equation*} we expect:
        # \sphinxAtStartPar\n
        # \sphinxstyleemphasis{(N.M)}
        follow_start = line_end + 1 if line_end + 1 < len(content) else len(content)

        # Find \sphinxAtStartPar
        at_marker = BS + "sphinxAtStartPar"
        style_marker = BS + "sphinxstyleemphasis{(2."
        close_paren = ")}"

        at_pos = content.find(at_marker, follow_start)
        style_pos = content.find(style_marker, follow_start)

        eq_num = None
        if at_pos != -1 and style_pos != -1 and style_pos < at_pos + 60:
            # Verify there's a newline between \sphinxAtStartPar and \sphinxstyleemphasis
            between = content[at_pos + len(at_marker) : style_pos]
            if "\n" in between or content[at_pos + len(at_marker)] == "\n":
                # Extract equation number from \sphinxstyleemphasis{(N.M)}
                num_start = style_pos + len(style_marker)
                num_end = content.find(close_paren, num_start)
                if num_end != -1:
                    eq_num = content[num_start:num_end]

        # Extract the full equation block (from \begin to \end, inclusive)
        full_eq_end = eq_end + len(end_marker)
        eq_block = content[eq_start:full_eq_end]

        if eq_num:
            # Build new numbered equation
            # Replace \begin{equation*} with \begin{equation}
            inner = eq_block[len(eq_start_marker) : -len(end_marker)]
            # Insert \hfill\tag{N.M} before \end{equation}
            new_eq = (
                BS
                + "begin{equation}"
                + inner
                + BS
                + "hfill"
                + BS
                + "tag{"
                + eq_num
                + "}"
                + BS
                + "end{equation}"
            )
            output.append(new_eq)
            equations_processed += 1

            # Skip past the \sphinxAtStartPar\n\sphinxstyleemphasis{(N.M)}\n lines
            if style_pos != -1:
                # Find end of the \sphinxstyleemphasis{...} line
                para_line_end = content.find("\n", style_pos)
                if para_line_end == -1:
                    para_line_end = len(content)
                # Skip to end of that line
                skip_to = para_line_end + 1
                # Skip any blank lines that follow
                while skip_to < len(content) and content[skip_to] == "\n":
                    skip_to += 1
                i = skip_to
            else:
                i = full_eq_end
        else:
            # No number found, keep equation* as-is
            output.append(eq_block)
            i = full_eq_end

    return "".join(output), equations_processed


def main():
    if len(sys.argv) > 1:
        tex_path = Path(sys.argv[1])
    else:
        # Default to _buildlatex/mtdatapro.tex
        script_dir = Path(__file__).parent
        tex_path = script_dir.parent / "_buildlatex" / "mtdatapro.tex"

    if not tex_path.exists():
        print(f"Error: {tex_path} not found")
        sys.exit(1)

    print(f"Processing: {tex_path}")

    content = tex_path.read_text(encoding="utf-8")

    new_content, count = process_latex(content)

    # Count remaining equation*
    remaining_eq_star = new_content.count(BS + "begin{equation*}")
    remaining_styleemphasis = new_content.count(BS + "sphinxstyleemphasis{(2.")

    print(f"Processed {count} equations")
    print(f"Remaining equation*: {remaining_eq_star}")
    print(f"Remaining sphinxstyleemphasis for eq numbers: {remaining_styleemphasis}")

    # Write output
    tex_path.write_text(new_content, encoding="utf-8")
    print(f"Written: {tex_path}")


if __name__ == "__main__":
    main()
