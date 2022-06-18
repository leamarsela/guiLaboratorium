import sys
import datetime


from ContainerUi import *
from AddContainer import *
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
        self.qdialog = QtWidgets.QDialog()
        self.ui = Ui_addContainer()
        self.ui.setupUi(self.qdialog)
        self.qdialog.show()

        if self.qdialog.exec_() == QDialog.Accepted:
            containerId = self.ui.lineEditContainerId.text()
            containerWeight = self.ui.lineEditWeightContainer.text()
            id = self.getRowCount() + 1
            currentTime = datetime.datetime.now()
            query = QSqlQuery()
            query.exec_(
                "INSERT INTO tContainer VALUES(%d, '%s', '%s', '%s')" %
                (
                id,
                containerId,
                containerWeight,
                currentTime
                )
            )
            self.loadDataContainer()

    def pushButtonEditClicked(self):
        self.qdialog = QtWidgets.QDialog()
        self.ui = Ui_addContainer()
        self.ui.setupUi(self.qdialog)
        self.qdialog.show()

        containerId = self.container.tableWidget.item(self.container.tableWidget.currentRow(), 0).text()
        containerWeight = self.container.tableWidget.item(self.container.tableWidget.currentRow(), 1).text()

        indexContainer = self.container.tableWidget.currentRow() + 1
        self.ui.lineEditContainerId.setText(containerId)
        self.ui.lineEditWeightContainer.setText(containerWeight)
        currentTime = datetime.datetime.now()

        if self.qdialog.exec_() == QDialog.Accepted:
            query = QSqlQuery()
            query.exec_(
                '''
                    UPDATE tContainer
                    SET idContainer = %d, weightContainer = '%s', dateContainer = '%s'
                    WHERE idxContainer = %d
                ''' %
                (
                    int(self.ui.lineEditContainerId.text()),
                    self.ui.lineEditWeightContainer.text(),
                    currentTime,
                    indexContainer
                )
            )
            self.loadDataContainer()

    def pushButtonDeleteClicked(self):
        idxContainer = self.container.tableWidget.currentRow() + 1
        query = QSqlQuery()
        query.exec_(
            'DELETE FROM tContainer WHERE idxContainer = %d' % idxContainer
        )
        self.loadDataContainer()

    def loadDataContainer(self):
        self.container.tableWidget.clear()
        self.container.tableWidget.setRowCount(self.getRowCount())
        columnHeaders = ['No.Container', 'Weight Container (gr)', 'Date']
        numberColumn = len(columnHeaders)
        self.container.tableWidget.setColumnCount(numberColumn)
        self.container.tableWidget.setHorizontalHeaderLabels(columnHeaders)

        query = QSqlQuery()
        idContainer, weightContainer, dateContainer = range(3)
        row = 0
        query.exec_('SELECT * FROM tContainer')
        while query.next():
            for i in range(numberColumn):
                item = QTableWidgetItem()
                item.setText(str(query.value(i + 1)))
                self.container.tableWidget.setItem(row, i, item)
            row += 1

    def getRowCount(self):
        query = QSqlQuery()
        query.exec_('SELECT COUNT(*) FROM tContainer')
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


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = Container()
    main.show()

    app.exec_()
