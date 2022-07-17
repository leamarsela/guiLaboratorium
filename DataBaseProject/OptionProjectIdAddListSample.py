import sys

from OptionProjectIdAddListSampleUi import *

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *

class OptionProjectIdAddListSample(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.optionProjectIdAddListSample = Ui_OptionProjectIdAddListSample()
        self.optionProjectIdAddListSample.setupUi(self)
        self.connectDb()
        self.loadDataProject()
        self.spinBox()

    def spinBox(self):
        self.spinBox = self.optionProjectIdAddListSample.doubleSpinBox
        self.spinBox.setPrefix("Project ID: ")
        self.spinBox.setValue(int(self.dataListBox[-1]))
        self.spinBox.setRange(int(self.dataListBox[0]), int(self.dataListBox[-1]))
        self.spinBox.setSingleStep(1)
        self.spinBox.value()

    def loadDataProject(self):
        query = QSqlQuery()
        query.exec_('VACUUM')
        query.exec_('SELECT * FROM tProject')

        rec = query.record()

        self.dataListBox = []
        nameCol = rec.indexOf('idNumProject')
        while query.next():
            self.dataListBox.append(query.value(nameCol))

    def connectDb(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('./Database/dbLab')
        if db.open():
            print(db.isOpen())
        else:
            print('error')
            sys.exit(1)




if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = OptionProjectIdAddListSample()
    main.show()

    app.exec_()
