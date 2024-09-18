import sys
import requests
import pandas as pd
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Real-time Data Sharing'
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.layout = QVBoxLayout()

        self.table = QTableWidget()
        self.layout.addWidget(self.table)

        self.update_button = QPushButton('Update Data')
        self.update_button.clicked.connect(self.update_data)
        self.layout.addWidget(self.update_button)

        self.setLayout(self.layout)
        self.show()

    def update_data(self):
        response = requests.get('http://127.0.0.1:5000/data')
        data = response.json()
        df = pd.DataFrame(data)
        self.table.setRowCount(len(df))
        self.table.setColumnCount(len(df.columns))
        self.table.setHorizontalHeaderLabels(df.columns)

        for i in range(len(df)):
            for j in range(len(df.columns)):
                self.table.setItem(i, j, QTableWidgetItem(str(df.iat[i, j])))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

