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
        self.qdialog = QtWidgets.QDialog()
        self.ui = Ui_addRingGamma()
        self.ui.setupUi(self.qdialog)
        self.qdialog.show()

        if self.qdialog.exec_() == QDialog.Accepted:
            id = self.getRowCount() + 1
            ringId = self.ui.lineEditRingId.text()
            ringWeight = self.ui.lineEditWeightRing.text()
            ringDiameter = self.ui.lineEditDiameterRing.text()
            ringThick = self.ui.lineEditThickRing.text()
            ringVolume = self.calcVolume(ringDiameter, ringThick)
            currentTime = datetime.datetime.now()
            query = QSqlQuery()
            query.exec_(
                "INSERT INTO tRingGamma VALUES (%d, '%s', '%s', '%s', '%s', '%s', '%s')" %
                (
                id,
                ringId,
                ringWeight,
                ringDiameter,
                ringThick,
                ringVolume,
                currentTime
                )
            )
            self.loadDataRingGamma()

    def pushButtonEditClicked(self):
        self.qdialog = QtWidgets.QDialog()
        self.ui = Ui_addRingGamma()
        self.ui.setupUi(self.qdialog)
        self.qdialog.show()

        ringId = self.ringGamma.tableWidget.item(self.ringGamma.tableWidget.currentRow(), 0).text()
        ringWeight = self.ringGamma.tableWidget.item(self.ringGamma.tableWidget.currentRow(), 1).text()
        ringDiameter = self.ringGamma.tableWidget.item(self.ringGamma.tableWidget.currentRow(), 2).text()
        ringThick = self.ringGamma.tableWidget.item(self.ringGamma.tableWidget.currentRow(), 3).text()

        indexRingGamma = self.ringGamma.tableWidget.currentRow() + 1
        self.ui.lineEditRingId.setText(ringId)
        self.ui.lineEditWeightRing.setText(ringWeight)
        self.ui.lineEditDiameterRing.setText(ringDiameter)
        self.ui.lineEditThickRing.setText(ringThick)
        volume = self.calcVolume(ringDiameter, ringThick)
        currentTime = datetime.datetime.now()

        if self.qdialog.exec() == QDialog.Accepted:
            query = QSqlQuery()
            query.exec_(
                '''
                    UPDATE tRingGamma
                    SET idRingGamma = %d, weightRingGamma = '%s', diameterRingGamma = '%s', thicknessRingGamma = '%s', volumeRingGamma = '%s', dateRingGamma = '%s'
                    WHERE idxRingGamma = %d
                ''' %
                (
                int(self.ui.lineEditRingId.text()),
                self.ui.lineEditWeightRing.text(),
                self.ui.lineEditDiameterRing.text(),
                self.ui.lineEditThickRing.text(),
                volume,
                currentTime,
                indexRingGamma
                )
            )
            self.loadDataRingGamma()

    def pushButtonDeleteClicked(self):
        idxRingGamma = self.ringGamma.tableWidget.currentRow() + 1
        query = QSqlQuery()
        query.exec_(
            'DELETE FROM tRingGamma WHERE idxRingGamma = %d' % idxRingGamma
        )
        self.loadDataRingGamma()

    def loadDataRingGamma(self):
        self.ringGamma.tableWidget.clear()
        self.ringGamma.tableWidget.setRowCount(self.getRowCount())
        columnHeaders = ['No. Ring', 'Weight (gr)', 'd (mm)', 't (mm)', 'V(mm^3)', 'Date']
        numberColumn = len(columnHeaders)
        self.ringGamma.tableWidget.setColumnCount(numberColumn)
        self.ringGamma.tableWidget.setHorizontalHeaderLabels(columnHeaders)

        query = QSqlQuery()
        idRing, wrightRing, dRing, tRing, dateRing = range(5)
        row = 0
        query.exec_('SELECT * FROM tRingGamma')
        while query.next():
            for i in range(numberColumn):
                item = QTableWidgetItem()
                item.setText(str(query.value(i + 1)))
                self.ringGamma.tableWidget.setItem(row, i, item)
            row += 1

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

    def calcVolume(self, diameter, thick):
        volume = 0.25 * pi * (float(diameter))**2 * float(thick)
        return volume

if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = RingGamma()
    main.show()

    app.exec_()
