
import sys

from PyQt6.QtWidgets import (
    QApplication, QMainWindow,
    QVBoxLayout, QHBoxLayout,
    QWidget, QPushButton, QLabel
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction



def main() -> None:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()


class MainWindow(QMainWindow): 
    def __init__(self):
        super().__init__()

        v = QVBoxLayout()
        h = QHBoxLayout()

        for a in range(10):
            button = QPushButton(str(a))
            button.pressed.connect(
                lambda val=a: self.button_pressed(val)
                #(x) lambda: self.button_pressed(a)
                # Lambda is executed after for loop, therefore, the value of "a" is always 9.
                # To avoid runtime-determined value(result), we need to record "a" statically(callable-statically),
                # as "lambda val=a", which save the value of a in the creation of callable(callable-static)
                # With this, we don't even have to check whether a is alive or not.
            )
            h.addWidget(button)

        v.addLayout(h)
        self.label = QLabel("")
        v.addWidget(self.label)
        
        w = QWidget()
        w.setLayout(v)
        self.setCentralWidget(w)

    def button_pressed(self, n):
        self.label.setText(str(n))


if __name__ == "__main__":
    main()



