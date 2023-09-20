
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Click in this window")

        self.setWindowTitle("My App")
        self.setCentralWidget(self.label)


    # Events Handling
    def mouseMoveEvent(self, e):    
        print("Mouse Move Issued")
        self.label.setText("mouseMoveEvent")

    def mousePressEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            # Handle the left-button press in here
            self.label.setText("mousePressEvent Left")
        elif e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("mousePressEvent Middle")
        elif e.button() == Qt.MouseButton.RightButton:
            self.label.setText("mousePressEvent Right")

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton :
            self.label.setText("mouseReleaseEvent Left")
        elif e.button() == Qt.MouseButton.MiddleButton :
            self.label.setText("mouseReleaseEvent Middle")
        elif e.button() == Qt.MouseButton.RightButton :
            self.label.setText("mouseReleaseEvent Right")

    def mouseDoubleClickEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton :
            self.label.setText("mouseDoubleClickEvent Left")
        elif e.button() == Qt.MouseButton.MiddleButton :
            self.label.setText("mouseDoubleClickEvent Middle")
        elif e.button() == Qt.MouseButton.RightButton :
            self.label.setText("mouseDoubleClickEvent Right")


def main() -> None:
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()



if __name__=="__main__" :
    main()





