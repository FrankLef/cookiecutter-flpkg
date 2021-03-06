"""Sphinx configuration."""
from datetime import datetime


project = "flpkg Cookiecutter"
author = "François Lefebvre"
copyright = f"{datetime.now().year}, {author}"
extensions = ["sphinx.ext.intersphinx"]
intersphinx_mapping = {
    "mypy": ("https://mypy.readthedocs.io/en/stable/", None)}
language = "en"
html_static_path = ["_static"]
html_theme = "alabaster"
html_theme_options = {
    "github_banner": "true",
    "github_button": "true",
    "github_count": "true",
    "github_user": "FrankLef",
    "github_repo": "cookiecutter-fkpkg",
    "github_type": "star",
    "logo": "logo.jpg",
    "logo_name": "true",
    "fixed_sidebar": "true",
    "sidebar_width": "250px",
}
linkcheck_ignore = [
    "codeofconduct.html",
    "https://github.com/PyCQA/flake8-bugbear#",
    "https://github.com/peterjc/flake8-rst-docstrings#",
    "https://github.com/pre-commit/pre-commit-hooks#",
    "https://github.com/pycqa/pep8-naming#",
    "https://github.com/terrencepreilly/darglint#",
    "https://github.com/PyCQA/mccabe#",
]
