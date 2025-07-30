# install the PyQt5 module
# then, we first import the sys module to use
# system-specific parameters and functions
import sys
# then, we can import the widget module and a bunch of essentials
from PyQt5.QtWidgets import QApplication, QMainWindow
# to add an icon, we want to access the following:
from PyQt5.QtGui import QIcon
from functions import start_sound

# then, we need to create some boilerplate code:
# 1. create a main window class that inherits from QMainWindow
class MainWindow(QMainWindow):
    def __init__(self, title):
        super().__init__()
        # we can set the title of the window
        self.setWindowTitle(title)
        # set the initial geometry of the window (x, y, width, height)
        # it is all in pixels
        self.setGeometry(300, 300, 400, 300)
        # we can also set an icon, using a file in the project folder
        self.setWindowIcon(QIcon('icons/icon.png'))
    def showEvent(self, event):
        super().showEvent(event)
        start_sound()