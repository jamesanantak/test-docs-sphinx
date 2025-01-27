# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

import os
from dataclasses import asdict

from sphinx.application import Sphinx
from sphinx.util.docfields import Field

import sphinxawesome_theme
from sphinxawesome_theme.postprocess import Icons

sys.path.insert(0, os.path.abspath('.'))

project = 'Docs Testing'
copyright = '2025, James Bambridge'
author = 'James Bambridge'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinxawesome_theme",
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'recommonmark',
    'sphinx_markdown_tables',
    "sphinx.ext.intersphinx",
    "sphinx.ext.extlinks",
    "sphinx_design",
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'sphinx_rtd_theme'
html_theme = 'sphinxawesome_theme'

html_title = project
html_use_index = False
html_domain_indices = False  # Don't need module indices
html_copy_source = False  # Don't need sources
#html_permalinks_icon = '<span>¶</span>'
html_permalinks_icon = Icons.permalinks_icon


html_static_path = ['_static']


# Add theme-specific options
html_theme_options = {
    "logo_light": "_static/ana-logo-black.png",
    "logo_dark": "_static/ana-logo-black.png",
}

