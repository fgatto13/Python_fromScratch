import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 500, 350)
        # let's create 3 radio buttons:
        self.radio1 = QRadioButton("Visa", self)
        self.radio2 = QRadioButton("MasterCard", self)
        self.radio3 = QRadioButton("PostePay", self)
        self.radio4 = QRadioButton("In-Store", self)
        self.radio5 = QRadioButton("Online", self)
        # By default, all radio buttons are part of the same group
        # so let's create two button groups:
        self.paymentGroup = QButtonGroup(self)
        self.methodGroup = QButtonGroup(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Radio Buttons")
        self.radio1.setGeometry(0, 0, 300, 50)
        self.radio2.setGeometry(0, 50, 300, 50)
        self.radio3.setGeometry(0, 100, 300, 50)
        self.radio4.setGeometry(0, 150, 300, 50)
        self.radio5.setGeometry(0, 200, 300, 50)

        # we can style a group of elements, just like in CSS:
        self.setStyleSheet("QRadioButton{"
                        "font-size: 40px;"
                        "font-family: Arial;"
                        "padding: 10px;"
                        "}")

        # we can now define which button belongs to what group
        self.paymentGroup.addButton(self.radio1)
        self.paymentGroup.addButton(self.radio2)
        self.paymentGroup.addButton(self.radio3)
        self.methodGroup.addButton(self.radio4)
        self.methodGroup.addButton(self.radio5)

        # to handle the behavior of a radio button, we use the signal -> slot method:
        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)

    def radio_button_changed(self):
        # to check which element sent the signal, we use the sender method
        radio_button = self.sender()
        # we can see if the radio button is checked (selected)
        if radio_button.isChecked():
            print(f"{radio_button.text()} is checked")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()