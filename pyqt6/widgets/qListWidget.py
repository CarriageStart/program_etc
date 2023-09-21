
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

        widget = QListWidget()
        widget.addItems(["One", "Two", "Three"])

        widget.currentItemChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)
    
    def index_changed(self, i):
        print("Index : ", i)
        print("Index.dir : ", dir(i))
        print("Index text : ", i.text())

    def text_changed(self, s):
        print("Label : %s" % s)


def main() -> None:
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()


if __name__=="__main__":
    main()






