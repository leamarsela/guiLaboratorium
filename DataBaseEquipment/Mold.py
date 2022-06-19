import sys
import datetime
from math import pi

from MoldUi import *
from addMoldUi import *

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *

class Mold(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.mold = Ui_DBMold()
        self.mold.setupUi(self)
        self.connectDb()
        self.loadMold()

        self.mold.pushButtonAdd.clicked.connect(self.pushButtonAddClicked)
        self.mold.pushButtonUpdate.clicked.connect(self.pushButtonEditClicked)
        self.mold.pushButtonDelete.clicked.connect(self.pushButtonDeleteClicked)

    def pushButtonAddClicked(self):
        self.qdialog = QtWidgets.QDialog()
        self.ui = Ui_addMold()
        self.ui.setupUi(self.qdialog)
        self.qdialog.show()

        if self.qdialog.exec_() == QDialog.Accepted:
            id = self.getRowCount() + 1
            moldId = self.ui.lineEditRingId.text()
            moldWeight = self.ui.lineEditWeightRing.text()
            moldDiameter = self.ui.lineEditDiameterRing.text()
            moldThick = self.ui.lineEditThickRing.text()
            moldVolume = self.calcVolume(moldDiameter, moldThick)
            currentTime = datetime.datetime.now()
            query = QSqlQuery()
            query.exec_(
                "INSERT INTO tMold VALUES (%d, '%s', '%s', '%s', '%s', '%s', '%s')" %
                (
                id,
                moldId,
                moldWeight,
                moldDiameter,
                moldThick,
                moldVolume,
                currentTime
                )
            )
            self.loadMold()

    def pushButtonEditClicked(self):
        self.qdialog = QtWidgets.QDialog()
        self.ui = Ui_addMold()
        self.ui.setupUi(self.qdialog)
        self.qdialog.show()

        moldId = self.mold.tableWidget.item(self.mold.tableWidget.currentRow(), 0).text()
        moldWeight = self.mold.tableWidget.item(self.mold.tableWidget.currentRow(), 1).text()
        moldDiameter = self.mold.tableWidget.item(self.mold.tableWidget.currentRow(), 2).text()
        moldThick = self.mold.tableWidget.item(self.mold.tableWidget.currentRow(), 3).text()

        idxMold = self.mold.tableWidget.currentRow() + 1
        self.ui.lineEditRingId.setText(moldId)
        self.ui.lineEditWeightRing.setText(moldWeight)
        self.ui.lineEditDiameterRing.setText(moldDiameter)
        self.ui.lineEditThickRing.setText(moldThick)
        volume = self.calcVolume(moldDiameter, moldThick)
        currentTime = datetime.datetime.now()

        if self.qdialog.exec_() == QDialog.Accepted:
            query = QSqlQuery()
            query.exec(
                '''
                    UPDATE tMold
                    SET idMold = %d, weightMold = '%s', diameterMold = '%s', thicknessMold = '%s', volumeMold = '%s', dateMold = '%s'
                    WHERE idxMold = %d
                ''' %
                (
                int(self.ui.lineEditRingId.text()),
                self.ui.lineEditWeightRing.text(),
                self.ui.lineEditDiameterRing.text(),
                self.ui.lineEditThickRing.text(),
                volume,
                currentTime,
                idxMold
                )
            )
            self.loadMold()

    def pushButtonDeleteClicked(self):
        idxMold = self.mold.tableWidget.currentRow() + 1
        query = QSqlQuery()
        query.exec_(
            'DELETE FROM tMold WHERE idxMold = %d' % idxMold
        )
        self.loadMold()

    def loadMold(self):
        self.mold.tableWidget.clear()
        self.mold.tableWidget.setRowCount(self.getRowCount())
        columnHeaders = ['No. Mold', 'Weight (gr)', 'd (mm)', 't (mm)', 'V(mm^3)', 'Date']
        numberColumn = len(columnHeaders)
        self.mold.tableWidget.setColumnCount(numberColumn)
        self.mold.tableWidget.setHorizontalHeaderLabels(columnHeaders)

        query = QSqlQuery()
        row = 0
        query.exec_('SELECT * FROM tMold')
        while query.next():
            for i in range(numberColumn):
                item = QTableWidgetItem()
                item.setText(str(query.value(i + 1)))
                self.mold.tableWidget.setItem(row, i, item)
            row += 1

    def getRowCount(self):
        query = QSqlQuery()
        query.exec_('SELECT COUNT(*) FROM tMold')
        query.next()
        rowCount = query.value(0)
        return rowCount

    def connectDb(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('./Database/dbLab')
        if db.open():
            print(db.isOpen())
        else:
            print('error')
            sys.exit(1)

    def calcVolume(self, diameter, thick):
        volume = 0.25 * pi * (float(diameter))**2 * float(thick)
        return volume


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = Mold()
    main.show()

    app.exec_()
