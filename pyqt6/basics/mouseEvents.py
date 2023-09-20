
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Click in this window")

        self.setWindowTitle("My App")
        self.setCentralWidget(self.label)


    # If you customize the widget, you can simply override the slots without registering
    def mouseMoveEvent(self, e):    # Mouse movement while clicking
        print("Mouse Move Issued")
        self.label.setText("mouseMoveEvent")

    # This doesn't check new events while "Press Event" is issued
    def mouseReleaseEvent(self, e):
        print("Mouse Release Issued")
        self.label.setText("mouseReleaseEvent")

    # This check new events while "Press Event" is issued. 
    # If is, conduct it and finally change the label text
    def mousePressEvent(self, e):
        print("Mouse Press Issued")
        super().mousePressEvent(e)
        self.label.setText("mousePressEvent")

    # This check new events while "Double Event" is issued. 
    # It first change the label, but the new "Press" event excuted in super.
    def mouseDoubleClickEvent(self, e):
        print("Mouse double click Issued")
        super().mouseDoubleClickEvent(e)
        self.label.setText("mouseDoubleClickEvent")


def main() -> None:
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()


if __name__=="__main__" :
    main()

