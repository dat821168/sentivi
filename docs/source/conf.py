import os
import sys

project = 'Sentivi'
copyright = '2020, Duy V. Huynh'
author = 'Duy V. Huynh'
version = '0.1.0'
release = '0.1.0'
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
pygments_style = 'sphinx'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['static']

sys.path.insert(0, os.path.abspath('../..'))
extensions = ['sphinx.ext.autodoc', 'sphinx_rtd_theme']
