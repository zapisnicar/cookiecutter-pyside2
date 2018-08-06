
Cookiecutter-PySide2 is a Cookiecutter_ template that assists users in their creation of GUI applications.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter

Features
--------

* GUI application template
* Package creation with ready-made setup.py

Installation
------------

Prior to installing the PySide2 cookiecutter, the cookiecutter package must be installed in the user's virtual environment. This is achieved via the following command::

    $ pip install cookiecutter

With cookiecutter installed, the PySide2 cookiecutter template can be installed with::

    $ cookiecutter https://github.com/zapisnicar/cookiecutter-pyside2.git

Once cookiecutter clones the template, the user will be asked a series of questions related to their
project::

    $ full_name [Pesnik Zapisnicar]: Enter your full name.

    $ email [zapisnicar@mail.xyz]: Enter your email address.

    $ github_username [zapisnicar]: Enter your github username.

    $ repo_name [cookiecutter-pyside2]: Enter the name of your project's repository.

    $ package_name [cookiecutter-pyside2]: Enter the name of your application's package.

    $ application_name [application]: Enter the name of your GUI application.

    $ application_title [Template]: Enter the title of your application. This name is also used
      as an entry point into the application.

    $ project_short_description [A PySide2 GUI application]: Enter a short description about your project.

    $ version [0.0.1]: Enter the version number for your application.

    $ (not implemented) insert_toolbar [yes]: If you would like a tool bar on your application, press enter or type yes.

    $ (not implemented) insert_statusbar [yes]: If you would like a movable status bar on your application, press enter or type yes.



Usage
-------

With the questions during installation answered, the user will have a fully functioning Python project
in their current working directory. This package will contain a GUI application template in the package
directory. All the user needs to finish coding is the rest of their GUI application.
