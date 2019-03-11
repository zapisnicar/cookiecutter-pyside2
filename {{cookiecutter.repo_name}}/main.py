#!/usr/bin/env python3


import sys
from {{cookiecutter.package_name}} import app


# Back up the reference to the exceptionhook
sys._excepthook = sys.excepthook

def my_exception_hook(exctype, value, traceback):
    # Catch PySide2 exceptions
    # https://stackoverflow.com/questions/43039048/pyqt5-fails-with-cryptic-message

    # Print the error and traceback
    print(exctype, value, traceback)
    # Call the normal Exception hook after
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)

# Set the exception hook to our wrapping function
sys.excepthook = my_exception_hook


if __name__ == '__main__':
    # Catch PySide2 exceptions
    try:
        sys.exit(app.main(sys.argv))
    except:
        print("Exiting")
