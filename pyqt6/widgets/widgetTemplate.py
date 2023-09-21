
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QMainWindow,
    QLabel, QCheckBox, QComboBox, QListWidget,
    QLineEdit, QSpinBox, QDoubleSpinBox, QSlider,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Widget App")


def main() -> None:
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

if __name__=="__main__":
    main()






