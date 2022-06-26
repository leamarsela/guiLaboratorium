import sys
import datetime
from math import pi

from RingConsolidationUi import *
from addRingConsolidationUi import *

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *

class RingConsolidation(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ringConsolidation = Ui_DBRingConsolidation()
        self.ringConsolidation.setupUi(self)
        self.connectDb()
        self.loadRingConsol()

        self.ringConsolidation.pushButtonAdd.clicked.connect(self.pushButtonAddClicked)
        self.ringConsolidation.pushButtonUpdate.clicked.connect(self.pushButtonEditClicked)
        self.ringConsolidation.pushButtonDelete.clicked.connect(self.pushButtonDeleteClicked)

    def pushButtonAddClicked(self):
        self.setAdd()

        if self.qdialog.exec() == QDialog.Accepted:
            ringId = self.ui.lineEditRingId.text()
            ringWeight = self.ui.lineEditWeightRing.text()
            ringDiameter = self.ui.lineEditDiameterRing.text()
            ringThick = self.ui.lineEditThickRing.text()
            ringVolume = self.calcVolume(ringDiameter, ringThick)
            currentTime = self.currentTime()
            query = QSqlQuery()
            query.prepare("INSERT INTO tRingConsolidation (ROWID, idRingConsol, weightRingConsol, diameterRingConsol, thicknessRingConsol, volumeRingConsol, dateRingConsol)"
                          "VALUES (?, ?, ?, ?, ?, ?, ?)")

            query.bindValue(0, None)
            query.bindValue(1, ringId)
            query.bindValue(2, ringWeight)
            query.bindValue(3, ringDiameter)
            query.bindValue(4, ringThick)
            query.bindValue(5, ringVolume)
            query.bindValue(6, str(currentTime))
            query.exec_()
            self.loadRingConsol()

    def pushButtonEditClicked(self):
        self.setAdd()

        ringId = self.ringConsolidation.tableWidget.item(self.ringConsolidation.tableWidget.currentRow(), 0).text()
        rowId = self.getRowId(ringId)
        ringWeight = self.ringConsolidation.tableWidget.item(self.ringConsolidation.tableWidget.currentRow(), 1).text()
        ringDiameter = self.ringConsolidation.tableWidget.item(self.ringConsolidation.tableWidget.currentRow(), 2).text()
        ringThick = self.ringConsolidation.tableWidget.item(self.ringConsolidation.tableWidget.currentRow(), 3).text()

        self.ui.lineEditRingId.setText(ringId)
        self.ui.lineEditWeightRing.setText(ringWeight)
        self.ui.lineEditDiameterRing.setText(ringDiameter)
        self.ui.lineEditThickRing.setText(ringThick)

        self.ui.lineEditWeightRing.textChanged.connect(lambda x: float(ringWeight))
        self.ui.lineEditDiameterRing.textChanged.connect(lambda x: float(ringDiameter))
        self.ui.lineEditThickRing.textChanged.connect(lambda x: float(ringThick))

        if self.qdialog.exec_() == QDialog.Accepted:
            ringId = self.ui.lineEditRingId.text()
            ringWeight = self.ui.lineEditWeightRing.text()
            ringDiameter = self.ui.lineEditDiameterRing.text()
            ringThick = self.ui.lineEditThickRing.text()
            volume = self.calcVolume(ringDiameter, ringThick)
            currentTime = self.currentTime()

            query = QSqlQuery()
            query.exec_(
                '''
                    UPDATE tRingConsolidation
                    SET idRingConsol = %d, weightRingConsol = '%s', diameterRingConsol = '%s', thicknessRingConsol = '%s', volumeRingConsol = '%s', dateRingConsol = '%s'
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
            self.loadRingConsol()

    def pushButtonDeleteClicked(self):
        valIdRingConsolidation = self.ringConsolidation.tableWidget.item(self.ringConsolidation.tableWidget.currentRow(), 0).text()
        rowId = self.getRowId(valIdRingConsolidation)
        query = QSqlQuery()
        query.exec_(
            'DELETE FROM tRingConsolidation WHERE ROWID = %d' % rowId
        )
        self.loadRingConsol()

    def loadRingConsol(self):
        self.ringConsolidation.tableWidget.clear()
        self.ringConsolidation.tableWidget.setRowCount(self.getRowCount())
        columnHeaders = ['No. Ring', 'Weight (gr)', 'd (mm)', 't (mm)', 'V(mm^3)', 'Date']
        numberColumn = len(columnHeaders)
        self.ringConsolidation.tableWidget.setColumnCount(numberColumn)
        self.ringConsolidation.tableWidget.setHorizontalHeaderLabels(columnHeaders)
        self.setColTableWidget()

        query = QSqlQuery()
        row = 0
        query.exec_('VACUUM')
        query.exec_('SELECT * FROM tRingConsolidation')
        while query.next():
            for i in range(numberColumn):
                item = QTableWidgetItem()
                item.setText(str(query.value(i)))
                self.ringConsolidation.tableWidget.setItem(row, i, item)
            row += 1

    def getRowId(self, idRingConsol):
        query = QSqlQuery()
        query.exec_('SELECT ROWID, * FROM tRingConsolidation WHERE idRingConsol = %d' % int(idRingConsol))
        query.next()
        rowId = query.value(0)
        return rowId

    def getRowCount(self):
        query = QSqlQuery()
        query.exec_('SELECT COUNT(*) FROM tRingConsolidation')
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
        self.ui = Ui_addRingConsolidation()
        self.ui.setupUi(self.qdialog)
        self.qdialog.show()

    def calcVolume(self, diameter, thick):
        volume = 0.25 * pi * (float(diameter))**2 * float(thick)
        return round(volume, 3)

    def currentTime(self):
        return datetime.date.today()

    def setColTableWidget(self):
        self.ringConsolidation.tableWidget.setColumnWidth(0, 80)
        self.ringConsolidation.tableWidget.setColumnWidth(1, 90)
        self.ringConsolidation.tableWidget.setColumnWidth(2, 70)
        self.ringConsolidation.tableWidget.setColumnWidth(3, 70)
        self.ringConsolidation.tableWidget.setColumnWidth(4, 90)
        self.ringConsolidation.tableWidget.horizontalHeader().setStretchLastSection(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = RingConsolidation()
    main.show()

    app.exec_()
