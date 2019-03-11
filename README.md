
Cookiecutter-PySide2 is a [Cookiecutter](http://github.com/audreyr/cookiecutter) template that assists users in their creation of GUI applications.

---
## Features

* GUI application template
* Package creation with ready-made setup.py

---
## Installation

Prior to installing the PySide2 cookiecutter, the cookiecutter package must be installed in the user's virtual environment. This is achieved via the following command:

    $ pip install cookiecutter

With cookiecutter installed, the PySide2 cookiecutter template can be installed with:

    $ cookiecutter https://github.com/zapisnicar/cookiecutter-pyside2.git

Once cookiecutter clones the template, the user will be asked a series of questions related to their
project:

    $ full_name [My Name]: Enter your full name.

    $ email [myaddress@mail.com]: Enter your email address.

    $ github_username [githubuser]: Enter your github username.

    $ repo_name [PySide2_demo]: Enter the name of your project's repository.

    $ package_name [pyside2_demo]: Enter the name of your application's package.

    $ application_name [application]: Enter the name of your GUI application.

    $ application_title [Template]: Enter the title of your application. This name is also used
      as an entry point into the application.

    $ project_short_description [A PySide2 GUI application]: Enter a short description about your project.

    $ version [0.0.1]: Enter the version number for your application.


---
## Usage

With the questions during installation answered, the user will have a fully functioning Python project
in their current working directory. This package will contain a GUI application template in the package
directory. All the user needs to finish coding is the rest of their GUI application.

Source files (*.ui and sample icons) for Qt Designer are inside /designer directory. Compile it with
Makefile.

[Included icons are free for comercial use.](https://www.creativefreedom.co.uk/)