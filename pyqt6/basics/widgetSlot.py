import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget


def main() -> None :
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.label = QLabel()
        self.input = QLineEdit()
        # Connect between widgets as slot
        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()  #
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)


if __name__ == "__main__" :
    main()
    


