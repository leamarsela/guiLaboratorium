import sys
import datetime

from ProvingRingUi import *
from addProvingRingUi import *

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *

class ProvingRing(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.provingRing = Ui_DBProvingRing()
        self.provingRing.setupUi(self)
        self.connectDb()
        self.loadProvingRing()

        self.provingRing.pushButtonAdd.clicked.connect(self.pushButtonAddClicked)
        self.provingRing.pushButtonUpdate.clicked.connect(self.pushButtonEditClicked)
        self.provingRing.pushButtonDelete.clicked.connect(self.pushButtonDeleteClicked)

    def pushButtonAddClicked(self):
        self.setAdd()

        if self.qdialog.exec_() == QDialog.Accepted:
            pRingId = self.ui.lineEditRingId.text()
            pRingCalibration = self.ui.lineEditWeightRing.text()
            currentTime =  self.currentTime()
            query = QSqlQuery()
            query.prepare(
                    "INSERT INTO tProvingRing (ROWID, idProving, valCalibration, dateProvingRing)"
                    "VALUES (?, ?, ?, ?)"
            )
            query.bindValue(0, None)
            query.bindValue(1, pRingId)
            query.bindValue(2, pRingCalibration)
            query.bindValue(3, str(currentTime))
            query.exec_()
            self.loadProvingRing()

    def pushButtonEditClicked(self):
        self.setAdd()

        pRingId = self.provingRing.tableWidget.item(self.provingRing.tableWidget.currentRow(), 0).text()
        rowId = self.getRowId(pRingId)
        pRingCalibration = self.provingRing.tableWidget.item(self.provingRing.tableWidget.currentRow(), 1).text()

        self.ui.lineEditRingId.setText(pRingId)
        self.ui.lineEditWeightRing.setText(pRingCalibration)

        self.ui.lineEditWeightRing.textChanged.connect(lambda x: float(pRingCalibration))

        if self.qdialog.exec_() == QDialog.Accepted:
            pRingId = self.ui.lineEditRingId.text()
            pRingCalibration = self.ui.lineEditWeightRing.text()
            currentTime = self.currentTime()
            query = QSqlQuery()
            query.exec_(
                '''
                    UPDATE tProvingRing
                    SET idProving = '%s', valCalibration = '%s', dateProvingRing = '%s'
                    WHERE ROWID = '%d'
                ''' %
                (
                int(pRingId),
                pRingCalibration,
                currentTime,
                rowId
                )
            )
            self.loadProvingRing()

    def pushButtonDeleteClicked(self):
        valIdProving = self.provingRing.tableWidget.item(self.provingRing.tableWidget.currentRow(), 0).text()
        rowId = self.getRowId(valIdProving)
        query = QSqlQuery()
        query.exec_(
            'DELETE FROM tProvingRing WHERE ROWID = %d' % rowId
        )
        self.loadProvingRing()

    def loadProvingRing(self):
        self.provingRing.tableWidget.clear()
        self.provingRing.tableWidget.setRowCount(self.getRowCount())
        columnHeaders = ['No. Proving Ring', 'Calibration (kg/div)', 'Date (-)']
        numberColumn = len(columnHeaders)
        self.provingRing.tableWidget.setColumnCount(numberColumn)
        self.provingRing.tableWidget.setHorizontalHeaderLabels(columnHeaders)
        self.setColTableWidget()

        query = QSqlQuery()
        row = 0
        query.exec_('VACUUM')
        query.exec_('SELECT * FROM tProvingRing')
        while query.next():
            for i in range(numberColumn):
                item = QTableWidgetItem()
                item.setText(str(query.value(i)))
                self.provingRing.tableWidget.setItem(row, i, item)
            row += 1

    def getRowId(self, idProving):
        query = QSqlQuery()
        query.exec_('SELECT ROWID, * FROM tProvingRing WHERE idProving = "%s"' % idProving)
        query.next()
        rowId = query.value(0)
        return rowId

    def getRowCount(self):
        query = QSqlQuery()
        query.exec_('SELECT COUNT(*) FROM tProvingRing')
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
        self.ui = Ui_addProvingRing()
        self.ui.setupUi(self.qdialog)
        self.qdialog.show()

    def setColTableWidget(self):
        self.provingRing.tableWidget.setColumnWidth(0, 150)
        self.provingRing.tableWidget.setColumnWidth(1, 150)
        self.provingRing.tableWidget.horizontalHeader().setStretchLastSection(True)

    def currentTime(self):
        return datetime.date.today()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = ProvingRing()
    main.show()

    app.exec_()
