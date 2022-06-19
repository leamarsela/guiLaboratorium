import sys
import datetime

from PycnometerUi import *
from addPycnometerUi import *

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *

class Pycnometer(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.pycno = Ui_DBPycnometer()
        self.pycno.setupUi(self)
        self.connectDb()
        self.loadPycnometer()

        self.pycno.pushButtonAdd.clicked.connect(self.pushButtonAddClicked)
        self.pycno.pushButtonUpdate.clicked.connect(self.pushButtonUpdateClicked)
        self.pycno.pushButtonDelete.clicked.connect(self.pushButtonDeleteClicked)

    def pushButtonAddClicked(self):
        self.setAdd()

        if self.qdialog.exec_() == QDialog.Accepted:
            id = self.getRowCount() + 1
            pycnoId = self.ui.lineEditRingId.text()
            pycnoWeight = self.ui.lineEditWeightRing.text()
            pycnoValM = self.ui.lineEditDiameterRing.text()
            pycnoValN = self.ui.lineEditThickRing.text()
            currentTime = datetime.datetime.now()

            query = QSqlQuery()
            query.exec_(
                "INSERT INTO tPycnometer VALUES (%d, '%s', '%s', '%s', '%s', '%s')" %
                (
                id,
                pycnoId,
                pycnoWeight,
                pycnoValM,
                pycnoValN,
                currentTime
                )
            )
            self.loadPycnometer()

    def pushButtonUpdateClicked(self):
        self.setAdd()

        pycnoId = self.pycno.tableWidget.item(self.pycno.tableWidget.currentRow(), 0).text()
        pycnoWeight = self.pycno.tableWidget.item(self.pycno.tableWidget.currentRow(), 1).text()
        pycnoValM = self.pycno.tableWidget.item(self.pycno.tableWidget.currentRow(), 2).text()
        pycnoValN = self.pycno.tableWidget.item(self.pycno.tableWidget.currentRow(), 3).text()

        idxPycno = self.pycno.tableWidget.currentRow() + 1
        self.ui.lineEditRingId.setText(pycnoId)
        self.ui.lineEditWeightRing.setText(pycnoWeight)
        self.ui.lineEditDiameterRing.setText(pycnoValM)
        self.ui.lineEditThickRing.setText(pycnoValN)
        currentTime = datetime.datetime.now()

        if self.qdialog.exec_() == QDialog.Accepted:
            query = QSqlQuery()
            query.exec_(
                '''
                    UPDATE tPycnometer
                    SET idPycno = '%s', weightPycno = '%s', valMPycno = '%s', valNPycno = '%s', datePycno = '%s'
                    WHERE idxPycno = %d
                ''' %
                (
                self.ui.lineEditRingId.text(),
                self.ui.lineEditWeightRing.text(),
                self.ui.lineEditDiameterRing.text(),
                self.ui.lineEditThickRing.text(),
                currentTime,
                idxPycno
                )
            )
            self.loadPycnometer()

    def pushButtonDeleteClicked(self):
        idxPycno = self.pycno.tableWidget.currentRow() + 1
        query = QSqlQuery()
        query.exec_(
            'DELETE FROM tPycnometer WHERE idxPycno = %d' % idxPycno
        )
        self.loadPycnometer()

    def loadPycnometer(self):
        self.pycno.tableWidget.clear()
        self.pycno.tableWidget.setRowCount(self.getRowCount())
        columnHeaders = ['No. Pycno', 'Weight (gr)', 'valM (-)', 'valN (-)', 'Date (-)']
        numberColumn = len(columnHeaders)
        self.pycno.tableWidget.setColumnCount(numberColumn)
        self.pycno.tableWidget.setHorizontalHeaderLabels(columnHeaders)

        query = QSqlQuery()
        row = 0
        query.exec_('SELECT * FROM tPycnometer')
        while query.next():
            for i in range(numberColumn):
                item = QTableWidgetItem()
                item.setText(str(query.value(i + 1)))
                self.pycno.tableWidget.setItem(row, i, item)
            row += 1

    def getRowCount(self):
        query = QSqlQuery()
        query.exec_('SELECT COUNT(*) FROM tPycnometer')
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
        self.ui = Ui_addPycnometer()
        self.ui.setupUi(self.qdialog)
        self.qdialog.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = Pycnometer()
    main.show()

    app.exec_()
