import sys
import os

dir = os.getcwd()

sys.path.insert(0, dir + "/DataBaseEquipment")
sys.path.insert(0, dir + "/DataBaseProject")

from Container import *
from RingGamma import *
from RingConsolidation import *
from Mold import *
from Cbr import *
from Pycnometer import *
from ProvingRing import *
from OptionProjectId import *
from OptionProjectIdAddListSample import *
# from ListSample import *

from Project import *

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
        self.mainWindow.actionShow_Data_Mold.triggered.connect(self.actionShowDataMold)
        self.mainWindow.actionShow_Data_Cbr.triggered.connect(self.actionShowDataCbr)
        self.mainWindow.actionShow_Data_Pycnometer.triggered.connect(self.actionShowDataPycno)
        self.mainWindow.actionShow_Data_ProvingRing.triggered.connect(self.actionShowDataProvingRing)
        self.mainWindow.actionShow_All_Project.triggered.connect(self.actionShowDataProject)
        self.mainWindow.actionShow_List_Sample.triggered.connect(self.actionShowListSample)
        self.mainWindow.actionAdd_List_Sample.triggered.connect(self.actionAddListSample)

    def actionShowDataContainer(self):
        self.container = Container()
        self.container.show()

    def actionShowDataRingGamma(self):
        self.ringGamma = RingGamma()
        self.ringGamma.show()

    def actionShowDataRingConsolidation(self):
        self.ringConsolidation = RingConsolidation()
        self.ringConsolidation.show()

    def actionShowDataMold(self):
        self.mold = Mold()
        self.mold.show()

    def actionShowDataCbr(self):
        self.cbr = Cbr()
        self.cbr.show()

    def actionShowDataPycno(self):
        self.pycno = Pycnometer()
        self.pycno.show()

    def actionShowDataProvingRing(self):
        self.provingRing = ProvingRing()
        self.provingRing.show()

    def actionShowDataProject(self):
        self.project = Project()
        self.project.show()

    def actionShowListSample(self):
        self.optionProjectId = OptionProjectId()
        self.optionProjectId.show()

    def actionAddListSample(self):
        self.optionProjectIdAddListSample = OptionProjectIdAddListSample()
        self.optionProjectIdAddListSample.show()




    #     self.listSample = ListSample()
    #     self.listSample.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = MainWindow()
    main.show()

    app.exec_()
