import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QApplication, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 500, 500)

        self.label = QLabel("Hello", self)

        # to create a button, we'll use the push button widget
        self.button1 = QPushButton("Click me", self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Buttons")

        # we then style it
        self.button1.setGeometry(150, 100, 200, 200)
        self.button1.setStyleSheet("font-size: 30px;")

        # to connect the button to the function, we need to list the kind of event expected (click)
        # then we need to connect the button to an action to perform (slot),
        # in this case is the function on_click1 (signal -> slot == event -> action)
        self.button1.clicked.connect(self.on_click1)

        self.label.setGeometry(150, 300, 200, 200)
        self.label.setStyleSheet("font-size: 30px;")

    # for the button to perform any action, we need to set up a signal and slot action (signal.connect(slot))
    def on_click1(self):
        print("button1 clicked")
        # we can change the text of the button
        self.button1.setText("clicked")
        # you can disable a button:
        # self.button1.setDisabled(True)
        #
        # or perform some other action on another element, such as a label
        self.label.setText("Goodbye")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()