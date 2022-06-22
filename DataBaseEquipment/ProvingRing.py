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
            id = self.getRowCount() + 1
            pRingId = self.ui.lineEditRingId.text()
            pRingCalibration = self.ui.lineEditWeightRing.text()
            currentTime =  datetime.datetime.now()
            query = QSqlQuery()
            query.exec_(
                "INSERT INTO tProvingRing VALUES (%d, '%s', '%s', '%s')" %
                (
                id,
                pRingId,
                pRingCalibration,
                currentTime
                )
            )
            self.loadProvingRing()

    def pushButtonEditClicked(self):
        self.setAdd()

        pRingId = self.provingRing.tableWidget.item(self.provingRing.tableWidget.currentRow(), 0).text()
        pRingCalibration = self.provingRing.tableWidget.item(self.provingRing.tableWidget.currentRow(), 1).text()

        indexProvingRIng = self.provingRing.tableWidget.currentRow() + 1
        self.ui.lineEditRingId.setText(pRingId)
        self.ui.lineEditWeightRing.setText(pRingCalibration)
        currentTime = datetime.datetime.now()

        if self.qdialog.exec_() == QDialog.Accepted:
            query = QSqlQuery()
            query.exec_(
                '''
                    UPDATE tProvingRing
                    SET idProving = '%s', valCalibration = '%s', dateProvingRing = '%s'
                    WHERE idxProving = '%d'
                ''' %
                (
                self.ui.lineEditRingId.text(),
                self.ui.lineEditWeightRing.text(),
                currentTime,
                indexProvingRIng
                )
            )
            self.loadProvingRing()

    def pushButtonDeleteClicked(self):
        idxProving = self.provingRing.tableWidget.currentRow() + 1
        query = QSqlQuery()
        query.exec_(
            'DELETE FROM tProvingRing WHERE idxProving = %d' % idxProving
        )
        self.loadProvingRing()

    def loadProvingRing(self):
        self.provingRing.tableWidget.clear()
        self.provingRing.tableWidget.setRowCount(self.getRowCount())
        columnHeaders = ['No. Proving Ring', 'Calibration (kg/div)', 'Date (-)']
        numberColumn = len(columnHeaders)
        self.provingRing.tableWidget.setColumnCount(numberColumn)
        self.provingRing.tableWidget.setHorizontalHeaderLabels(columnHeaders)

        query = QSqlQuery()
        row = 0
        query.exec_('SELECT * FROM tProvingRing')
        while query.next():
            for i in range(numberColumn):
                item = QTableWidgetItem()
                item.setText(str(query.value(i + 1)))
                self.provingRing.tableWidget.setItem(row, i, item)
            row += 1

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

    def getRowCount(self):
        query = QSqlQuery()
        query.exec_('SELECT COUNT(*) FROM tProvingRing')
        query.next()
        rowCount = query.value(0)
        return rowCount


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = ProvingRing()
    main.show()

    app.exec_()
