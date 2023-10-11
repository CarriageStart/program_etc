#from PyQt6.QtGui import 
from PyQt6.QtWidgets import (
    QApplication, QMainWindow,
    QVBoxLayout,
    QWidget, QLabel, QPushButton
)
from PyQt6.QtCore import QTimer

import time

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.counter = 0

        layout = QVBoxLayout()
        self.l = QLabel("Start")
        b = QPushButton("Danger!")
        b.pressed.connect(self.oh_no)
        layout.addWidget(self.l)
        layout.addWidget(b)

        w = QWidget()
        w.setLayout(layout)

        self.setCentralWidget(w)
        self.show()

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()

    def oh_no(self):
        time.sleep(5)

    def recurring_timer(self):
        self.counter += 1
        self.l.setText("Counter %d" % self.counter)



def main() -> None:
    app = QApplication([])
    window = MainWindow()
    app.exec()
    


if __name__=="__main__":
    main()

