import sys
# to use labels, we need the QLabel module:
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
# to set a font, we need the QFont module:
from PyQt5.QtGui import QFont
# using the QtCore, we can align items
from PyQt5.QtCore import Qt
# to work with images, we need to import the QPixmap widget to handle images
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle("Images")

        label = QLabel(self)
        label.setGeometry(0, 0, 250, 250)

        # to access an image, we need to create a QPixmap object, passing the path of the image used
        pixmap = QPixmap("img/ditto.png")
        # to add the image to the label, we use the setPixmap method
        label.setPixmap(pixmap)
        # to size the image according to the label, we use the setScaledContents methods and set it to true
        label.setScaledContents(True)
        label.setStyleSheet(
            "background-color: lightgray;"
            "border-radius: 5px;"
            "border: 2px solid black;"
        )
        # to position the label, we can reuse the setGeometry method
        label.setGeometry(
            # we can subtract the window width and height
            # from that of the label and divide it by two (integer's divisions)
            # to get a center alignment
            (self.width() - label.width()) // 2,
            (self.height() - label.height()) // 2,
            label.width(),
            label.height()
        )


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