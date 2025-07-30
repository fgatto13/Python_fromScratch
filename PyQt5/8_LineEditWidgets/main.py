import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QGridLayout, QLineEdit  # (text box)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 500, 200)
        self.lineEdit = QLineEdit(self)
        self.submitButton = QPushButton("Push", self)
        self.initUI()

    def initUI(self):
        # let's style the text box
        self.setWindowTitle("Text boxes")
        self.lineEdit.setGeometry(10, 10, 200, 80)
        self.lineEdit.setPlaceholderText("Input some text")
        self.lineEdit.setStyleSheet("QLineEdit { "
                                    "background-color: #fff; "
                                    "border: 1px solid #ddd; "
                                    "border-radius: 5px; }")
        self.submitButton.setGeometry(210, 10, 200, 80)
        self.submitButton.clicked.connect(self.submit)

    def submit(self):
        # we can retrieve the text inserted from the user and do something with it
        text = self.lineEdit.text()
        print(text)
        self.lineEdit.clear()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()