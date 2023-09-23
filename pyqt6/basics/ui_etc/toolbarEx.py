
import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow,
    QWidget, QLabel, QToolBar, QStatusBar, QCheckBox
)
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt, QSize


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label)


        toolbar = QToolBar("My main Toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        button_action = QAction(QIcon("../../data/abacus.png"), "MyButton", self)
        button_action.setStatusTip("This is your button")       # Put status string for corresponding QAction
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        #button_action.toggled.connect()
        toolbar.addAction(button_action)

        toolbar.addSeparator()
        button_action2 = QAction(QIcon("../../data/abacus.png"), "MyButton2", self)
        button_action2.setStatusTip("This is your second button!")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        toolbar.addSeparator()
        toolbar.addWidget(QLabel("Hello"))
        toolbar.addWidget(QCheckBox())

        self.setStatusBar(QStatusBar(self))                 # Status string is shown here.


    def onMyToolBarButtonClick(self, s):
        #print(type(s))      # Bool : Always False since the button is uncheckable
        print("Click", s)    




def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()



if __name__=="__main__":
    main()

