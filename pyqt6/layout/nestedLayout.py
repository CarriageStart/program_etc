
import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QHBoxLayout
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

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()


        layout2.addWidget(Color("red"))
        layout2.addWidget(Color("yellow"))
        layout2.addWidget(Color("purple"))

        layout1.addLayout(layout2)
        layout1.addWidget(Color("green"))

        layout3.addWidget(Color("blue"))
        layout3.addWidget(Color("purple"))

        layout1.addLayout(layout3)

        # Setting Layout
        layout1.setContentsMargins(0, 0, 0, 0)      # Spacing itself from its parent(holder)
        layout1.setSpacing(20)                      # Between QObject

        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)



def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()



if __name__ == "__main__" :
    main()


