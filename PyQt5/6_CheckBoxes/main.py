import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
# to work with different states, we need the Qt module
from PyQt5.QtCore import Qt # QtCore contains non GUI classes relative to PyQt5 apps
from inquirer3 import checkbox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 500, 400)
        # to create a checkbox, we can insert the label of the checkbox
        self.checkbox = QCheckBox("Do you like food?", self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("CheckBoxes")
        self.checkbox.setStyleSheet("font-size: 30px;")
        self.checkbox.setGeometry(10, 0, 400, 100)

        # to default to a position:
        self.checkbox.setChecked(False)
        # to connect a slot to a signal:
        self.checkbox.stateChanged.connect(self.checkbox_changed)

    # we need to pass the state when working with checkboxes, and it can be:
    # - 0 for unchecked
    # - 2 for checked
    # - 1 for partially checked
    def checkbox_changed(self, state):
        print(state)
        # there is a constant to check that makes the code mor readable:
        if state == Qt.Checked:
            print("Checked")
        else:
            print("UnChecked")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()