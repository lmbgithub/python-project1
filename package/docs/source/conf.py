# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Camera Simulator'
copyright = '2022, Luis Manuel Barrios'
author = 'Luis Manuel Barrios'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
#    'sphinx.ext.autosummary',
]



templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
napoleon_google_docstring = True

import os
import sys
import unittest.mock as mock

sys.path.insert(0, os.path.abspath('../../'))
sys.path.insert(0, os.path.abspath('../../camera_simulator'))
sys.setrecursionlimit(1500)

MOCKED_MODULES = [
        'numpy', 
        'numpy.lib',
        'numpy.lib.stride_tricks',
        'numpy.lib.recfunctions',
        'numpy.linalg',
        'numpy.testing',
        'numpy.__version__',
        ]

for mod_name in MOCKED_MODULES:
    sys.modules[mod_name] = mock.Mock()