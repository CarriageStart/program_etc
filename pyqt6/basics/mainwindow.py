import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

# Subclass QMainWindow to customize your application's main Window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # QtWidget should always call super.__init__

        # Configure how MainWindow looks
        self.setWindowTitle("My App")

        # Create widget and set under another widget
        button = QPushButton("Press Me!")
        # Set the central widget of the Window (Assignment + central feature)
        self.setCentralWidget(button)

if __name__=="__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()


