import sys
import os

dir = os.getcwd()

sys.path.insert(0, dir + "/DataBaseEquipment")

from Container import *
from RingGamma import *
from RingConsolidation import *

from MainWindowUi import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.mainWindow = Ui_MainWindow()
        self.mainWindow.setupUi(self)

        self.mainWindow.actionShow_Data_Container.triggered.connect(self.actionShowDataContainer)
        self.mainWindow.actionShow_Data_RingGamma.triggered.connect(self.actionShowDataRingGamma)
        self.mainWindow.actionShow_Data_Consolidation.triggered.connect(self.actionShowDataRingConsolidation)

    def actionShowDataContainer(self):
        self.container = Container()
        self.container.show()

    def actionShowDataRingGamma(self):
        self.ringGamma = RingGamma()
        self.ringGamma.show()

    def actionShowDataRingConsolidation(self):
        self.ringConsolidation = RingConsolidation()
        self.ringConsolidation.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = MainWindow()
    main.show()

    app.exec_()
