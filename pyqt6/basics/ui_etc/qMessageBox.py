
import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow,
    QVBoxLayout, QHBoxLayout,
    QWidget,QPushButton, QDialog, QDialogButtonBox, QLabel, QMessageBox
)
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt, QSize



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        layout = QHBoxLayout()

        button = QPushButton("Press me for a Question!")
        button.clicked.connect(self.button_clicked)
        layout.addWidget(button)

        button = QPushButton("Press me for a Warning!")
        button.clicked.connect(self.button1_clicked)
        layout.addWidget(button)

        button = QPushButton("Press me for a Critical!")
        button.clicked.connect(self.button2_clicked)
        layout.addWidget(button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


    def button_clicked(self, s):
        print("Clicked : ", s)

        dig = QMessageBox(self)
        dig.setWindowTitle("I have a question!")
        dig.setText("This is a simple dialog")
        dig.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        dig.setIcon(QMessageBox.Icon.Question)
        button = dig.exec()

        if button == QMessageBox.StandardButton.Yes:
            print("Yew!")
        else:
            print("No!")


    def button1_clicked(self, s):
        button = QMessageBox.warning(
            self,
            "Hey, Dude!",
            "Something seems wrong!",
            buttons=QMessageBox.StandardButton.Discard 
                | QMessageBox.StandardButton.NoToAll 
                | QMessageBox.StandardButton.Ignore,
            defaultButton=QMessageBox.StandardButton.Discard,
        )
        if button == QMessageBox.StandardButton.Discard:
            print("My warning is discarded!")
        elif button == QMessageBox.StandardButton.NoToAll:
            print("No to All warnings!")
        else:
            print("Ignore!")

    def button2_clicked(self, s):
        button = QMessageBox.critical(
            self,
            "Oh, Dear!",
            "Something is very wrong!",
            buttons=QMessageBox.StandardButton.Discard 
                | QMessageBox.StandardButton.NoToAll 
                | QMessageBox.StandardButton.Ignore,
            defaultButton=QMessageBox.StandardButton.Discard,
        )
        if button == QMessageBox.StandardButton.Discard:
            print("My Criticals is discarded!")
        elif button == QMessageBox.StandardButton.NoToAll:
            print("No to All warnings!")
        else:
            print("Ignore!")


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()



if __name__=="__main__":
    main()



