import sys
# to use labels, we need the QLabel module:
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
# to set a font, we need the QFont module:
from PyQt5.QtGui import QFont
# using the QtCore, we can align items
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle("Hello World")
        # to create a label widget to display text or images,
        # we want a label object, passing the element and the window(self)
        label = QLabel("Hello", self)
        # Get the system default font and increase its size
        default_font = QFont()
        default_font.setPointSize(40)  # Set to desired size

        label.setFont(default_font)
        # to set the geometry of the label, there is the setGeometry function
        label.setGeometry(140, 30, 200, 200)
        # we can also style our label with CSS-like properties:
        label.setStyleSheet("QLabel { "
                            "color: white; "
                            "background-color: lightgray; "
                            "border-radius: 5px; "
                            "padding: 5px; "
                            "text-align: center; "
                            "}")
        # to play with the alignment:
        label.setAlignment(Qt.AlignCenter)

def main():
    app = QApplication(sys.argv)

    # Optional: set the same font size globally for all widgets
    default_font = QFont()
    default_font.setPointSize(12)
    app.setFont(default_font)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()