
import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow,
    QWidget,QLabel, QPushButton, QTabWidget
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

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.TabPosition.West)
        tabs.setMovable(True)

        for n, color in enumerate(["red", "green", "blue", "yellow"]):
            tabs.addTab(Color(color), color)

        self.setCentralWidget(tabs)


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec()



if __name__ == "__main__" :
    main()


