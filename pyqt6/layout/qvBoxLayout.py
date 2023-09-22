
import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout
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

        layout = QVBoxLayout()
        layout.addWidget(Color("red"))
        layout.addWidget(Color("green"))
        layout.addWidget(Color("blue"))
        layout.addWidget(Color("red"))
        layout.addWidget(Color("green"))
        layout.addWidget(Color("blue"))

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()



if __name__ == "__main__" :
    main()


