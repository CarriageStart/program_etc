
import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow,
    QWidget, QLabel, QToolBar, QStatusBar, QCheckBox
)
from PyQt6.QtGui import QAction, QIcon, QKeySequence
from PyQt6.QtCore import Qt, QSize


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        label = QLabel("Hello")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label)

        # toolBar
        toolbar = QToolBar("My main Toolbar")
        toolbar.setIconSize(QSize(16, 16))

        button1 = QAction(QIcon("../../data/acorn.png"), "Button 1", self)
        button1.setStatusTip("This is the first button!")
        button1.triggered.connect(self.onMytoolBarButtonClick)
        button1.setCheckable(True)
        button1.setShortcut(QKeySequence("Ctrl+p")) # Per-window Shortcut for the action
        toolbar.addAction(button1)
        toolbar.addSeparator()

        button2 = QAction(QIcon("../../data/acorn.png"), "Button 2", self)
        button2.setStatusTip("This is the second button!")
        button2.triggered.connect(self.onMytoolBarButtonClick)
        button2.setCheckable(True)
        toolbar.addAction(button2)

        toolbar.addWidget(QLabel("Hello"))
        toolbar.addWidget(QCheckBox())
        self.addToolBar(toolbar)
        
        # MenuBar
        menu = self.menuBar()               # Menu  != Toolbar
        file_menu = menu.addMenu("&File")   # & : means shortcut with "Alt" => Alt + f
        file_menu.addAction(button1)
        file_menu.addSeparator()
        file_menu.addAction(button2)
        file_sub_menu = file_menu.addMenu("Submenu")
        file_sub_menu.addAction(button1)
        file_sub_menu.addAction(button2)

        # Status Bar
        self.setStatusBar(QStatusBar(self))


    def onMytoolBarButtonClick(self, s):
        print("Clicked! : ", s)



def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()



if __name__=="__main__":
    main()

