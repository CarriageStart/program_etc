import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow,
    QWidget, QDialog, QPushButton
)
from ui_dialog_employee import Ui_Dialog_Employee as F_Reg_Employee

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.centralWidget = QPushButton("Push me for register!")
        self.centralWidget.clicked.connect(self.onRegBtnClicked)
        self.setCentralWidget(self.centralWidget)

        self.regDig = EmployeeDig(self)

    def onRegBtnClicked(self):
        if not self.regDig.isVisible:
            self.regDig.show()
        self.regDig.pushButton.click()
        self.regDig.exec()


class EmployeeDig(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = F_Reg_Employee()
        self.ui.setupUi(self)
        self.pushButton = self.ui.pushButton



def main() -> None:
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()



if __name__=="__main__":
    main()


