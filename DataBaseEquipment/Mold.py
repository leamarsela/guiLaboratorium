import sys
import datetime
from math import pi

from MoldUi import *
from addMoldUi import *

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *

class Mold(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.mold = Ui_DBMold()
        self.mold.setupUi(self)
        self.connectDb()
        self.loadMold()

        self.mold.pushButtonAdd.clicked.connect(self.pushButtonAddClicked)
        self.mold.pushButtonUpdate.clicked.connect(self.pushButtonEditClicked)
        self.mold.pushButtonDelete.clicked.connect(self.pushButtonDeleteClicked)

    def pushButtonAddClicked(self):
        self.setAdd()

        if self.qdialog.exec_() == QDialog.Accepted:
            moldId = self.ui.lineEditRingId.text()
            moldWeight = self.ui.lineEditWeightRing.text()
            moldDiameter = self.ui.lineEditDiameterRing.text()
            moldThick = self.ui.lineEditThickRing.text()
            moldVolume = self.calcVolume(moldDiameter, moldThick)
            currentTime = self.currentTime()
            query = QSqlQuery()
            query.prepare(
                "INSERT INTO tMold (ROWID, idMold, weightMold, diameterMold, thicknessMold, volumeMold, dateMold)"
                "VALUES (?, ?, ?, ?, ?, ?, ?)")

            query.bindValue(0, None)
            query.bindValue(1, moldId)
            query.bindValue(2, moldWeight)
            query.bindValue(3, moldDiameter)
            query.bindValue(4, moldThick)
            query.bindValue(5, moldVolume)
            query.bindValue(6, str(currentTime))
            query.exec_()
            self.loadMold()

    def pushButtonEditClicked(self):
        self.setAdd()

        moldId = self.mold.tableWidget.item(self.mold.tableWidget.currentRow(), 0).text()
        rowId = self.getRowId(moldId)
        moldWeight = self.mold.tableWidget.item(self.mold.tableWidget.currentRow(), 1).text()
        moldDiameter = self.mold.tableWidget.item(self.mold.tableWidget.currentRow(), 2).text()
        moldThick = self.mold.tableWidget.item(self.mold.tableWidget.currentRow(), 3).text()

        self.ui.lineEditRingId.setText(moldId)
        self.ui.lineEditWeightRing.setText(moldWeight)
        self.ui.lineEditDiameterRing.setText(moldDiameter)
        self.ui.lineEditThickRing.setText(moldThick)

        self.ui.lineEditWeightRing.textChanged.connect(lambda x: float(moldWeight))
        self.ui.lineEditDiameterRing.textChanged.connect(lambda x: float(moldDiameter))
        self.ui.lineEditThickRing.textChanged.connect(lambda x: float(moldThick))

        if self.qdialog.exec_() == QDialog.Accepted:
            moldWeight =  self.ui.lineEditWeightRing.text()
            moldDiameter = self.ui.lineEditDiameterRing.text()
            moldThick =  self.ui.lineEditThickRing.text()
            volume = self.calcVolume(moldDiameter, moldThick)
            currentTime = self.currentTime()

            query = QSqlQuery()
            query.exec(
                '''
                    UPDATE tMold
                    SET idMold = %d, weightMold = '%s', diameterMold = '%s', thicknessMold = '%s', volumeMold = '%s', dateMold = '%s'
                    WHERE ROWID = %d
                ''' %
                (
                int(moldId),
                moldWeight,
                moldDiameter,
                moldThick,
                volume,
                currentTime,
                rowId
                )
            )
            self.loadMold()

    def pushButtonDeleteClicked(self):
        valIdMold = self.mold.tableWidget.item(self.mold.tableWidget.currentRow(), 0).text()
        rowId = self.getRowId(valIdMold)
        query = QSqlQuery()
        query.exec_(
            'DELETE FROM tMold WHERE ROWID = %d' % rowId
        )
        self.loadMold()

    def loadMold(self):
        self.mold.tableWidget.clear()
        self.mold.tableWidget.setRowCount(self.getRowCount())
        columnHeaders = ['No. Mold', 'Weight (gr)', 'd (mm)', 't (mm)', 'V(mm^3)', 'Date']
        numberColumn = len(columnHeaders)
        self.mold.tableWidget.setColumnCount(numberColumn)
        self.mold.tableWidget.setHorizontalHeaderLabels(columnHeaders)
        self.setColTableWidget()

        query = QSqlQuery()
        row = 0
        query.exec_('VACUUM')
        query.exec_('SELECT * FROM tMold')
        while query.next():
            for i in range(numberColumn):
                item = QTableWidgetItem()
                item.setText(str(query.value(i)))
                self.mold.tableWidget.setItem(row, i, item)
            row += 1

    def getRowId(self, idMold):
        query = QSqlQuery()
        query.exec_('SELECT ROWID, * FROM tMold WHERE idMold = %d' % int(idMold))
        query.next()
        rowId = query.value(0)
        return rowId

    def getRowCount(self):
        query = QSqlQuery()
        query.exec_('SELECT COUNT(*) FROM tMold')
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
        self.ui = Ui_addMold()
        self.ui.setupUi(self.qdialog)
        self.qdialog.show()

    def calcVolume(self, diameter, thick):
        volume = 0.25 * pi * (float(diameter))**2 * float(thick)
        return round(volume, 3)

    def setColTableWidget(self):
        self.mold.tableWidget.setColumnWidth(0, 80)
        self.mold.tableWidget.setColumnWidth(1, 90)
        self.mold.tableWidget.setColumnWidth(2, 70)
        self.mold.tableWidget.setColumnWidth(3, 70)
        self.mold.tableWidget.setColumnWidth(4, 90)
        self.mold.tableWidget.horizontalHeader().setStretchLastSection(True)

    def currentTime(self):
        return datetime.date.today()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = Mold()
    main.show()

    app.exec_()
