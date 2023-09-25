
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
        self.setWindowTitle("My App")
        self.w = AnotherWindow()

        layout = QHBoxLayout()
        self.button = QPushButton("Push for the existing window")
        self.button.clicked.connect(self.toggle_window)
        layout.addWidget(self.button)

        self.button1 = QPushButton("Update the window number")
        self.button1.clicked.connect(self.w.update_number)
        layout.addWidget(self.button1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


    def toggle_window(self, checked):
        if self.w.isVisible():
            self.w.hide()
            #self.w.close()     # The window is still updatable in close state
        else:
            self.w.show()

    def update_number(self, checked):
        self.w.update_number()


class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.label = QLabel("Another Window with %d" % randint(0, 100))
        layout.addWidget(self.label)
        self.setLayout(layout)

    def update_number(self):
        self.label.setText("Another Window with %d" % randint(0, 100))


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()



if __name__=="__main__":
    main()



