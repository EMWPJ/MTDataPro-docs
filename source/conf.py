project = 'MTDataPro 中文手册'
copyright = '2026, MTDataPro 开发团队'
author = 'MTDataPro 开发团队'
version = '1.9'
release = '1.9.4'
language = 'zh_CN'

exclude_patterns = []

extensions = [
    'myst_parser',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx.ext.mathjax',
    'sphinx_copybutton',
    'sphinx_sitemap',
    'sphinx_design',
    'sphinxcontrib.mermaid',
]

# Mermaid 配置
mermaid_version = '10.6.1'
mermaid_init_js = 'mermaid.initialize({startOnLoad:true,theme:"neutral"});'

# MathJax 配置
mathjax3_config = {
    "options": {
        "enableMenu": False,
        "processHtmlClass": "math|tex2jax_process|mathjax_process|output_area",
    },
    "tex2jax": {
        "inlineMath": [["$", "$"], ["\\(", "\\)"]],
        "displayMath": [["$$", "$$"], ["\\[", "\\]"]],
    },
    "startup": {
        "ready": "MathJax.startup.promise.then(() => MathJax.typesetPromise())"
    }
}

templates_path = ['_templates']

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'logo_only': False,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'style_nav_header_background': '#2980B9',
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,
    'flyout_display': 'hidden',
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
    'substitution',
    'tasklist',
    'dollarmath',
]
myst_heading_anchors = 3
myst_url_schemes = ('http', 'https', 'mailto')
myst_fence_as_directive = ['mermaid']

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}

sitemap_url_scheme = 'https://mtdp-china.org/docs/{lang}'

# HTML 输出选项
html_title = 'MTDataPro 中文手册'
html_short_title = 'MTDataPro'
html_last_updated_fmt = '%Y 年 %m 月 %d 日'
html_show_sourcelink = True
html_show_sphinx = True
html_show_copyright = True

# 侧边栏配置
html_sidebars = {
    '**': [
        'sidebar/brand.html',
        'sidebar/search.html',
        'sidebar/scroll.html',
        'sidebar/ethical-ads.html',
    ]
}
