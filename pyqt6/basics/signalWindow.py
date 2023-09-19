import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

from random import choice

window_titles = [
    "My App",
    "My App",
    "Still My App",
    "Still My App",
    "Hello, Kihoon",
    "Hello, Kihoon",
    "This is Surprising",
    "This is Surprising",
    "Today is wednesday",
    "Something went wrong"
]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.n_times_clicked = 0

        self.setWindowTitle("My App")
        self.button = QPushButton("Push Me!")
        self.button.clicked.connect(self.inButtonClicked)

        # This signal is triggered by the event handler of button
        #   => It is important not to make a loop of event handling....
        self.windowTitleChanged.connect(self.the_window_title_changed)
        self.setCentralWidget(self.button)

    def inButtonClicked(self):
        print("Clicked!")
        new_window_title = choice(window_titles)
        print("New window title : %s" % new_window_title)
        self.setWindowTitle(new_window_title)

    def the_window_title_changed(self, window_title):
        print("Window title changed : %s" % window_title)
        if window_title == "Something went wrong" :
            self.button.setDisabled(True)


def main() -> None:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()

if __name__ == "__main__" :
    main()

