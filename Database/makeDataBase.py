import sys

from PyQt5.QtSql import *

def createDataBase():
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('dbLab')
    if db.open():
        print('success')
    else:
        print('error')

    query = QSqlQuery()

    sqlContainer = '''
            CREATE TABLE tContainer (
                idxContainer INTEGER NOT NULL PRIMARY KEY,
                idContainer INTEGER,
                weightContainer REAL,
                dateContainer NUMERIC
            )
    '''

    sqlRingGamma = '''
        CREATE TABLE tRingGamma (
            idxRingGamma INTEGER NOT NULL PRIMARY KEY,
            idRingGamma INTEGER,
            weightRingGamma REAL,
            diameterRingGamma REAL,
            thicknessRingGamma REAL,
            volumeRingGamma REAL,
            dateRingGamma NUMERIC
        )
    '''

    sqlRingConsolidation = '''
        CREATE TABLE tRingConsolidation (
            idxRingConsolidation INTEGER NOT NULL PRIMARY KEY,
            idRingConsol INTEGER,
            weightRingConsol REAL,
            diameterRingConsol REAL,
            thicknessRingConsol REAL,
            volumeRingConsol REAL,
            dateRingConsol NUMERIC
        )
    '''


    listTable = [
        sqlContainer,
        sqlRingGamma,
        sqlRingConsolidation
    ]

    for sql in listTable:
        query.exec_(sql)



createDataBase()
