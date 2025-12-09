import os

from atsphinx.mini18n import get_template_dir as get_mini18n_template_dir
from atsphinx.stlite import __version__ as version

# -- Project information
project = "atsphinx-stlite"
copyright = "2025, Kazuya Takei"
author = "Kazuya Takei"
release = version

# -- General configuration
extensions = [
    # Bundled extensions
    "sphinx.ext.githubpages",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    # atsphinx extensions
    "atsphinx.bulma.layout.hero",
    "atsphinx.mini18n",
    # Third-party extensions
    "sphinx_toolbox.confval",
]
templates_path = ["_templates", get_mini18n_template_dir()]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for i18n
language = "en"
gettext_compact = False
locale_dirs = ["_locales"]

# -- Options for HTML output
html_theme = "bulma-basic"
html_static_path = ["_static"]
html_title = f"{project} v{release}"
html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/fontawesome.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/solid.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/brands.min.css",
]
html_theme_options = {
    "color_mode": "light",
    "bulmaswatch": "pulse",
    "logo_description": "Documentation of atsphinx-stlite.",
    "navbar_icons": [
        {
            "label": "",
            "icon": "fa-brands fa-solid fa-github fa-2x",
            "url": "https://github.com/atsphinx/stlite",
        }
    ],
    "navbar_search": True,
    "navbar_show_hidden_toctree": True,
    "layout": {
        "index": [
            {"type": "space", "size": 1},
            {"type": "main", "size": 10},
            {"type": "space", "size": 1},
        ],
        "**": [
            {"type": "main", "size": 10},
            {"type": "sidebar", "size": 2},
        ],
    },
}
html_sidebars = {
    "**": [
        "sidebar/logo.html",
        "sidebar/line.html",
        "select-lang.html",
        "sidebar/localtoc.html",
        "navigation.html",
    ],
}

# -- Options for extensions
# sphinx.ext.intersphinx
intersphinx_mapping = {
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
}
# sphinx.ext.todo
todo_include_todos = True
# atsphinx.mini18n
mini18n_default_language = "en"
mini18n_support_languages = ["en", "ja"]
mini18n_basepath = "/stlite/" if "CI" in os.environ else "/"
