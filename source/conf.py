# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
# from pygments.lexers import get_lexer_by_name
from sphinx.highlighting import lexers
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from makrell_lexer import MakrellLexer

lexers['makrell'] = MakrellLexer()

project = 'Makrell'
copyright = '2025, Hans-Christian Holm'
author = 'Hans-Christian Holm'
release = '0.9'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = 'furo'
html_static_path = ['_static']

