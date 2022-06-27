import sys
import datetime
from math import pi

from RingGammaUi import *
from addRingGammaUi import *

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *

class RingGamma(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ringGamma = Ui_DBRingGamma()
        self.ringGamma.setupUi(self)
        self.connectDb()
        self.loadDataRingGamma()

        self.ringGamma.pushButtonAdd.clicked.connect(self.pushButtonAddClicked)
        self.ringGamma.pushButtonUpdate.clicked.connect(self.pushButtonEditClicked)
        self.ringGamma.pushButtonDelete.clicked.connect(self.pushButtonDeleteClicked)

    def pushButtonAddClicked(self):
        self.setAdd()

        if self.qdialog.exec_() == QDialog.Accepted:
            ringId = self.ui.lineEditRingId.text()
            ringWeight = self.ui.lineEditWeightRing.text()
            ringDiameter = self.ui.lineEditDiameterRing.text()
            ringThick = self.ui.lineEditThickRing.text()
            ringVolume = self.calcVolume(ringDiameter, ringThick)
            currentTime =self.currentTime()
            query = QSqlQuery()
            query.prepare(
                    "INSERT INTO tRingGamma (ROWID, idRingGamma, weightRingGamma, diameterRingGamma, thicknessRingGamma, volumeRingGamma, dateRingGamma)"
                    "VALUES (?, ?, ?, ?, ?, ?, ?)"
            )
            query.bindValue(0, None)
            query.bindValue(1, ringId)
            query.bindValue(2, ringWeight)
            query.bindValue(3, ringDiameter)
            query.bindValue(4, ringThick)
            query.bindValue(5, ringVolume)
            query.bindValue(6, str(currentTime))
            query.exec_()
            self.loadDataRingGamma()

    def pushButtonEditClicked(self):
        self.setAdd()

        ringId = self.ringGamma.tableWidget.item(self.ringGamma.tableWidget.currentRow(), 0).text()
        rowId = self.getRowId(ringId)
        ringWeight = self.ringGamma.tableWidget.item(self.ringGamma.tableWidget.currentRow(), 1).text()
        ringDiameter = self.ringGamma.tableWidget.item(self.ringGamma.tableWidget.currentRow(), 2).text()
        ringThick = self.ringGamma.tableWidget.item(self.ringGamma.tableWidget.currentRow(), 3).text()

        self.ui.lineEditRingId.setText(ringId)
        self.ui.lineEditWeightRing.setText(ringWeight)
        self.ui.lineEditDiameterRing.setText(ringDiameter)
        self.ui.lineEditThickRing.setText(ringThick)

        self.ui.lineEditWeightRing.textChanged.connect(lambda x: float(ringWeight))
        self.ui.lineEditDiameterRing.textChanged.connect(lambda x: float(ringDiameter))
        self.ui.lineEditThickRing.textChanged.connect(lambda x: float(ringThick))

        if self.qdialog.exec() == QDialog.Accepted:
            ringId = self.ui.lineEditRingId.text()
            ringWeight = self.ui.lineEditWeightRing.text()
            ringDiameter = self.ui.lineEditDiameterRing.text()
            ringThick = self.ui.lineEditThickRing.text()
            volume = self.calcVolume(ringDiameter, ringThick)
            currentTime = self.currentTime()
            query = QSqlQuery()
            query.exec_(
                '''
                    UPDATE tRingGamma
                    SET idRingGamma = %d, weightRingGamma = '%s', diameterRingGamma = '%s', thicknessRingGamma = '%s', volumeRingGamma = '%s', dateRingGamma = '%s'
                    WHERE ROWID = %d
                ''' %
                (
                int(ringId),
                ringWeight,
                ringDiameter,
                ringThick,
                volume,
                currentTime,
                rowId
                )
            )
            self.loadDataRingGamma()

    def pushButtonDeleteClicked(self):
        valIdRingGamma = self.ringGamma.tableWidget.item(self.ringGamma.tableWidget.currentRow(), 0).text()
        rowId = self.getRowId(valIdRingGamma)
        query = QSqlQuery()
        query.exec_(
            'DELETE FROM tRingGamma WHERE ROWID = %d' % rowId
        )
        self.loadDataRingGamma()

    def loadDataRingGamma(self):
        self.ringGamma.tableWidget.clear()
        self.ringGamma.tableWidget.setRowCount(self.getRowCount())
        columnHeaders = ['No. Ring', 'Weight (gr)', 'd (mm)', 't (mm)', 'V(mm^3)', 'Date']
        numberColumn = len(columnHeaders)
        self.ringGamma.tableWidget.setColumnCount(numberColumn)
        self.ringGamma.tableWidget.setHorizontalHeaderLabels(columnHeaders)
        self.setColTableWidget()

        query = QSqlQuery()
        row = 0
        query.exec_('VACUUM')
        query.exec_('SELECT * FROM tRingGamma')
        while query.next():
            for i in range(numberColumn):
                item = QTableWidgetItem()
                item.setText(str(query.value(i)))
                self.ringGamma.tableWidget.setItem(row, i, item)
            row += 1

    def getRowId(self, idRingGamma):
        query = QSqlQuery()
        query.exec_('SELECT ROWID, * FROM tRingGamma WHERE idRingGamma = %d' % int(idRingGamma))
        query.next()
        rowId = query.value(0)
        return rowId

    def getRowCount(self):
        query = QSqlQuery()
        query.exec_('SELECT COUNT(*) FROM tRingGamma')
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
        self.ui = Ui_addRingGamma()
        self.ui.setupUi(self.qdialog)
        self.qdialog.show()

    def calcVolume(self, diameter, thick):
        volume = 0.25 * pi * (float(diameter))**2 * float(thick)
        return round(volume, 3)

    def setColTableWidget(self):
        self.ringGamma.tableWidget.setColumnWidth(0, 80)
        self.ringGamma.tableWidget.setColumnWidth(1, 90)
        self.ringGamma.tableWidget.setColumnWidth(2, 70)
        self.ringGamma.tableWidget.setColumnWidth(3, 70)
        self.ringGamma.tableWidget.setColumnWidth(4, 90)
        self.ringGamma.tableWidget.horizontalHeader().setStretchLastSection(True)

    def currentTime(self):
        return datetime.date.today()



if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = RingGamma()
    main.show()

    app.exec_()
