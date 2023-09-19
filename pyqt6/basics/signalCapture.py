import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Set EventListenter")

        button = QPushButton("Press Me!")
        button.setCheckable(True)                           # 
        button.clicked.connect(self.methodInClicked) #

        self.setCentralWidget(button)


    def methodInClicked(self):
        print("Clicked!")
    

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()




