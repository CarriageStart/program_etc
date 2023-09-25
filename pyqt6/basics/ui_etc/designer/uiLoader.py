import sys
from PyQt6 import uic
from PyQt6.QtWidgets import (
    QApplication, QMainWindow
)
from uiConverted import Ui_MainWindow

# 1. Direct-load with uic.loadUi method
def main():
    window = uic.loadUi("test.ui")  # XML format UI file : Load here!
    window.show()
    
    app.exec()



# 2. Embedding-load with uic.loadUi method
class MainWindow1(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("test.ui", self) # Load with-in init block

def main1():
    window = MainWindow1()
    window.show()
    
    app.exec()


# 3. By inheriting the converted Ui source class
class MainWindow2(QMainWindow, Ui_MainWindow):
    def __init__(self, obj=None, *args, **kwargs):
        super(MainWindow2, self).__init__(*args, **kwargs)
        self.setupUi(self)

def main2():
    window = MainWindow2()
    window.show()
    
    app.exec()



if __name__=="__main__":
    app = QApplication(sys.argv)
    main()
    main1()
    main2()




