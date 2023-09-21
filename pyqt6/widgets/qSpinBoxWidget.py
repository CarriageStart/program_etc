
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QMainWindow,
    QLabel, QCheckBox, QComboBox, QListWidget,
    QLineEdit, QSpinBox, QDoubleSpinBox, QSlider,
)


class MainWindow_Spinbox(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Spinbox App")

        widget = QSpinBox()
        widget.setMinimum(-10)
        widget.setMaximum(3)
        widget.setPrefix("c")
        widget.setSuffix("$")
        widget.setSingleStep(3) # increment and decrement in the unit of 3

        widget.valueChanged.connect(self.value_changed)
        widget.textChanged.connect(self.value_changed_str)

        self.setCentralWidget(widget)

    def value_changed(self, i):
        print(i)

    def value_changed_str(self, s):
        print(s)



class MainWindow_DoubleSpinbox(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Spinbox App")

        widget = QDoubleSpinBox()
        widget.setRange(-10, 3)
        widget.setPrefix("$")
        widget.setSuffix("c")
        widget.setSingleStep(0.5) # increment and decrement in the unit of 0.5

        widget.valueChanged.connect(self.value_changed)
        widget.textChanged.connect(self.value_changed_str)

        self.setCentralWidget(widget)

    def value_changed(self, i):
        print(i)

    def value_changed_str(self, s):
        print(s)


def main() -> None:
    app = QApplication(sys.argv)

    window = MainWindow_Spinbox()
    window.show()

    app.exec()

    window = MainWindow_DoubleSpinbox()
    window.show()

    app.exec()


if __name__=="__main__":
    main()






