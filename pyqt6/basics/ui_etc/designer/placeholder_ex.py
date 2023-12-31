
from PyQt6 import QtWidgets, uic
from pyqtgraph import PlotWidget
import pyqtgraph as pg
import sys


def main() -> None:
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        uic.loadUi("placeholder_ex.ui", self)
        self.plot([1, 2, 3, 4, 5,6, 7, 8, 9,10], [30, 32, 34, 32, 33, 31, 29, 32 ,35, 45])

    def plot(self, hour, temp):
        self.graphWidget.plot(hour, temp)
        

if __name__=="__main__":
    main()


