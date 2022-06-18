import os
import sys

dir = os.getcwd()
sys.path.insert(0, dir + "\Classification")
sys.path.insert(0, dir + "\DbProject")

from PyQt5.QtWidgets import QWidget, QPushButton

from Classification import *
from MainDB import *

class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(300, 200)
        self.move(300, 300)
        self.setWindowTitle('Main')

        self.buttonClassification = QPushButton('Classification')
        self.buttonClassification.move(50, 50)
        self.buttonClassification.setParent(self)
        self.buttonClassification.clicked.connect(self.buttonClickClassification)

        self.buttonDbProject = QPushButton('DBProject')
        self.buttonDbProject.move(200, 50)
        self.buttonDbProject.setParent(self)
        self.buttonDbProject.clicked.connect(self.buttonClickDbProject)


    def buttonClickClassification(self):
        self.classification = Classification()
        self.classification.show()

    def buttonClickDbProject(self):
        self.dbProject = MainDB()
        self.dbProject.show()
