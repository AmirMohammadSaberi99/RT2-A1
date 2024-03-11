import os
import subprocess
import sys

sys.path.insert(0, os.path.abspath('../'))
project = 'Assignment1-RT2'
copyright = '2024, Assignment1-S5840276'
author = 'Assignment1-S5840276'
release = '1.0'

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.doctest', 'sphinx.ext.intersphinx', 'sphinx.ext.todo', 'sphinx.ext.coverage', 'sphinx.ext.mathjax', 'sphinx.ext.ifconfig', 'sphinx.ext.viewcode', 'sphinx.ext.githubpages', "sphinx.ext.napoleon", 'sphinx.ext.inheritance_diagram', 'breathe']

templates_path = ['_templates']
exclude_patterns = []

source_suffix = '.rst'
master_doc = 'index'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

intersphinx_mapping = {
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
