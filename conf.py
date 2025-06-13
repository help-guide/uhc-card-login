# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# Add any paths that contain custom extensions or modules here.
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Activate Your UHC Card'
copyright = '2025, UnitedHealthcare'
author = 'UnitedHealthcare'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- General configuration ---------------------------------------------------

# Sphinx extensions
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
    'sphinx.ext.githubpages',
]

# Templates path
templates_path = ['_templates']

# Source file suffix and master document
source_suffix = '.rst'
master_doc = 'index'

# Language
language = 'en'

# Patterns to exclude when looking for source files
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# Theme options
html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,
    'display_version': True,
    'style_external_links': True,
    'style_nav_header_background': '#005da6',  # UHC brand-like color
    'show_powered_by': False,
}

# Title shown in the browser tab
html_title = "Activate Your UHC Card at activate.uhc.com – Step-by-Step Guide"
html_short_title = "UHC Card Activation"

# Logo and favicon
# Uncomment and add paths if needed
# html_logo = '_static/logo.png'
html_favicon = 'favicon.ico'

# Static paths
html_static_path = ['_static']

# Hide "View page source" link
html_show_sourcelink = False

# Allow raw HTML in .rst files
rst_prolog = """
.. role:: raw-html(raw)
   :format: html
"""

# -- Options for todo extension ----------------------------------------------

todo_include_todos = True
