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
            cbrId = self.ui.lineEditRingId.text()
            cbrWeight = self.ui.lineEditWeightRing.text()
            cbrDiameter = self.ui.lineEditDiameterRing.text()
            cbrThick = self.ui.lineEditThickRing.text()
            cbrVolume = self.calcVolume(cbrDiameter, cbrThick)
            currentTime = self.currentTime()
            query = QSqlQuery()
            query.prepare(
                "INSERT INTO tCbr (ROWID, idCbr, weightCbr, diameterCbr, thicknessCbr, volumeCbr, dateCbr)"
                "VALUES (?, ?, ?, ?, ?, ?, ?)"
            )
            query.bindValue(0, None)
            query.bindValue(1, cbrId)
            query.bindValue(2, cbrWeight)
            query.bindValue(3, cbrDiameter)
            query.bindValue(4, cbrThick)
            query.bindValue(5, cbrVolume)
            query.bindValue(6, str(currentTime))
            query.exec_()
            self.loadCbr()

    def pushButtonEditClicked(self):
        self.setAdd()

        cbrId = self.cbr.tableWidget.item(self.cbr.tableWidget.currentRow(), 0).text()
        rowId = self.getRowId(cbrId)
        cbrWeight = self.cbr.tableWidget.item(self.cbr.tableWidget.currentRow(), 1).text()
        cbrDiameter = self.cbr.tableWidget.item(self.cbr.tableWidget.currentRow(), 2).text()
        cbrThick = self.cbr.tableWidget.item(self.cbr.tableWidget.currentRow(), 3).text()

        self.ui.lineEditRingId.setText(cbrId)
        self.ui.lineEditWeightRing.setText(cbrWeight)
        self.ui.lineEditDiameterRing.setText(cbrDiameter)
        self.ui.lineEditThickRing.setText(cbrThick)

        self.ui.lineEditWeightRing.textChanged.connect(lambda x: float(cbrWeight))
        self.ui.lineEditDiameterRing.textChanged.connect(lambda x: float(cbrDiameter))
        self.ui.lineEditThickRing.textChanged.connect(lambda x: float(cbrThick))

        if self.qdialog.exec_() == QDialog.Accepted:
            cbrId = self.ui.lineEditRingId.text()
            cbrWeight = self.ui.lineEditWeightRing.text()
            cbrDiameter = self.ui.lineEditDiameterRing.text()
            cbrThick = self.ui.lineEditThickRing.text()
            volume = self.calcVolume(cbrDiameter, cbrThick)
            currentTime = datetime.datetime.now()

            query = QSqlQuery()
            query.exec_(
                '''
                    UPDATE tCbr
                    SET idCbr = %d, weightCbr = '%s', diameterCbr = '%s', thicknessCbr = '%s', volumeCbr = '%s', dateCbr = '%s'
                    WHERE ROWID = %d
                ''' %
                (
                int(cbrId),
                cbrWeight,
                cbrDiameter,
                cbrThick,
                volume,
                currentTime,
                rowId
                )
            )
            self.loadCbr()

    def pushButtonDeleteClicked(self):
        valIdCbr = self.cbr.tableWidget.item(self.cbr.tableWidget.currentRow(), 0).text()
        rowId = self.getRowId(valIdCbr)
        query = QSqlQuery()
        query.exec_(
            'DELETE FROM tCbr WHERE ROWID = %d' % rowId
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
        query.exec_('VACUUM')
        query.exec_('SELECT * FROM tCbr')
        while query.next():
            for i in range(numberColumn):
                item = QTableWidgetItem()
                item.setText(str(query.value(i)))
                self.cbr.tableWidget.setItem(row, i, item)
            row += 1

    def getRowId(self, idCbr):
        query = QSqlQuery()
        query.exec_('SELECT ROWID, * FROM tCbr WHERE idCbr = %d' % int(idCbr))
        query.next()
        rowId = query.value(0)
        return rowId

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

    def currentTime(self):
        return datetime.date.today()

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
