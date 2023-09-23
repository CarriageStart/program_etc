
import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QGridLayout
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

        # Automatically, resize the grid structure (row x col)
        layout = QGridLayout()
        # Typical addWidget of GridLayout : addWidget(QObject, row_index, col_index)
        layout.addWidget(Color("red"), 0, 0)
        layout.addWidget(Color("green"), 1, 0)
        layout.addWidget(Color("blue"), 1, 1)
        layout.addWidget(Color("purple"), 2, 1)

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


