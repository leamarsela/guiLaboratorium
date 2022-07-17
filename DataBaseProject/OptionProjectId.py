import sys

from OptionProjectIdUi import *
from ListSample import *

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *

class OptionProjectId(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.optionProject = Ui_OptionProject()
        self.optionProject.setupUi(self)
        self.connectDb()
        self.loadDataProject()
        self.spinBox()

        self.optionProject.pushButton.clicked.connect(self.tutup)

    def spinBox(self):
        self.spinBox = self.optionProject.doubleSpinBox
        self.spinBox.setPrefix("Project ID: ")
        self.spinBox.setValue(int(self.dataListBox[-1]))
        self.spinBox.setRange(int(self.dataListBox[0]), int(self.dataListBox[-1]))
        self.spinBox.setSingleStep(1)
        self.spinBox.value()

    def tutup(self):
        self.close()
        self.listSample = ListSample()
        self.listSample.show()
        self.listSample.label.setText('Project ID: ' + str(int(self.spinBox.value())))

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

    main = OptionProjectId()
    main.show()

    app.exec_()
