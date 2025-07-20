import os
import sys
from importlib.metadata import version as get_version


sys.path.insert(0, os.path.abspath(".."))

project = "Ledgerly"
author = "truthless-dev"
copyright = "2025, truthless-dev"
release = get_version(project)

extensions = [
    "autoapi.extension",
    "sphinx_click",
]

autoapi_dirs = ["../ledgerly"]

templates_path = ["_templates"]
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
]


html_theme = "alabaster"
html_static_path = ["_static"]
