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
        self.qdialog = QtWidgets.QDialog()
        self.ui = Ui_addRingConsolidation()
        self.ui.setupUi(self.qdialog)
        self.qdialog.show()

        if self.qdialog.exec() == QDialog.Accepted:
            id = self.getRowCount() + 1
            ringId = self.ui.lineEditRingId.text()
            ringWeight = self.ui.lineEditWeightRing.text()
            ringDiameter = self.ui.lineEditDiameterRing.text()
            ringThick = self.ui.lineEditThickRing.text()
            ringVolume = self.calcVolume(ringDiameter, ringThick)
            currentTime = datetime.datetime.now()
            query = QSqlQuery()
            query.exec_(
                "INSERT INTO tRingConsolidation VALUES (%d, '%s', '%s', '%s', '%s', '%s', '%s')" %
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
            self.loadRingConsol()

    def pushButtonEditClicked(self):
        self.qdialog = QtWidgets.QDialog()
        self.ui = Ui_addRingConsolidation()
        self.ui.setupUi(self.qdialog)
        self.qdialog.show()

        ringId = self.ringConsolidation.tableWidget.item(self.ringConsolidation.tableWidget.currentRow(), 0).text()
        ringWeight = self.ringConsolidation.tableWidget.item(self.ringConsolidation.tableWidget.currentRow(), 1).text()
        ringDiameter = self.ringConsolidation.tableWidget.item(self.ringConsolidation.tableWidget.currentRow(), 2).text()
        ringThick = self.ringConsolidation.tableWidget.item(self.ringConsolidation.tableWidget.currentRow(), 3).text()

        idxRingConsolidation = self.ringConsolidation.tableWidget.currentRow() + 1
        self.ui.lineEditRingId.setText(ringId)
        self.ui.lineEditWeightRing.setText(ringWeight)
        self.ui.lineEditDiameterRing.setText(ringDiameter)
        self.ui.lineEditThickRing.setText(ringThick)
        volume = self.calcVolume(ringDiameter, ringThick)
        currentTime = datetime.datetime.now()

        if self.qdialog.exec_() == QDialog.Accepted:
            query = QSqlQuery()
            query.exec_(
                '''
                    UPDATE tRingConsolidation
                    SET idRingConsol = %d, weightRingConsol = '%s', diameterRingConsol = '%s', thicknessRingConsol = '%s', volumeRingConsol = '%s', dateRingConsol = '%s'
                    WHERE idxRingConsolidation = %d
                ''' %
                (
                int(self.ui.lineEditRingId.text()),
                self.ui.lineEditWeightRing.text(),
                self.ui.lineEditDiameterRing.text(),
                self.ui.lineEditThickRing.text(),
                volume,
                currentTime,
                idxRingConsolidation
                )
            )
            self.loadRingConsol()

    def pushButtonDeleteClicked(self):
        idxRingConsolidation = self.ringConsolidation.tableWidget.currentRow() + 1
        query = QSqlQuery()
        query.exec_(
            'DELETE FROM tRingConsolidation WHERE idxRingConsolidation = %d' % idxRingConsolidation
        )
        self.loadRingConsol()

    def loadRingConsol(self):
        self.ringConsolidation.tableWidget.clear()
        self.ringConsolidation.tableWidget.setRowCount(self.getRowCount())
        columnHeaders = ['No. Ring', 'Weight (gr)', 'd (mm)', 't (mm)', 'V(mm^3)', 'Date']
        numberColumn = len(columnHeaders)
        self.ringConsolidation.tableWidget.setColumnCount(numberColumn)
        self.ringConsolidation.tableWidget.setHorizontalHeaderLabels(columnHeaders)

        query = QSqlQuery()
        row = 0
        query.exec_('SELECT * FROM tRingConsolidation')
        while query.next():
            for i in range(numberColumn):
                item = QTableWidgetItem()
                item.setText(str(query.value(i + 1)))
                self.ringConsolidation.tableWidget.setItem(row, i, item)
            row += 1

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

    def calcVolume(self, diameter, thick):
        volume = 0.25 * pi * (float(diameter))**2 * float(thick)
        return volume


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = RingConsolidation()
    main.show()

    app.exec_()
