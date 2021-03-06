cookiecutter-flpkg
===============================

.. badges-begin

| |Status| |CalVer| |License|
| |pre-commit| |Black|

.. |Status| image:: https://badgen.net/badge/status/alpha/d8624d
   :target: https://badgen.net/badge/status/alpha/d8624d
   :alt: Project Status
.. |CalVer| image:: https://img.shields.io/badge/calver-YYYY.MM.DD-22bfda.svg
   :target: http://calver.org/
   :alt: CalVer
.. |License| image:: https://img.shields.io/github/license/FrankLef/cookiecutter-flpkg
   :target: https://opensource.org/licenses/MIT
   :alt: License
.. |pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit
.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Black

.. badges-end

.. caption-begin

Cookiecutter_ template with the best practices in creating
a Python package. It is a scaled down version of
`Hypermodern cookiecutter`_.

.. caption-end

✨📚✨ Read the `full documentation`_ to avoid error. Particularly the **Quickstart**.

__ https://cookiecutter-flpkg.readthedocs.io/


Usage
-----

.. usage-begin

Change to the parent location where you want the project to be created.
For example if your project is called `project-pkg` in the `parent` folder,
then move to `parent` first

.. code:: shell

   cd ../parent

then create the package. A folder called `project-pkg` will be created in `..\\parent`.

.. code:: shell

   pipx run cookiecutter https://github.com/FrankLef/cookiecutter-flpkg.git


`pipx` will ask you if you want to reinstall `cookiecutter`, say **no**. It will then
ask if you want to reuse `cookiecutter` say **yes**.

You will then be asked for these inputs

.. csv-table::
   :header: "Variable", "Description", "Example"
   :widths: 10, 40, 10

   "project_name", "Name on Github and PyPI", "plain-pkg"
   "package_name", "Import name of the package", "plain_pkg"
   "friendly_name", "Friendly name", "A plain Package"
   "author", "Primary author", "François Lefebvre"
   "email", "email of author", "flefebvre01@hotmail.com"
   "github_user", "GitHub username of author", "FrankLef"
   "version", "Initial package version", "0.1.0"
   "license", "Open source license", "MIT license"

and that is it.  The project is created.

.. usage-end


Resources and credits
---------------------

Cookiecutter_ template for a Python package based on the
`Hypermodern cookiecutter`_. 
The features are a strict subset, a scaled down version 
of Hypermodern cookiecutter.

That is, there is no feature that are not already included
in the Hypermodern cookiecutter and, therefore the wonderful
`Hypermodern docs`_ can and should be used.

There is also a very instructive and useful article on how to practically
create a package available here `Hypermodern article`_. I strongly
recommend it if it is your first time creating a Python package.

A survey of best practices can be found at `Jonas Kemper`_ which
confirms the choice of features of the Hypermodern cookiecutter.

Modifications
^^^^^^^^^^^^^^

In spite of what was just mentioned, the following marginal modifications were made.
They are entirely optional and don't really change what was mentioned previously.

Sphinx-copybutton
   Sphinx-copybutton with ``pip install sphinx-copybutton``. The ``conf.py`` and
   ``requirements.txt`` files were modified accordingly.


Features
---------

.. features-begin

The template supports Python 3.6, 3.7, 3.8 and 3.9.

.. csv-table::
   :header: "Package", "Description", "Link"
   :widths: 10, 40, 10

   "Poetry", "Packaging and dependency management", Poetry_
   "Nox", "Task automation", Nox_
   "nox-poetry", "Drop-in replacement for the `nox.session` operator", `nox-poetry`_
   "flake8","Linting", flake8_
   "black","Code formatting", black_
   "pre-commit", "Git hook scripts", `pre-commit`_
   "GitHub actions", "Continuous integration", `github actions`_
   "pytest", "Testing suite", pytest_
   "coverage", "Code coverage", coverage_
   "mypy", "Static type-checking", mypy_
   "typeguard", "Runtime type-checking", typeguard_
   "click", "Command-line interface", click_
   "sphinx", "Documentation in rst format", sphinx_
   "pygments", "Automatic code highliting", pygments_
   "autodoc", "Documentation from docstrings in rst style", autodoc_
   "napoleon", "Documentation from docstrings in NumPy or Google style", napoleon_
   "sphinx-click", "Documentation for command-line interface", `sphinx-click`_
   "darglint", "Check docstring matches the actual function/method", darglint_
   "xdoctest", "Check documentation examples", xdoctest_
   "safety", "Safety check installed dependencies for known vulnerabilities", safety_
   "bandit", "Find common security issues in Python code", bandit_

.. features-end

.. references-begin

.. _Cookiecutter: https://cookiecutter.readthedocs.io/en/latest
.. _Hypermodern article: https://medium.com/@cjolowicz/hypermodern-python-d44485d9d769
.. _Hypermodern cookiecutter: https://github.com/cjolowicz/cookiecutter-hypermodern-python
.. _Hypermodern docs: https://cookiecutter-hypermodern-python.readthedocs.io/en/latest
.. _Jonas Kemper: https://dev.to/jonasrk/understanding-best-practice-python-tooling-by-comparing-popular-project-templates-2dnj
.. _pipenv: https://realpython.com/pipenv-guide
.. _pipx: https://github.com/pypa/pipx
.. _full documentation: https://cookiecutter-flpkg.readthedocs.io

.. _Poetry: https://python-poetry.org
.. _Poetry install: https://python-poetry.org/docs
.. _Nox: https://nox.thea.codes/en/stable
.. _nox-poetry: https://nox-poetry.readthedocs.io/en/latest
.. _flake8: http://flake8.pycqa.org/en/latest
.. _black: https://github.com/psf/black
.. _prettier: https://prettier.io/
.. _pre-commit: https://pre-commit.com
.. _github actions: https://github.com/features/actions
.. _pytest: https://docs.pytest.org/en/latest
.. _coverage: https://coverage.readthedocs.io/en/coverage-5.5
.. _mypy: http://mypy-lang.org
.. _typeguard: https://github.com/agronholm/typeguard
.. _click: https://click.palletsprojects.com/en/8.0.x
.. _sphinx: https://www.sphinx-doc.org/en/master
.. _pygments: https://pygments.org
.. _autodoc: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
.. _napoleon: https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
.. _sphinx-click: https://sphinx-click.readthedocs.io/en/latest
.. _darglint: https://github.com/terrencepreilly/darglint
.. _xdoctest: https://github.com/Erotemic/xdoctest
.. _bandit: https://github.com/PyCQA/bandit
.. _safety: https://github.com/pyupio/safety

.. references-end
