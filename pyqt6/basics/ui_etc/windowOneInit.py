
import sys
from random import randint
from PyQt6.QtWidgets import (
    QApplication, QMainWindow,
    QVBoxLayout, QHBoxLayout,
    QWidget, QLabel, QPushButton
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = None
        self.setWindowTitle("My App")

        layout = QHBoxLayout()
        self.button = QPushButton("Push for new window and discard")
        self.button.clicked.connect(self.show_new_window)
        layout.addWidget(self.button)

        self.button1 = QPushButton("Push for new window and explicitly None")
        self.button1.clicked.connect(self.show_new_window1)
        layout.addWidget(self.button1)

        self.button2 = QPushButton("Push for one window")
        self.button2.clicked.connect(self.show_one_window)
        layout.addWidget(self.button2)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def show_new_window(self, checked):
        if self.w is None:
            self.w = AnotherWindow()
            self.w.show()
        else:
            self.w = None # If you want to discard the window


    def show_new_window1(self, checked):
        if self.w is None:
            self.w = AnotherWindow()
            self.w.show()
        else:
            self.w.close()
            self.w = None # If you want to discard the window


    def show_one_window(self, checked):
        if self.w is None:
            self.w = AnotherWindow()
            self.w.show()
            self.closed = False
        elif not self.closed:
            self.w.close()
            self.closed = True
            #self.w = None # If you want to discard the window
        else:
            self.w.show()
            self.closed = False



class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.label = QLabel("Another Window with %d" % randint(0, 100))
        layout.addWidget(self.label)
        self.setLayout(layout)


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()



if __name__=="__main__":
    main()



