
import sys

from PyQt6.QtWidgets import (
    QApplication, QMainWindow,
    QWidget
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction


"""
def fn(checked):
    self.handle_trigger(checked, <additional args>)

lambda checked: self.handle_trigger(checked, <additional args>)


action = QAction()
action.triggered.connect(lambda checked: self.handle_trigger(checked, action))
"""

def main() -> None:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()


class MainWindow(QMainWindow): 
    def __init__(self):
        super().__init__()
        self.windowTitleChanged.connect(self.on_window_title_changed)
        self.windowTitleChanged.connect(lambda x: self.on_window_title_changed_no_params())
        self.windowTitleChanged.connect(lambda x: self.my_custom_fn())
        self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x, 25))
        self.setWindowTitle("My Signal App")


    def on_window_title_changed(self, s):
        print(s)

    def on_window_title_changed_no_params(self):
        print("Window title changed.")

    def my_custom_fn(self, a="Hello!", b=5):
        print(a, b)


if __name__ == "__main__":
    main()


