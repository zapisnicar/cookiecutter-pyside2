#!/usr/bin/env python3


import sys
from pathlib import Path
from PySide2.QtWidgets import QMainWindow, QApplication, QMessageBox
from PySide2.QtCore import QCoreApplication, Signal, QThread
from PySide2.QtGui import QClipboard

# from PySide2 import uic
# MAIN_DIR = Path(__file__).resolve().parent
# Ui_MainWindow, QtBaseClass = uic.loadUiType(MAIN_DIR/'designer'/'mainwindow.ui')
from {{cookiecutter.package_name}}.gui.mainwindow import Ui_MainWindow


class ApplicationWindow(QMainWindow):
    """Main Window"""
    def __init__(self, parent=None):
        super(ApplicationWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Create widgets
        self.clipboard = QApplication.clipboard()

        # Connect signals and slots
        self.ui.actionSave.triggered.connect(self.save_content)
        self.ui.actionQuit.triggered.connect(self.quit_app)
        self.ui.actionCopy.triggered.connect(self.clipboard_copy)
        self.ui.actionAbout.triggered.connect(self.about)

        self.ui.okButton.clicked.connect(self.quit_app)
        self.ui.cancelButton.clicked.connect(self.quit_app)

        # Configure widgets
        self.ui.textBrowser.setOpenExternalLinks(True)

        # Start thread
        self.worker = Worker()
        self.worker.send_text.connect(self.receive_text)
        self.worker.start()

    def quit_app(self):
        """Close application"""
        # answer = QMessageBox.question(self, 'Quit program', 'Are you sure?',
        #                               QMessageBox.Yes | QMessageBox.No)
        # if answer == QMessageBox.Yes:
        #     self.close()
        self.close()

    def save_content(self):
        """Save content of textBrowser to file"""
        # TODO Save to file
        print('Save')

    def clipboard_copy(self):
        """Copy text box content to the clipboard"""
        text = self.ui.textBrowser.toPlainText()
        self.clipboard.setText(text,  QClipboard.Clipboard)

    def receive_text(self, some_string):
        """Add some_string at the end of textBrowser"""
        self.ui.textBrowser.append(some_string)

    def about(self):
        """Help/About message box"""
        QMessageBox.about(self, '{{cookiecutter.application_name}}', '{{cookiecutter.email}}')


class Worker(QThread):
    """
    Worker thread
    Runs work method, and create signals:

    finished
        No data
    error
        `tuple` (exctype, value, traceback.format_exc() )
    result
        `object` data returned from processing, anything
    progress
        `int` indicating % progress
    send_text
        'str' send text to textBrowser
    """
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)
    send_text = Signal(str)

    def __init__(self, parent=None):
        super(Worker, self).__init__(parent)

    def run(self):
        """Start work method and take care about run-time errors in thread"""
        result = self.work()
        self.result.emit(result)

    def work(self):
        """Emit program arguments as 'send_text' signal"""
        arguments = QCoreApplication.arguments()
        if len(arguments) > 1:
            for arg in arguments[1:]:
                self.send_text.emit(arg)


def main(args=sys.argv):
    app = QApplication(args)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
