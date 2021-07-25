===============================
cookiecutter-flpkg
===============================

.. badges-begin

| |Status| |CalVer| |License|
| |Read the Docs|
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
.. |Read the Docs| image:: https://img.shields.io/readthedocs/cookiecutter-flpkg/latest.svg?label=Read%20the%20Docs
   :target: https://cookiecutter-flpkg.readthedocs.io/
   :alt: Read the documentation at https://cookiecutter-flpkg.readthedocs.io/
.. |pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit
.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Black

.. badges-end



Cookiecutter_ template with the best practices in creating
a Python package. Heavily inspired by the
`Hypermodern cookiecutter`_HypermodernCookie.


✨📚✨ `Read the full documentation`__

__ https://cookiecutter-flpkg.readthedocs.io/


Usage
=====

.. code:: console

   cookiecutter gh:FrankLef/cookiecutter-flpkg

Resources and credits
=====================

Cookiecutter_ template for a Python package based on the
`Hypermodern cookiecutter`_HypermodernCookie. 
The features are a strict subset, a scaled down version 
of Hypermodern cookiecutter.

That is, there is no feature that are not already included
in the Hypermodern cookiecutter and, therefore the wonderful
`Hypermodern documentation`_HypermodernDocs can and should be used.

There is also a very instructive and useful article on how to practically
create a package available `here`_HypermodernArticle. I strongly
recommend it if it is your first time creating a Python package.

Features
========

.. features-begin

The template supports Python 3.6, 3.7, 3.8, and 3.9.

- Packaging and dependency management with Poetry_
- Test automation with Nox_
- Linting with pre-commit_ and Flake8_
- Continuous integration with `GitHub Actions`_
- Documentation with Sphinx_ and `Read the Docs`_
- Automated uploads to PyPI_ and TestPyPI_
- Automated release notes with `Release Drafter`_
- Automated dependency updates with Dependabot_
- Code formatting with Black_ and Prettier_
- Testing with pytest_
- Code coverage with Coverage.py_
- Coverage reporting with Codecov_
- Command-line interface with Click_
- Static type-checking with mypy_
- Runtime type-checking with Typeguard_
- Security audit with Bandit_ and Safety_
- Check documentation examples with xdoctest_
- Generate API documentation with autodoc_ and napoleon_
- Generate command-line reference with sphinx-click_
- Manage project labels with `GitHub Labeler`_

.. features-end

.. references-begin

.. _Bandit: https://github.com/PyCQA/bandit
.. _Black: https://github.com/psf/black
.. _Click: https://click.palletsprojects.com/
.. _Codecov: https://codecov.io/
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _Coverage.py: https://coverage.readthedocs.io/
.. _Dependabot: https://dependabot.com/
.. _Flake8: http://flake8.pycqa.org
.. _GitHub Actions: https://github.com/features/actions
.. _HypermodernArticle: https://medium.com/@cjolowicz/hypermodern-python-d44485d9d769
.. _HypermodernCookie: https://github.com/cjolowicz/cookiecutter-hypermodern-python
.. _HypermodernDocs: https://cookiecutter-hypermodern-python.readthedocs.io/en/latest
.. _Nox: https://nox.thea.codes/
.. _Poetry: https://python-poetry.org/
.. _Prettier: https://prettier.io/
.. _PyPI: https://pypi.org/
.. _Read the Docs: https://readthedocs.org/
.. _Release Drafter: https://github.com/release-drafter/release-drafter
.. _Safety: https://github.com/pyupio/safety
.. _Sphinx: http://www.sphinx-doc.org/
.. _TestPyPI: https://test.pypi.org/
.. _Typeguard: https://github.com/agronholm/typeguard
.. _autodoc: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
.. _mypy: http://mypy-lang.org/
.. _napoleon: https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
.. _pre-commit: https://pre-commit.com/
.. _pytest: https://docs.pytest.org/en/latest/
.. _sphinx-click: https://sphinx-click.readthedocs.io/
.. _xdoctest: https://github.com/Erotemic/xdoctest
.. _GitHub Labeler: https://github.com/marketplace/actions/github-labeler

.. references-end
