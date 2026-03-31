project = "MTDataPro 中文手册"
copyright = "2026, 王培杰"
author = "王培杰"
version = "1.9"
release = "1.9.5"
language = "zh_CN"

exclude_patterns = []

extensions = [
    "myst_parser",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx_copybutton",
    "sphinx_sitemap",
    "sphinxcontrib.mermaid",
    # "sphinx_docxbuilder",  # DISABLED - import error with Sphinx 9.x
]

myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_admonition",
    "html_image",
    "linkify",
    "substitution",
    "tasklist",
]

mermaid_version = "10.6.1"
mermaid_init_js = 'mermaid.initialize({startOnLoad:true,theme:"neutral"});'

templates_path = ["_templates"]

html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "logo_only": False,
    "prev_next_buttons_location": "bottom",
    "style_external_links": False,
    "style_nav_header_background": "#2980B9",
    "collapse_navigation": False,
    "sticky_navigation": True,
    "navigation_depth": 4,
    "includehidden": True,
    "titles_only": False,
    "flyout_display": "hidden",
}

html_static_path = ["_static"]
html_css_files = ["css/custom.css"]
html_js_files = ["mathjax-init.js"]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

myst_heading_anchors = 3
myst_url_schemes = ("http", "https", "mailto")
myst_fence_as_directive = ["mermaid"]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

# Sitemap configuration
html_baseurl = "https://emwpj.github.io/MTDataPro-docs/"
sitemap_url_scheme = "https://emwpj.github.io/MTDataPro-docs/{lang}"

html_title = "MTDataPro 中文手册"
html_short_title = "MTDataPro"
html_last_updated_fmt = "%Y 年 %m 月 %d 日"
html_show_sourcelink = True
html_show_sphinx = True
html_show_copyright = True

html_sidebars = {
    "**": [
        "sidebar/brand.html",
        "sidebar/search.html",
        "sidebar/scroll.html",
        "sidebar/ethical-ads.html",
    ]
}

# MathJax configuration
mathjax3_config = {
    "options": {
        "processHtmlClass": "math",
    },
    "tex2jax": {
        "inlineMath": [["$", "$"], ["\\(", "\\)"]],
        "displayMath": [["$$", "$$"], ["\\[", "\\]"]],
    },
    "startup": {
        "pageReady": "MathJax.startup.promise.then(() => MathJax.typesetPromise())"
    },
}

# LaTeX configuration for PDF output
latex_documents = [
    ("index", "mtdatapro.tex", "MTDataPro 中文手册", "王培杰", "manual"),
]

latex_toplevel_sectioning = "chapter"
latex_show_urls = "inline"
latex_elements = {
    "papersize": "a4",
    "pointsize": "10pt",
    "preamble": """
\\usepackage{xeCJK}
\\setCJKmainfont{FandolSong}
\\setCJKsansfont{FandolHei}
\\setCJKmonofont{FandolFang}
""",
}

# Word document configuration
docx_documents = [
    ("index", "MTDataPro中文手册.docx", "MTDataPro 中文手册", "王培杰", "general"),
]
docx_cover = True
docx_numbering = True
