import os
import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *



class LabRequest(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(800, 400)
        self.move(500, 500)
        self.setWindowTitle('Request')

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['id', 'name', 'date'])

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        self.setLayout(layout)





if __name__ == '__main__':
    app = QApplication(sys.argv)

    lab = LabRequest()
    lab.show()

    app.exec_()
