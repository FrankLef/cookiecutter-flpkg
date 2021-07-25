# Cookiecutter with best practices

A cookiecutter using the most up-to-date (I think) best practices as of 2021.  It is entirely inspired
by the Hypermodern cookiecutter [Hypermodern][Hypermodern] which has the most complete and wonderful documention
on the best practices.

## Resources

As mentioned above this cookiecutter is a subset, a scaled-down version of [Hypermodern python cookiecutter][Hypermodern].
That is, **there should no feature that is not already in [Hypermodern python cookiecutter][Hypermodern]**. As a result you
should always look first to [Hypermodern python cookiecutter][Hypermodern] for explanation.

The author of the Hypermodern cookiecutter, Claudio Jolowicz, has written a series of articles full of additional
sound advices [Hypermodern guide][HypermodernGuide] on how to build a python project.  I strongly recommend reading it.
It is particularly useful about the testing.

## Documentation with 

## Features

See the article by [Jonas Kemper][Jonas Kemper] with concurs with my own days spent on the net trying to figure
out how to set up a python project. The [Hyper modern cookicutter][Hypermodern] has all these features and much more.

The most important best practices are the use of [poetry] for package and dependency management
and [nox] to automate the different tasks.

|Package|Description|Reference|
|-------|-----------|---------|
|Poetry|Packaging and dependency management|[poetry]|
|Nox|Automation|[nox]|
|nox-poetry|drop-in replacement for the `nox.session` operator|[nox-poetry]|
|flake8|Linting|[flake8]|
|black|Code formatting|[black]|
|pre-commit|Git hook scripts|[pre-commit]|
|GitHub Actions|Continuous Integration|[GitHub Actions][githubActions]|
|pytest|Testing suite|[pytest]|
|coverage|Code coverage|[coverage]|
|mypy|Static type-checking|[mypy]|
|typeguard|Runtime type-checking|[typeguard]|
|click|Command-line interface|[click]|
|sphinx|Documentation in rst format|[sphinx]|
|pygments|Automatic code highliting|[pygments]|
|autodoc|Documentation from docstrings in rst style|[autodoc]|
|napoleon|Documentation from docstrings in NumPy or Google style|[napoleon]|
|sphinx-click|Documentation for command-line interface|[sphinx-click]|
|darglint|Check docstring matches the actual function/method|[darglint]|
|xdoctest|Check documentation examples|[xdoctest]|
|safety|Safety check installed dependencies for known vulnerabilities|[safety]|
|bandit|Find common security issues in Python code|[bandit]|

## Quickstart

### Step 0: Requirements (only once)

Install the requirements first.  Normally they **only need be installed once** in your
default `python` environment.  From time to time, you should update them.

#### `pipx`, `cookiecutter` and `pipenv`

If `pipx`, `cookiecutter` and `pipenv` have not already been installed, do it as follows

```shell
python3 -m pip install --user pipx
python3 -m pipx ensurepath
pipx install cookiecutter
pipx install pipenv
```

#### `Poetry`

Install `poetry` by following the instructions from the official website [poetry install][poetryInstall].
Many web sites give outdated instructions on how to install `poetry`, especially regarding the use
of the file `get-poetry.py` which was replaced by `install-poetry.py`. Use the official way at [poetry install][poetryInstall].

#### `Nox` and `nox-poetry`

Install [nox] and [nox-poetry]. When using `pipx` it is important to use `inject`
to ensure that `nox-poetry` is in the same environment that `nox` is in. See details in
[nox-poetry].  Some `nox session` (e.g. coverage) don't seem to work if you don't use the
`inject` command.

```shell
pipx install nox
# make sure to use inject with pipx
pipx inject nox nox-poetry
```

### Step 1: Create from cookiecutter

Create the project using the `cookiecutter`.
Read [cookiecutter] docs for the different ways to create a project.

```shell
pipx run cookiecutter https://github.com/FrankLef/cookiecutter-plainpkg.git
```

> `pipx` will ask you if you want to reinstall `cookiecutter`, say **no**. It will then
ask if you want to reuse `cookiecutter` say **yes**.

You will then be asked for these inputs

|Variable|Description|Example|
|--------|-----------|-------|
|project_name|Name on Github and PyPI|plain-pkg|
|package_name|Import name of the package|plain_pkg|
|friendly_name|Friendly name|A plain Package|
|author|Primary author|François Lefebvre|
|email|email of author|flefebvre01@hotmail.com|
|github_user|GitHub username of author|FrankLef|
|version|Initial package version|0.1.0|
|license|Opensource license|MIT license|

### Step 2: Create virtual environment

Create a virtual environment using `pipenv`. See [pipenv guide][pyenv] for details.
Make sure you are in the project directory.

```shell
# Change to project directory
cd <project_name>
pipenv shell
```

### Step 3: Install packages

Install the required packages using `pipx` in the virtual environment. See [pipx github][pipx]
for details.

The package `mkdocs` is used as an example here.

```shell
# Change to project directory
cd <project_name>
# install the mkdocs package, this is only an example
pipx install mkdocs
```

which should give you this message if all went fine.

```shell
install completed successfully
```

### Step 4: Initialize Github

Create a repo in github and get its url which we call `<repo_url>` from now on.  The repo

* must be empty, i.e. no `README`, `.gitignore` and `LICENCE` file
* should be created at least 1 minute1 before running the next step,
  it seems sometimes to cause problem otherwise.
* if problem, verify gitub status at [status](https://www.githubstatus.com)

Then add the origin with `<repo_url>` with this command on the terminal.

```shell
git remote add origin <repo_url>
```

and run the `Makefile` as follow to push to github

```shell
make push
```

> If you get an interruption cause by a change to a file by `black`, rerun the `make push`
command.  The interruption was caused by black reformatting some files (usually `setup.py`),
running `make push` a second time normally works since `black` has no more reformatting
to do after the first pass.

and you should see this message which confirms that you are finished.

```shell
push completed successfully
```

To start coding in your new project, open the shell with `pipenv`, if an environment
doesn't already exist, `pipenv` will create it.

```shell
pipenv shell
```

## Directory structure

```console
├── {{cookiecutter.project_name}}
    ├── .gitignore                <- GitHub's excellent Python .gitignore customized for this project
    ├── LICENSE                   <- License.
    ├── Makefile                  <- Makefile with init and push rules
    ├── Pipfile                   <- The Pipfile for reproducing the analysis environment
    ├── README.md                 <- The top-level README for developers using this project.
    ├── setup.cfg                 <- Configurations for flake8, isort, mypy, pytest, etc.
    ├── setup.py                  <- Setup file used to build and install the this package.
    │
    ├── {{cookiecutter.repo_name}}
    │   ├── __init__.py
    │   ├── __main__.py
    │   └── {{cookiecutter.repo_name}}.py
    │
    └── tests                     <- Directory of tests for pytest
        ├── __init__.py
        └── test_{{cookiecutter.repo_name}}.py
```

## Credits

* [Hypermodern][Hypermodern]: This cookiecutter is largely inspired by the wonderful Hypermodern cookiecutter.
* [Cookiecutter][cookiecutter]: The tool that saves me so much time.
* Carmine Paolino's [Modern Data Science][ModernDataScience]: A template centered around
the pipeline architecture using `prefect` which is, in my experience, the way of data science projects.

[poetry]: https://python-poetry.org
[poetryInstall]: https://python-poetry.org/docs
[nox]: https://nox.thea.codes/en/stable
[nox-poetry]: https://nox-poetry.readthedocs.io/en/latest
[flake8]: http://flake8.pycqa.org/en/latest
[black]: https://github.com/psf/black
[pre-commit]: https://pre-commit.com
[githubActions]: https://github.com/features/actions
[pytest]: https://docs.pytest.org/en/latest
[coverage]: https://coverage.readthedocs.io/en/coverage-5.5
[mypy]: http://mypy-lang.org
[typeguard]: https://github.com/agronholm/typeguard
[click]: https://click.palletsprojects.com/en/8.0.x
[sphinx]: https://www.sphinx-doc.org/en/master
[pygments]: https://pygments.org
[autodoc]: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
[napoleon]: https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
[sphinx-click]: https://sphinx-click.readthedocs.io/en/latest
[darglint]: https://github.com/terrencepreilly/darglint
[xdoctest]: https://github.com/Erotemic/xdoctest
[bandit]: https://github.com/PyCQA/bandit
[safety]: https://github.com/pyupio/safety
[Jonas Kemper]: https://dev.to/jonasrk/understanding-best-practice-python-tooling-by-comparing-popular-project-templates-2dnj
[cookiecutter]: https://cookiecutter.readthedocs.io/en/latest
[pyenv]: https://realpython.com/pipenv-guide
[pipx]: https://github.com/pypa/pipx
[PyPackage]: https://github.com/audreyfeldroy/cookiecutter-pypackage
[AudreyFamily]: https://github.com/audreyfeldroy/cookiecutter-pypackage/network/members
[Hypermodern]: https://cookiecutter-hypermodern-python.readthedocs.io/en/2020.6.15/guide.html
[HypermodernGuide]: https://cjolowicz.github.io/posts/hypermodern-python-01-setup
[MkDos]: https://www.mkdocs.org

[ModernDataScience]: https://github.com/crmne/cookiecutter-modern-datascience
[SourceryBestBractice]: https://github.com/sourcery-ai/python-best-practices-cookiecutter
