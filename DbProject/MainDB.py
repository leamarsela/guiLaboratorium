import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *

from DbProject import *

class MainDB(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.loadData()


    def setupUi(self):
        self.resize(750, 300)
        self.move(500, 500)
        self.setWindowTitle('Daftar Project')

        self.table = QTableWidget()

        self.addButton = QPushButton('Tambah')
        self.editButton = QPushButton('Ubah')
        self.deleteButton = QPushButton('Hapus')
        self.closeButton = QPushButton('Close')

        hbox = QHBoxLayout()
        hbox.addWidget(self.addButton)
        hbox.addWidget(self.editButton)
        hbox.addWidget(self.deleteButton)
        hbox.addWidget(self.closeButton)
        hbox.addStretch()

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addLayout(hbox)
        self.setLayout(layout)

        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('DbProject/testdb')
        if db.open():
            print(db.isOpen())
        else:
            print('error')
            sys.exit(1)

        self.addButton.clicked.connect(self.addButtonClick)
        self.editButton.clicked.connect(self.editButtonClick)
        self.deleteButton.clicked.connect(self.deleteButtonClick)
        self.closeButton.clicked.connect(self.closeButtonClick)


    def loadData(self):
        self.table.clear()
        self.table.setRowCount(self.getRowCount())
        columnHeaders = ['id', 'PROJECT NUMBER', 'CLIENT', 'PROJECT']
        numberColumn = len(columnHeaders)
        self.table.setColumnCount(numberColumn)
        self.table.setHorizontalHeaderLabels(columnHeaders)

        query = QSqlQuery()
        ID, IDPROJECT, CLIENT, PROJECT = range(numberColumn)
        row = 0
        query.exec_('SELECT * FROM tableProject')
        while query.next():
            for i in range(numberColumn):
                item = QTableWidgetItem()
                item.setText(str(query.value(i)))
                self.table.setItem(row, i, item)
            row += 1



    def getRowCount(self):
        query = QSqlQuery()
        query.exec_('SELECT COUNT(*) FROM tableProject')
        query.next()
        rowCount = query.value(0)
        return rowCount


    def addButtonClick(self):
        self.dbProject = DbProject()
        self.mode = 0

        if self.dbProject.exec_() == QDialog.Accepted:
            id = self.getRowCount() + 1
            query = QSqlQuery()
            query.exec_(
                "INSERT INTO tableProject VALUES(%d, '%s', '%s', '%s')" %
                (id, self.dbProject.projectNumberLineEdit.text(),
                self.dbProject.clientLineEdit.text(),
                self.dbProject.projectLinetEdit.text())
            )
            self.loadData()


    def editButtonClick(self):
        self.dbProject = DbProject()
        self.mode = 1
        self.dbProject.projectNumberLineEdit.setText(
            self.table.item(self.table.currentRow(), 1).text()
        )
        self.dbProject.clientLineEdit.setText(
            self.table.item(self.table.currentRow(), 2).text()
        )
        self.dbProject.projectLinetEdit.setText(
            self.table.item(self.table.currentRow(), 2).text()
        )

        if self.dbProject.exec_() == QDialog.Accepted:
            id = int(self.table.item(self.table.currentRow(), 0).text())
            query = QSqlQuery()
            query.exec_(
                '''
                    UPDATE tableProject
                    SET idProjectNumber = '%s', clientProject = '%s',  projectName = '%s'
                    WHERE idProject = %d
                ''' %
                (self.dbProject.projectNumberLineEdit.text(),
                self.dbProject.clientLineEdit.text(),
                self.dbProject.projectLinetEdit.text(), id))
            self.loadData()


    def deleteButtonClick(self):
        id = int(self.table.item(self.table.currentRow(), 0).text())
        query = QSqlQuery()
        query.exec_('DELETE FROM tableProject WHERE id = %d' % id)
        self.loadData()


    def closeButtonClick(self):
        self.close()





























    def hanyapass(self):
        pass
