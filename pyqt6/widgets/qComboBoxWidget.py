
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
        self.setWindowTitle("ComboBox App")

        widget = QComboBox()
        widget.addItems(["One", "Two", "Three"])

        # Sends the current index (position) of the selected item
        widget.currentIndexChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_change)
        widget.setEditable(True)

        self.setCentralWidget(widget)


    def index_changed(self, i): # i is index (focus of combobox)
        print("Index is changed : %d" % i)

    def text_change(self, s):      # s is Str
        print("text is changed : %s" % s)


def main() -> None:
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()

if __name__=="__main__":
    main()






