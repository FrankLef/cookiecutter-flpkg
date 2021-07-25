Quickstart
==================

Follow the steps in the order mentioned to create a package with
the `flpkg cookiecutter`.

Step 0: Requirements
---------------------

Install the requirements first.  Normally they **only need be installed once** in your
default `python` environment.

Verify if `pipx`, `pipenv` and `cookiecutter` are installed

.. code:: shell

   pipx --version
   pipenv --version
   cookiecutter --version

You should received a message on the console that looks like This

.. code:: console

   # for pipx
   0.16.2.1
   # for pipenv
   pipenv, version 2020.11.15
   # for cookiecutter
   Cookiecutter 1.7.3 C:\ ...

If `pipx`, `cookiecutter` and `pipenv` are not already installed,
install them as follows

.. code:: shell

   python3 -m pip install --user pipx
   python3 -m pipx ensurepath
   pipx install pipenv
   pipx install cookiecutter

Step 1: Create the project
---------------------------

Create the project using the `cookiecutter`.
Read _Cookiecutter docs for the different ways to create a project.
Here is a common way to do it, from github.

.. include:: ../README.rst
   :start-after: usage-begin
   :end-before: usage-end

Now, make sure you work in a virtual environment with _Poetry, 
Nox_ and `nox-poetry`_. See the next step on that.



..
   This is the list of external links

.. include:: ../README.rst
   :start-after: references-begin
   :end-before: references-end


Step 2: Create a virtual environment
-------------------------------------

Create a virtual environment using pipenv_.
Make sure you are in the project directory.

.. code:: shell

   # Change to project directory
   cd <project_name>
   pipenv shell

Step 3: Initialize Github
--------------------------

Create a repo in github and get its url which we call `<repo_url>` from now on.  The repo

* must be empty, i.e. no `README`, `.gitignore` and `LICENCE` file
* should be created at least 1 minute before running the next step,
  sometimes an error is returned if we go too fast.
* if problem, verify gitub status at `status <https://www.githubstatus.com>`_

Then add the origin with `<repo_url>` with this command on the terminal.

.. code:: shell
   
   git remote add origin <repo_url>

and push to github as follow *FrankLef* in `user.name="FrankLef"` is an example
and so is *https://github.com/FrankLef/cookiecutter-flpkg.git* in
`user.email=` and *Initial commit* in `commit -m`.

.. code:: shell

   git branch -M main
   git add -A
   git -c user.name="FrankLef" -c user.email="<repo_url>" commit -m "Initial commit"
   git push -u origin main

To start coding in your new project, open the shell with `pipenv`, if an environment
doesn't already exist, `pipenv` will create it.

.. code:: shell

   pipenv shell

