from mainWindow import *

def main():
    # we need to create a new application, passing system argv (main args)
    app = QApplication(sys.argv)
    # then, we create a window
    window = MainWindow("First GUI")
    # to show a window, we'll access the show() method
    window.show()
    # after we're done, we want to call the sys.exit function to provide a clean exit from the program
    sys.exit(app.exec_()) # the exec_() function executes the app, waits for user inputs and handles events

if __name__ == '__main__':
    main()