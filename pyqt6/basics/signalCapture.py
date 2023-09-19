import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Set EventListenter")

        button = QPushButton("Press Me!")
        button.setCheckable(True)               # Let the button widget store Check state
            # Implicit(built-in) event handling of button : Change the color and toggle state
        button.clicked.connect(self.methodInClicked) # Slot for "Click event" is hoolked.

        self.setCentralWidget(button)


    def methodInClicked(self):
        print("Clicked!")
    
def main() -> None :
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()

if __name__ == "__main__" :
    main()




