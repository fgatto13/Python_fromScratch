import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow,
    QLabel, QWidget,
    # the following are not widgets, but classes that help us manage the layout
    QVBoxLayout, QHBoxLayout, QGridLayout)

# usually, you can't add a layout manager in a MainWindow object.
# MainWindow widgets have a specific design in layout structure that is incompatible with layout managers
#
# The goal is then to:
# 1. create a generic widget (QWidget)
# 2. add a layout manager to it
# 3. add the generic widget to the main widget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Layouts")
        self.setGeometry(300, 300, 500, 500)
        self.initUI()

    # best practice is to create the following function within the mainWindow class to initialize the user interface
    def initUI(self):
        # let's create a generic widget
        central_widget = QWidget()
        # we then add the central widget to the main widget
        self.setCentralWidget(central_widget)

        label1 = QLabel("1", self)
        label2 = QLabel("2", self)
        label3 = QLabel("3", self)
        label4 = QLabel("4", self)
        label5 = QLabel("5", self)
        label6 = QLabel("6", self)

        label1.setStyleSheet(
            "background-color:red;"
            "border-radius: 5px;")
        label2.setStyleSheet(
            "background-color:green;"
            "border-radius: 5px;")
        label3.setStyleSheet(
            "background-color:blue;"
            "border-radius: 5px;")
        label4.setStyleSheet(
            "background-color:purple;"
            "border-radius: 5px;"
        )
        label5.setStyleSheet(
            "background-color:yellow;"
            "border-radius: 5px;"
        )
        label6.setStyleSheet(
            "background-color:red;"
            "border-radius: 5px;"
        )
        # to manage the labels, let's start with a grid layout manager
        vbox = QGridLayout()
        # we then want to add our labels to the grid layout
        # with grids, after adding an object, we need to specify row and column
        vbox.addWidget(label1, 0, 0)
        vbox.addWidget(label2, 0, 1)
        vbox.addWidget(label3, 0, 2)
        vbox.addWidget(label4, 1, 0)
        vbox.addWidget(label5, 1, 1)
        vbox.addWidget(label6, 1, 2)
        # and then set the layout of the central widget to be the vbox
        central_widget.setLayout(vbox)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
