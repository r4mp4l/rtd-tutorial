# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Dietrichs'
copyright = '2024, Dietrichs'
author = 'Gaurav Rampal'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']


# -- Options for HTML output
html_theme = 'piccolo_theme'
# By default the project value is used in the nav bar.
project = 'Deitrichs Documentation'
html_logo = 'https://www.dietrichs.com/fileadmin/_processed_/c/d/csm_dietrichs_5499b34bc7.png'
pygments_style = "gruvbox-light"


html_theme_options = {
    # Note how we can include links:
    # "banner_text": 'This is a temporary banner, <a href="https://mynewsletter.com/">please subscribe</a>!',
    "globaltoc_collapse": False
}

# extensions = ["myst_parser"]
extensions.append("sphinx_wagtail_theme")


# -- Options for EPUB output
epub_show_urls = 'footnote'

html_last_updated_fmt = "%b %d, %Y"

# These folders are copied to the documentation's HTML output.
html_static_path = ["_static"]

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...).
html_css_files = ["custom.css"]