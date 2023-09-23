
import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, 
    QStackedLayout, QVBoxLayout, QHBoxLayout,
    QWidget, QPushButton,QLabel
)
from PyQt6.QtGui import QPalette, QColor



# Color only Widget
class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        # Initiate the palette before use.
        palette = self.palette()
        palette.setColor(
                # Position to set    , Color
            QPalette.ColorRole.Window, QColor(color)
        )
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My APP")

        layout = QStackedLayout()
        layout.addWidget(Color("red"))
        layout.addWidget(Color("green"))
        layout.addWidget(Color("blue"))
        layout.addWidget(Color("yellow"))

        layout.setCurrentIndex(1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


class MainWindow2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        pagelayout = QVBoxLayout()
        button_layout = QHBoxLayout()
        self.stackLayout = QStackedLayout()

        pagelayout.addLayout(button_layout)
        pagelayout.addLayout(self.stackLayout)

        btn = QPushButton("red")
        btn.pressed.connect(self.stack_activate_1)
        button_layout.addWidget(btn)
        self.stackLayout.addWidget(Color("red"))

        btn = QPushButton("yellow")
        btn.pressed.connect(self.stack_activate_2)
        button_layout.addWidget(btn)
        self.stackLayout.addWidget(Color("yellow"))

        btn = QPushButton("green")
        btn.pressed.connect(self.stack_activate_3)
        button_layout.addWidget(btn)
        self.stackLayout.addWidget(Color("green"))

        widget = QWidget()
        widget.setLayout(pagelayout)
        self.setCentralWidget(widget)
    
    def stack_activate_1(self):
        self.stackLayout.setCurrentIndex(0)

    def stack_activate_2(self):
        self.stackLayout.setCurrentIndex(1)

    def stack_activate_3(self):
        self.stackLayout.setCurrentIndex(2)



def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

    window = MainWindow2()
    window.show()

    app.exec()


if __name__ == "__main__" :
    main()


