import sys

from PyQt5.QtSql import *


def createTableProject():
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('testdb')
    if db.open():
        print('koneksi berhasil')
        print(db.isOpen())
    else:
        print('error')

    query = QSqlQuery()

    sql = '''
            CREATE TABLE tableProject (
                idProject INTEGER NOT NULL PRIMARY KEY,
                idProjectNumber VARCHAR(10),
                clientProject VARCHAR(25),
                projectName VARCHAR(50)
            )
        '''

    query.exec_(sql)


createTableProject()
