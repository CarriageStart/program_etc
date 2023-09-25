
import sys
from random import randint
from PyQt6.QtWidgets import (
    QApplication, QMainWindow,
    QVBoxLayout,
    QWidget, QLabel, QPushButton
)

class OpMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.window1 = AnotherWindow()
        self.window2 = AnotherWindow()

        layout = QVBoxLayout()
        self.button1 = QPushButton("Push for new window1")
        self.button1.clicked.connect(
            lambda checked: self.show_new_window(self.window1)
        )
        layout.addWidget(self.button1)

        self.button2 = QPushButton("Push for new window2")
        self.button2.clicked.connect(
            lambda checked: self.show_new_window(self.window2)
        )
        layout.addWidget(self.button2)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


    def show_new_window(self, window):
        if window.isVisible():
            window.hide()
        else:
            window.show()



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.window1 = AnotherWindow()
        self.window2 = AnotherWindow()

        layout = QVBoxLayout()
        self.button1 = QPushButton("Push for new window1")
        self.button1.clicked.connect(self.show_new_window1)
        layout.addWidget(self.button1)

        self.button2 = QPushButton("Push for new window2")
        self.button2.clicked.connect(self.show_new_window2)
        layout.addWidget(self.button2)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


    def show_new_window1(self):
        if self.window1.isVisible():
            self.window1.hide()
        else:
            self.window1.show()


    def show_new_window2(self):
        if self.window2.isVisible():
            self.window2.hide()
        else:
            self.window2.show()


class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.label = QLabel("Another Window with %d" % randint(0, 100))
        layout.addWidget(self.label)
        self.setLayout(layout)


def main():
    app = QApplication(sys.argv)

    window = OpMainWindow()
    window.show()

    app.exec()

    window = MainWindow()
    window.show()

    app.exec()



if __name__=="__main__":
    main()



