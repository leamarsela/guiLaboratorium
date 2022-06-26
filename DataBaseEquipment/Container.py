import sys
import datetime

from ContainerUi import *
from addContainerUi import *

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *

class Container(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.container = Ui_DBContainer()
        self.container.setupUi(self)
        self.connectDb()
        self.loadDataContainer()


        self.container.pushButtonAdd.clicked.connect(self.pushButtonAddClicked)
        self.container.pushButtonUpdate.clicked.connect(self.pushButtonEditClicked)
        self.container.pushButtonDelete.clicked.connect(self.pushButtonDeleteClicked)


    def pushButtonAddClicked(self):
        self.setAdd()

        if self.qdialog.exec_() == QDialog.Accepted:
            containerId = self.ui.lineEditContainerId.text()
            containerWeight = self.ui.lineEditWeightContainer.text()
            currentTime = self.currentTime()
            query = QSqlQuery()
            query.prepare("INSERT INTO tContainer (ROWID, idContainer, weightContainer, dateContainer)"
                          "VALUES (?, ?, ?, ?)")

            query.bindValue(0, None)
            query.bindValue(1, containerId)
            query.bindValue(2, containerWeight)
            query.bindValue(3, str(currentTime))
            query.exec_()
            self.loadDataContainer()

    def pushButtonEditClicked(self):
        self.setAdd()

        containerId = self.container.tableWidget.item(self.container.tableWidget.currentRow(), 0).text()
        rowId = self.getRowId(containerId)
        containerWeight = self.container.tableWidget.item(self.container.tableWidget.currentRow(), 1).text()

        self.ui.lineEditContainerId.setText(containerId)
        self.ui.lineEditWeightContainer.setText(containerWeight)
        currentTime = self.currentTime()

        if self.qdialog.exec_() == QDialog.Accepted:
            query = QSqlQuery()
            query.exec_(
                '''
                    UPDATE tContainer
                    SET idContainer = %d, weightContainer = '%s', dateContainer = '%s'
                    WHERE ROWID = %d
                ''' %
                (
                    int(self.ui.lineEditContainerId.text()),
                    self.ui.lineEditWeightContainer.text(),
                    currentTime,
                    rowId
                )
            )
            self.loadDataContainer()

    def pushButtonDeleteClicked(self):
        valIdContainer = self.container.tableWidget.item(self.container.tableWidget.currentRow(), 0).text()
        rowId = self.getRowId(valIdContainer)
        query = QSqlQuery()
        query.exec_(
            'DELETE FROM tContainer WHERE ROWID = %d' % rowId
        )
        self.loadDataContainer()

    def loadDataContainer(self):
        self.container.tableWidget.clear()
        self.container.tableWidget.setRowCount(self.getRowCount())
        columnHeaders = ['No.Container', 'Weight Container (gr)', 'Date']
        numberColumn = len(columnHeaders)
        self.container.tableWidget.setColumnCount(numberColumn)
        self.container.tableWidget.setHorizontalHeaderLabels(columnHeaders)
        self.setColTableWidget()

        query = QSqlQuery()
        idContainer, weightContainer, dateContainer = range(3)
        row = 0
        query.exec_('VACUUM')
        query.exec_('SELECT * FROM tContainer')
        while query.next():
            for i in range(numberColumn):
                item = QTableWidgetItem()
                item.setText(str(query.value(i)))
                self.container.tableWidget.setItem(row, i, item)
            row += 1

    def getRowId(self, idContainer):
        query = QSqlQuery()
        query.exec_('SELECT ROWID, * FROM tContainer WHERE idContainer = %d' % int(idContainer))
        query.next()
        rowId = query.value(0)
        return rowId

    def getRowCount(self):
        query = QSqlQuery()
        query.exec_('SELECT COUNT(*) FROM tContainer')
        query.next()
        rowCount = query.value(0)
        return rowCount

    def connectDb(self):
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('./Database/dbLab')
        if self.db.open():
            print(self.db.isOpen())
        else:
            print('error')
            sys.exit(1)

    def setAdd(self):
        self.qdialog = QtWidgets.QDialog()
        self.ui = Ui_addContainer()
        self.ui.setupUi(self.qdialog)
        self.qdialog.show()

    def setColTableWidget(self):
        self.container.tableWidget.setColumnWidth(0, 95)
        self.container.tableWidget.setColumnWidth(1, 150)
        self.container.tableWidget.horizontalHeader().setStretchLastSection(True)

    def currentTime(self):
        return datetime.date.today()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = Container()
    main.show()

    app.exec_()
