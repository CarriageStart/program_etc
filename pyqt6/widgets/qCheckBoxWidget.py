
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QMainWindow,
    QLabel, QCheckBox, QComboBox, QListWidget,
    QLineEdit, QSpinBox, QDoubleSpinBox, QSlider,
)

# Combo box as a binary state
class MainWindow_Tri(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tri-state App")

        widget = QCheckBox()
        widget.setCheckState(Qt.CheckState.Checked)
        widget.setTristate(True)
        widget.stateChanged.connect(self.show_state)

        self.setCentralWidget(widget)

    def show_state(self, s):
        print(Qt.CheckState(s) == Qt.CheckState.Checked)


# Combo box as a binary state
class MainWindow_Bi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bi-state App")

        widget = QCheckBox()
        widget.setCheckState(Qt.CheckState.Checked)
        widget.stateChanged.connect(self.show_state)

        self.setCentralWidget(widget)

    def show_state(self, s):
        print(Qt.CheckState(s) == Qt.CheckState.Checked)


def main() -> None:
    app = QApplication(sys.argv)

    window = MainWindow_Bi()
    window.show()

    app.exec()

    window = MainWindow_Tri()
    window.show()

    app.exec()

if __name__=="__main__":
    main()






