
import sys

from PyQt6.QtWidgets import (
    QApplication, QMainWindow,
    QWidget, QCheckBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction



def main() -> None:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()


class MainWindow(QMainWindow): 
    def __init__(self):
        super(MainWindow, self).__init__()
        checkbox = QCheckBox("Check?")

        def checkstate_to_bool(state):
            #if state==0:
            if state == Qt.CheckState.Checked.value:
                return self.result(True)
            return self.result(False)

        checkbox.stateChanged.connect(checkstate_to_bool)

        _convert = {
            Qt.CheckState.Checked.value: True,
            Qt.CheckState.Unchecked.value: False,
        }
        checkbox.stateChanged.connect(
            lambda v: self.result(_convert[v])
        )
        self.setCentralWidget(checkbox)

    def result(self, v):
        print(f"{v=}")



if __name__ == "__main__":
    main()



