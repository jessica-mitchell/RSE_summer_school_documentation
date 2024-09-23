# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import sys
# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


# Tell Sphinx where your extenstions can be found
sys.path.append(os.path.abspath("./_ext"))

project = "RSE Documentation Workshop"
copyright = "2024, jessica-mitchell"
author = "Jessica Mitchell"
release = "1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# add your extensions to the list
extensions = ["helloworld", # custom extension
              "templating_example", # custom extension
              "sphinx_gallery.gen_gallery",
              "sphinx.ext.mathjax",
              "sphinx.ext.autodoc",
              ]

templates_path = ["_templates"]
# exclude_patterns = []

sphinx_gallery_conf = {
    # path to your examples scripts
    "examples_dirs": "../examples",
    # path where to save gallery generated examples
    "gallery_dirs": "auto_examples",
    "plot_gallery": True
}


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_material"
html_static_path = ["_static"]
html_theme_options = {
    "color_primary": "blue",
    "color_accent": "cyan",
    # Visible levels of the global TOC; -1 means unlimited
    "globaltoc_depth": 1,
    # If False, expand all TOC entries
    "globaltoc_collapse": True,
    # If True, show hidden TOC entries
    "globaltoc_includehidden": True,
    }
html_sidebars = {"**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]}
