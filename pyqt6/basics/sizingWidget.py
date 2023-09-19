import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("sizingWidget")
        button = QPushButton("Press Me!")

        # Size the Window
        self.setFixedSize(QSize(2000, 1000))

        self.setCentralWidget(button)



if __name__=="__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()




