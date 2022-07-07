import sys
import datetime

from ProjectUi import *
from addProjectUi import *

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *

class Project(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.project = Ui_DBProject()
        self.project.setupUi(self)
        self.connectDb()
        self.loadDataProject()

        self.project.pushButtonAdd.clicked.connect(self.pushButtonAddClicked)
        self.project.pushButtonUpdate.clicked.connect(self.pushButtonEditClicked)
        self.project.pushButtonDelete.clicked.connect(self.pushButtonDeleteClicked)

    def pushButtonAddClicked(self):
        self.setAdd()

        if self.qdialog.exec_() == QDialog.Accepted:
            idNumProject = self.ui.lineEditProjectId.text()
            clientId = self.ui.lineEditClientId.text()
            projectName = self.ui.lineEditProjectName.text()
            currentTime = self.currentTime()
            query = QSqlQuery()
            query.prepare(
                    "INSERT INTO tProject (ROWID, idNumProject, idClient, idProject, dateProject)"
                    "VALUES (?, ?, ?, ?, ?)"
            )
            query.bindValue(0, None)
            query.bindValue(1, idNumProject)
            query.bindValue(2, clientId)
            query.bindValue(3, projectName)
            query.bindValue(4, str(currentTime))
            query.exec_()
            self.loadDataProject()


    def pushButtonEditClicked(self):
        self.setAdd()

        idNumProject = self.project.tableWidget.item(self.project.tableWidget.currentRow(), 0).text()
        rowId = self.getRowId(idNumProject)
        clientId = self.project.tableWidget.item(self.project.tableWidget.currentRow(), 1).text()
        projectName = self.project.tableWidget.item(self.project.tableWidget.currentRow(), 2).text()

        self.ui.lineEditProjectId.setText(idNumProject)
        self.ui.lineEditClientId.setText(clientId)
        self.ui.lineEditProjectName.setText(projectName)

        self.ui.lineEditClientId.textChanged.connect(lambda x: clientId)
        self.ui.lineEditProjectName.textChanged.connect(lambda x: projectName)

        if self.qdialog.exec_() == QDialog.Accepted:
            clientId = self.ui.lineEditClientId.text()
            projectName = self.ui.lineEditProjectName.text()
            currentTime = self.currentTime()
            query = QSqlQuery()
            query.exec_(
                '''
                    UPDATE tProject
                    SET idNumProject = '%s', idClient = '%s', idProject = '%s', dateProject = '%s'
                    WHERE ROWID = %d
                ''' %
                (
                idNumProject,
                clientId,
                projectName,
                str(currentTime),
                rowId
                )
            )
            self.loadDataProject()

    def pushButtonDeleteClicked(self):
        valIdNumProject = self.project.tableWidget.item(self.project.tableWidget.currentRow(), 0).text()
        rowId = self.getRowId(valIdNumProject)
        query = QSqlQuery()
        query.exec_(
            'DELETE FROM tProject WHERE ROWID = %d' % rowId
        )
        self.loadDataProject()

    def setAdd(self):
        self.qdialog = QtWidgets.QDialog()
        self.ui = Ui_addProject()
        self.ui.setupUi(self.qdialog)
        self.qdialog.show()

    def loadDataProject(self):
        self.project.tableWidget.clear()
        self.project.tableWidget.setRowCount(self.getRowCount())
        columnHeaders = ['ID Project', 'Client ID', 'Project Name', 'Date']
        numberColumn = len(columnHeaders)
        self.project.tableWidget.setColumnCount(numberColumn)
        self.project.tableWidget.setHorizontalHeaderLabels(columnHeaders)

        query = QSqlQuery()
        row = 0
        query.exec_('VACUUM')
        query.exec_('SELECT * FROM tProject')
        while query.next():
            for i in range(numberColumn):
                item = QTableWidgetItem()
                item.setText(str(query.value(i)))
                self.project.tableWidget.setItem(row, i, item)
            row += 1

    def getRowId(self, idNumProject):
        query = QSqlQuery()
        query.exec_('SELECT ROWID, * FROM tProject WHERE idNumProject = "%s"' % idNumProject)
        query.next()
        rowId = query.value(0)
        return rowId

    def getRowCount(self):
        query = QSqlQuery()
        query.exec_('SELECT COUNT(*) FROM tProject')
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

    def currentTime(self):
        return datetime.date.today()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = Project()
    main.show()

    app.exec_()
