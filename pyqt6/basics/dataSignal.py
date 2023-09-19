import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow_WidgetState(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Receive the data of the event")

        button = QPushButton("Press Me!")
        button.setCheckable(True)                   
        # Multiple slots can be hooked to one kind of event.
        button.clicked.connect(self.methodInClicked) 
        button.clicked.connect(self.isToggled)         

        self.setCentralWidget(button)


    def methodInClicked(self):
        print("Clicked!")

    def isToggled(self, checked):       # Implicitly the data is conveyed as parameter.
        print("Checked?!?", checked)    # Print the toggle state after event
    

class MainWindow_StoreData(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button_is_toggled = True
        self.button_is_toggled2 = True

        self.setWindowTitle("Receive the data of the event")

        self.button = QPushButton("Press Me!")
        self.button.setCheckable(True)                   
        self.button.clicked.connect(self.methodInClicked) 
        self.button.clicked.connect(self.without_parameter) 
        self.button.setChecked(self.button_is_toggled)         

        self.setCentralWidget(self.button)


    def methodInClicked(self, checked):
        self.button_is_toggled = checked    # Retrieve data via callbacks
        print("Clicked! : ", self.button_is_toggled)

    def without_parameter(self):
        self.button_is_toggled2 = self.button.isChecked()    # Retrieve data via callbacks
        print("Clicked! : ", self.button_is_toggled2)


class MainWindow_OtherState(QMainWindow) :
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MyApp")
        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.the_button_was_clicked)
        
        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        self.button.setText("You already clicked me.")
        self.button.setEnabled(False)   
        # "Enable State" => Clickable 
        # "Unable State" => Non-Clickable 

        # Also change the window title
        self.setWindowTitle("My Oneshot App")



def main() -> None :
    app = QApplication(sys.argv)
    window = MainWindow_WidgetState()
    window.show()

    app.exec()

    window = MainWindow_StoreData()
    window.show()

    app.exec()

    window = MainWindow_OtherState()
    window.show()

    app.exec()


if __name__ == "__main__" :
    main()



