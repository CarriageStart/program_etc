from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

# Skeleton QApplication initialization
#   - To use the static methods in Qt objects like QWidget
app = QApplication(sys.argv)

# Create Empy Widget
window = QMainWindow()
window.show()

app.exec() # Start the evet loop

# Shouldn't reach here 

