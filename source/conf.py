from datetime import datetime, timezone

# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------
project = 'ONIX Docs'
copyright = '2010-{}, Open Ephys & Contributors'.format(datetime.now(timezone.utc).year)
author = 'Open Ephys & Contributors'
language = 'en'

# The short X.Y version
#version = '1.0'
## The full version, including alpha/beta/rc tags
#release = '1.0.0-beta'

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.githubpages',
    'sphinx.ext.graphviz',
    'sphinxcontrib.wavedrom',
    'sphinx_design'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# If you add .md, you will need the myst_parser package
source_suffix = ['.rst'] 

# The master toctree document.
main_doc = 'index'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None

# -- Extension configuration -------------------------------------------------

# todo configuration
todo_include_todos = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'pydata_sphinx_theme'
html_logo = '_static/onix_open_ephys_logo.svg'
html_scaled_image_link = True
html_title = project

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named 'default.css' will overwrite the builtin 'default.css'.
html_static_path = ['_static']

html_sidebars = {
    'index': ['search-field.html'],
    "**": [ "sidebar-nav-bs.html"]
}

# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        main_doc,
        'ONIX Documentation',
        'ONIX Documentation',
        author,
        'ONIX Documentation',
        'Next-generation electrophysiology data acquisition',
        'Miscellaneous',
    ),
]

# -- Extension configuration -------------------------------------------------
# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    'use_edit_page_button': True,
    "navigation_with_keys": True,
    "navbar_end": ["navbar-icon-links"],
    "navbar_align": "content",
    "footer_start": ["copyright"],
    "external_links": [{"name": "Open Ephys", "url": "https://open-ephys.org"},],
    'icon_links': [
        dict(name='GitHub',
             url='https://github.com/open-ephys/onix-docs',
             icon='fab fa-github'),
        dict(name='Twitter',
             url='https://twitter.com/openephys',
             icon='fab fa-twitter'),
        dict(name='Discord',
             url='https://discord.gg/WXAx2URNQU',
             icon='fab fa-discord')
    ]
    #'announcement': 'These docs are a work in progress.',
}

html_favicon = '_static/favicon.png'

html_context = {
    'github_user': 'open-ephys',
    'github_repo': 'onix-docs',
    'github_version': 'main',
    'doc_path': 'source',
    'default_mode': 'light',
}

html_css_files = [
    'theme_overrides.css',
]

# Option for linkcheck
linkcheck_anchors = False
linkcheck_timeout = 4

# NB: Ignore these sites, they throw 403 errors during linkcheck, but are accessible for end-users
linkcheck_ignore = [
    'https://multimedia.3m.com/mws/media/*', 
    'https://www.intel.com/*',
    'https://www.analog.com/*',
    'https://www.xilinx.com/*',
    'https://white-matter.com/*'
]

# NB: Allow this permanent redirect for a Visual Studio package
linkcheck_allowed_redirects = {
    'https://aka.ms/vs/16/release/vc_redist.x64.exe': 'https://download.visualstudio.microsoft.com/download/pr/9613cb5b-2786-49cd-8d90-73abd90aa50a/CEE28F29F904524B7F645BCEC3DFDFE38F8269B001144CD909F5D9232890D33B/VC_redist.x64.exe'
}

def rstjinja(app, docname, source):
    '''
    Render pages as a jinja template. 
    '''
    # Make sure we're outputting HTML
    if app.builder.format != 'html':
        return
    src = source[0]
    rendered = app.builder.templates.render_string(
        src, app.config.html_context
    )
    source[0] = rendered

def setup(app):
    app.connect('source-read', rstjinja)
    app.add_js_file('copyURLToClipboard.js')

panels_add_bootstrap_css = False
