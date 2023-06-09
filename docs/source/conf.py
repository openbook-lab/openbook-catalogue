# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'OpenBook'
copyright = '2023, OpenBook Lab'
author = 'OpenBook Lab'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_title='OpenBook Project'
html_baseurl=''
html_theme = 'furo'
html_static_path = ['_static']
html_logo = "https://avatars.githubusercontent.com/u/127606413"

html_css_files = [ 'css/custom.css' ]
