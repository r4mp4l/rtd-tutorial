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
html_theme = 'sphinx_wagtail_theme'
# html_theme = 'sphinx_rtd_theme'
# html_theme = 'sphinx_material'
html_logo = 'assets/img/logo.png'

# html_theme_options = {
#    'logo_only': True,
#    'display_version': True,
#    'prev_next_buttons_location': 'bottom',
#}


html_theme_options = dict(
    project_name = "Dietrichs Documentation",
    logo = "assets/img/logo.png",
    logo_alt = "Dietrichs",
    logo_height = 59,
    logo_url = "/",
    logo_width = 45,
)
# extensions = ["myst_parser"]
extensions.append("sphinx_wagtail_theme")


# -- Options for EPUB output
epub_show_urls = 'footnote'
