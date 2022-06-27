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
                idContainer INTEGER,
                weightContainer REAL,
                dateContainer NUMERIC
            )
    '''

    sqlRingGamma = '''
        CREATE TABLE tRingGamma (
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
            idRingConsol INTEGER,
            weightRingConsol REAL,
            diameterRingConsol REAL,
            thicknessRingConsol REAL,
            volumeRingConsol REAL,
            dateRingConsol NUMERIC
        )
    '''

    sqlMold = '''
        CREATE TABLE tMold (
            idMold INTEGER,
            weightMold REAL,
            diameterMold REAL,
            thicknessMold REAL,
            volumeMold REAL,
            dateMold NUMERIC
        )
    '''

    sqlCbr = '''
        CREATE TABLE tCbr (
            idCbr INTEGER,
            weightCbr REAL,
            diameterCbr REAL,
            thicknessCbr REAL,
            volumeCbr REAL,
            dateCbr NUMERIC
        )
    '''

    sqlPycnometer = '''
        CREATE TABLE tPycnometer (
            idxPycno INTEGER NOT NULL PRIMARY KEY,
            idPycno VARCHAR(4),
            weightPycno REAL,
            valMPycno REAL,
            valNPycno REAL,
            datePycno NUMERIC
        )
    '''

    sqlProvingRing = '''
        CREATE TABLE tProvingRing (
            idxProving INTEGER NOT NULL PRIMARY KEY,
            idProving VARCHAR(5),
            valCalibration REAL,
            dateProvingRing NUMERIC
        )
    '''

    sqlProject = '''
        CREATE TABLE tProject (
            idxProject INTEGER NOT NULL PRIMARY KEY,
            idNumProject VARCHAR(5),
            idClient VARCHAR(50),
            idProject VARCHAR(50),
            dateProject NUMERIC
        )
    '''



    listTable = [
        sqlContainer,
        sqlRingGamma,
        sqlRingConsolidation,
        sqlMold,
        sqlCbr,
        sqlPycnometer,
        sqlProvingRing,
        sqlProject
    ]

    for sql in listTable:
        query.exec_(sql)



createDataBase()
