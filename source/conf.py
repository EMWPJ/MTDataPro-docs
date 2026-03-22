project = 'MTDataPro'
copyright = '2026, EMWPJ'
author = 'EMWPJ'
release = '1.0'
language = 'zh_CN'

extensions = [
    'myst_parser',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.coverage',
    'sphinx_copybutton',
    'sphinx_sitemap',
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'style_nav_header_gradient': '#2980B9',
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,
}

html_static_path = ['_static']
html_css_files = ['css/custom.css']

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

myst_enable_extensions = [
    'amsmath',
    'colon_fence',
    'deflist',
    'html_admonition',
    'html_image',
    'linkify',
    ' substitution',
    'tasklist',
]
myst_heading_anchors = 3

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}

sitemap_urls = ['https://mtdp.example.com/docs/']
