import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #Let's define a bunch of elements:
        self.button1 = QPushButton('#1')
        self.button2 = QPushButton('#2')
        self.button3 = QPushButton('#3')

        self.initUI()

    def initUI(self):
        self.setWindowTitle("CSS Styling")

        # let's create the central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # now the layout
        layout = QHBoxLayout()

        # and let's add them
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)

        # now link the layout to the central widget
        central_widget.setLayout(layout)

        # we first set the object names
        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        # now for the CSS styling:
        self.setStyleSheet("""
            QPushButton {
                font-size: 40px;
                padding: 15px 75px;
                margin: 10px;
                border: 1px solid black;
                border-radius: 5px;
            }
            QPushButton#button1 {
                background-color: #ff4747;
            }
            QPushButton#button2 {
                background-color: hsl(122, 100%, 64%);
            }
            QPushButton#button3 {
                background-color: hsl(204, 100%, 64%);
            }
            QPushButton#button1:hover {
                background-color: hsl(0, 100%, 84%);
            }
            QPushButton#button2:hover {
                background-color: hsl(122, 100%, 84%);
            }
            QPushButton#button3:hover {
                background-color: hsl(204, 100%, 84%);
            }
        """)



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()