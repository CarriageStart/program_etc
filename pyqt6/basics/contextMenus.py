import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QMainWindow, QMenu, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Context Menu")

    # Window specific : Make proper context menu for each circumstance
    # In context menu pop-up, construct the context menu and start event loop.
    def contextMenuEvent(self, e):
        print(type(e))
        context = QMenu(self)
        context.addAction(QAction("Test 1", self))
        context.addAction(QAction("Test 2", self))
        context.addAction(QAction("Test 3", self))
        context.exec(e.globalPos())
        super().contextMenuEvent(e)

    def mousePressEvent(self, e):
        if e.button == Qt.MouseButton.RightButton :
            print("Right Clicked")


class MainWindow2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.show()

        self.setWindowTitle("My Context Menu")
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.on_context_menu)


    # Window specific : Make proper context menu for each circumstance
    # In context menu pop-up, construct the context menu and start event loop.
    def on_context_menu(self, pos):
        context = QMenu(self)
        context.addAction(QAction("Test 1", self))
        context.addAction(QAction("Test 2", self))
        context.addAction(QAction("Test 3", self))
        context.exec(self.mapToGlobal(pos))

    def mousePressEvent(self, e):
        if e.button == Qt.MouseButton.RightButton :
            print("Right Clicked")

def main() -> None:
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec()

    window = MainWindow2()
    app.exec()



if __name__=="__main__":
    main()



