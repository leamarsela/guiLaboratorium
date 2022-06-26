import sys
import datetime
from math import pi

from CbrUi import *
from addCbrUi import *

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *

class Cbr(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.cbr = Ui_DBCbr()
        self.cbr.setupUi(self)
        self.connectDb()
        self.loadCbr()

        self.cbr.pushButtonAdd.clicked.connect(self.pushButtonAddClicked)
        self.cbr.pushButtonUpdate.clicked.connect(self.pushButtonEditClicked)
        self.cbr.pushButtonDelete.clicked.connect(self.pushButtonDeleteClicked)

    def pushButtonAddClicked(self):
        self.setAdd()

        if self.qdialog.exec_() == QDialog.Accepted:
            id = self.getRowCount() + 1
            cbrId = self.ui.lineEditRingId.text()
            cbrWeight = self.ui.lineEditWeightRing.text()
            cbrDiameter = self.ui.lineEditDiameterRing.text()
            cbrThick = self.ui.lineEditThickRing.text()
            cbrVolume = self.calcVolume(cbrDiameter, cbrThick)
            currentTime = datetime.datetime.now()
            query = QSqlQuery()
            query.exec_(
                "INSERT INTO tCbr VALUES (%d, '%s', '%s', '%s', '%s', '%s', '%s')" %
                (
                id,
                cbrId,
                cbrWeight,
                cbrDiameter,
                cbrThick,
                cbrVolume,
                currentTime
                )
            )
            self.loadCbr()

    def pushButtonEditClicked(self):
        self.setAdd()

        cbrId = self.cbr.tableWidget.item(self.cbr.tableWidget.currentRow(), 0).text()
        cbrWeight = self.cbr.tableWidget.item(self.cbr.tableWidget.currentRow(), 1).text()
        cbrDiameter = self.cbr.tableWidget.item(self.cbr.tableWidget.currentRow(), 2).text()
        cbrThick = self.cbr.tableWidget.item(self.cbr.tableWidget.currentRow(), 3).text()

        idxCbr = self.cbr.tableWidget.currentRow() + 1
        self.ui.lineEditRingId.setText(cbrId)
        self.ui.lineEditWeightRing.setText(cbrWeight)
        self.ui.lineEditDiameterRing.setText(cbrDiameter)
        self.ui.lineEditThickRing.setText(cbrThick)
        volume = self.calcVolume(cbrDiameter, cbrThick)
        currentTime = datetime.datetime.now()

        if self.qdialog.exec_() == QDialog.Accepted:
            query = QSqlQuery()
            query.exec_(
                '''
                    UPDATE tCbr
                    SET idCbr = %d, weightCbr = '%s', diameterCbr = '%s', thicknessCbr = '%s', volumeCbr = '%s', dateCbr = '%s'
                    WHERE idxCbr = %d
                ''' %
                (
                int(self.ui.lineEditRingId.text()),
                self.ui.lineEditWeightRing.text(),
                self.ui.lineEditDiameterRing.text(),
                self.ui.lineEditThickRing.text(),
                volume,
                currentTime,
                idxCbr
                )
            )
            self.loadCbr()

    def pushButtonDeleteClicked(self):
        idxCbr = self.cbr.tableWidget.currentRow() + 1
        query = QSqlQuery()
        query.exec_(
            'DELETE FROM tCbr WHERE idxCbr = %d' % idxCbr
        )
        self.loadCbr()

    def loadCbr(self):
        self.cbr.tableWidget.clear()
        self.cbr.tableWidget.setRowCount(self.getRowCount())
        columnHeaders = ['No. CBR', 'Weight (gr)', 'd (mm)', 't (mm)', 'V(mm^3)', 'Date']
        numberColumn = len(columnHeaders)
        self.cbr.tableWidget.setColumnCount(numberColumn)
        self.cbr.tableWidget.setHorizontalHeaderLabels(columnHeaders)
        self.setColTableWidget()

        query = QSqlQuery()
        row = 0
        query.exec_('SELECT * FROM tCbr')
        while query.next():
            for i in range(numberColumn):
                item = QTableWidgetItem()
                item.setText(str(query.value(i + 1)))
                self.cbr.tableWidget.setItem(row, i, item)
            row += 1

    def getRowCount(self):
        query = QSqlQuery()
        query.exec_('SELECT COUNT(*) FROM tCbr')
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

    def setAdd(self):
        self.qdialog = QtWidgets.QDialog()
        self.ui = Ui_addCbr()
        self.ui.setupUi(self.qdialog)
        self.qdialog.show()

    def calcVolume(self, diameter, thick):
        volume = 0.25 * pi * (float(diameter))**2 * float(thick)
        return round(volume, 3)

    def setColTableWidget(self):
        self.cbr.tableWidget.setColumnWidth(0, 80)
        self.cbr.tableWidget.setColumnWidth(1, 85)
        self.cbr.tableWidget.setColumnWidth(2, 65)
        self.cbr.tableWidget.setColumnWidth(3, 65)
        self.cbr.tableWidget.setColumnWidth(4, 100)
        self.cbr.tableWidget.horizontalHeader().setStretchLastSection(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = Cbr()
    main.show()

    app.exec_()
