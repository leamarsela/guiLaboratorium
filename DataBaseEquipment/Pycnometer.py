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
            pycnoId = self.ui.lineEditRingId.text()
            pycnoWeight = self.ui.lineEditWeightRing.text()
            pycnoValM = self.ui.lineEditDiameterRing.text()
            pycnoValN = self.ui.lineEditThickRing.text()
            currentTime = self.currentTime()
            query = QSqlQuery()
            query.prepare(
                    "INSERT INTO tPycnometer (ROWID, idPycno, weightPycno, valMPycno, valNPycno, datePycno)"
                    "VALUES (?, ?, ?, ?, ?, ?)"
            )
            query.bindValue(0, None)
            query.bindValue(1, pycnoId)
            query.bindValue(2, pycnoWeight)
            query.bindValue(3, pycnoValM)
            query.bindValue(4, pycnoValN)
            query.bindValue(5, str(currentTime))
            query.exec_()
            self.loadPycnometer()

    def pushButtonUpdateClicked(self):
        self.setAdd()

        pycnoId = self.pycno.tableWidget.item(self.pycno.tableWidget.currentRow(), 0).text()
        rowId = self.getRowId(pycnoId)
        pycnoWeight = self.pycno.tableWidget.item(self.pycno.tableWidget.currentRow(), 1).text()
        pycnoValM = self.pycno.tableWidget.item(self.pycno.tableWidget.currentRow(), 2).text()
        pycnoValN = self.pycno.tableWidget.item(self.pycno.tableWidget.currentRow(), 3).text()

        self.ui.lineEditRingId.setText(pycnoId)
        self.ui.lineEditWeightRing.setText(pycnoWeight)
        self.ui.lineEditDiameterRing.setText(pycnoValM)
        self.ui.lineEditThickRing.setText(pycnoValN)

        self.ui.lineEditWeightRing.textChanged.connect(lambda x: float(pycnoWeight))
        self.ui.lineEditDiameterRing.textChanged.connect(lambda x: float(pycnoValM))
        self.ui.lineEditThickRing.textChanged.connect(lambda x: float(pycnoValN))

        if self.qdialog.exec_() == QDialog.Accepted:
            pycnoId = self.ui.lineEditRingId.text()
            pycnoWeight = self.ui.lineEditWeightRing.text()
            pycnoValM = self.ui.lineEditDiameterRing.text()
            pycnoValN = self.ui.lineEditThickRing.text()
            currentTime = self.currentTime()
            query = QSqlQuery()
            query.exec_(
                '''
                    UPDATE tPycnometer
                    SET idPycno = '%s', weightPycno = '%s', valMPycno = '%s', valNPycno = '%s', datePycno = '%s'
                    WHERE ROWID = %d
                ''' %
                (
                pycnoId,
                pycnoWeight,
                pycnoValM,
                pycnoValN,
                currentTime,
                rowId
                )
            )
            self.loadPycnometer()

    def pushButtonDeleteClicked(self):
        valIdPycno = self.pycno.tableWidget.item(self.pycno.tableWidget.currentRow(), 0).text()
        rowId = self.getRowId(valIdPycno)
        query = QSqlQuery()
        query.exec_(
            'DELETE FROM tPycnometer WHERE ROWID = %d' % rowId
        )
        self.loadPycnometer()

    def loadPycnometer(self):
        self.pycno.tableWidget.clear()
        self.pycno.tableWidget.setRowCount(self.getRowCount())
        columnHeaders = ['No. Pycno', 'Weight (gr)', 'valM (-)', 'valN (-)', 'Date (-)']
        numberColumn = len(columnHeaders)
        self.pycno.tableWidget.setColumnCount(numberColumn)
        self.pycno.tableWidget.setHorizontalHeaderLabels(columnHeaders)
        self.setColTableWidget()

        query = QSqlQuery()
        row = 0
        query.exec_('VACUUM')
        query.exec_('SELECT * FROM tPycnometer')
        while query.next():
            for i in range(numberColumn):
                item = QTableWidgetItem()
                item.setText(str(query.value(i)))
                self.pycno.tableWidget.setItem(row, i, item)
            row += 1

    def getRowId(self, idPycno):
        query = QSqlQuery()
        query.exec_('SELECT ROWID, * from tPycnometer WHERE idPycno = %d' % int(idPycno))
        query.next()
        rowId = query.value(0)
        return rowId

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

    def currentTime(self):
        return datetime.date.today()

    def setColTableWidget(self):
        self.pycno.tableWidget.setColumnWidth(0, 80)
        self.pycno.tableWidget.setColumnWidth(1, 100)
        self.pycno.tableWidget.setColumnWidth(2, 80)
        self.pycno.tableWidget.setColumnWidth(3, 80)
        self.pycno.tableWidget.setColumnWidth(4, 80)
        self.pycno.tableWidget.horizontalHeader().setStretchLastSection(True)



if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = Pycnometer()
    main.show()

    app.exec_()
