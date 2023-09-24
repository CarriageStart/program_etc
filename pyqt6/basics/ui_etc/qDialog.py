
import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow,
    QVBoxLayout,
    QWidget,QPushButton, QDialog, QDialogButtonBox, QLabel, QMessageBox
)
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt, QSize



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)


    def button_clicked(self, s):
        print("Clicked : ", s)

        dig = CustomDialog(self)
        if dig.exec():          # When
            print("Success!")
        else:
            print("Cancel!")



class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Hello!")

        qBtn = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel | QDialogButtonBox.StandardButton.Apply | QDialogButtonBox.StandardButton.Reset
        self.buttonBox = QDialogButtonBox(qBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("Somthing happened, is that OK?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)



def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()



if __name__=="__main__":
    main()



