import sys
from datetime import date

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
            idPycno VARCHAR(4),
            weightPycno REAL,
            valMPycno REAL,
            valNPycno REAL,
            datePycno NUMERIC
        )
    '''

    sqlProvingRing = '''
        CREATE TABLE tProvingRing (
            idProving VARCHAR(5),
            valCalibration REAL,
            dateProvingRing NUMERIC
        )
    '''

    sqlProject = '''
        CREATE TABLE tProject (
            projectId INTEGER PRIMARY KEY,
            idNumProject VARCHAR(5) NOT NULL,
            idClient VARCHAR(50),
            idProject VARCHAR(50),
            dateProject NUMERIC
        )
    '''

    sqlGroupTesting = '''
        CREATE TABLE tGroupTesting (
            groupTestingId INTEGER PRIMARY KEY,
            groupName VARCHAR(50) NOT NULL,
            dateGroupTesting NUMERIC
        )
    '''

    sqlListSample = '''
        CREATE TABLE tListSample (
            listSampleId INTEGER PRIMARY KEY,
            idArea VARCHAR(10) NOT NULL,
            idBorehole VARCHAR(10),
            depthFrom VARCHAR(5),
            depthTo VARCHAR(5),
            dateListSample NUMERIC,
            projectId INTEGER NOT NULL,
            groupTestingId INTEGER NOT NULL,
            FOREIGN KEY (projectId) REFERENCES tProject(projectId) ON UPDATE CASCADE ON DELETE CASCADE,
            FOREIGN KEY (groupTestingId) REFERENCES tGroupTesting(groupTestingId) ON UPDATE CASCADE ON DELETE CASCADE
        )
    '''

    sqlWaterContent = '''
        CREATE TABLE tWaterContent (
            idWaterContent INTEGER,
            idContainerFirst INTEGER,
            idContainerSecond INTEGER,
            idContainerThird INTEGER,
            idWetSoilContainerFirst REAL,
            idWetSoilContainerSecond REAL,
            idWetSoilContainerThird REAL,
            idDrySoilContainerFirst REAL,
            idDrySoilContainerSecond REAL,
            idDrySoilContainerThird REAL,
            dateWaterContent NUMERIC
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
        sqlProject,
        sqlListSample,
        sqlGroupTesting
    ]

    for sql in listTable:
        query.exec_(sql)


    groupNameList = [
        'atterbergLimit',
        'cbrSoaked',
        'cbrUnsoaked',
        'chlorideContent',
        'compation',
        'consolidation',
        'consolidationSwelling',
        'directShearRock',
        'directShearSoil',
        'emerson',
        'hydrometer',
        'losAngelesAbrasion',
        'organicContent',
        'permeabilityFallingHead',
        'permeabilityConstantHead',
        'phTest',
        'pointLoad',
        'propertiesRock',
        'sieveAnalysis',
        'slakeDurability',
        'spesificGravity',
        'sulphateContent',
        'tensile',
        'triaxialCd',
        'triaxialCu',
        'triaxialRock'
        'triaxialUu',
        'ucs',
        'ucsPoisson',
        'uct',
        'ultrasonic',
        'unitWeight',
        'waterContent'
    ]

    groupIdList = []
    dateGroupTestingList = []
    for i in range(len(groupNameList)-1):
        groupIdList.append(None)
        dateGroupTestingList.append(str(date.today()))


    query = QSqlQuery()

    query.prepare("INSERT INTO tGroupTesting VALUES (?, ?, ?)")

    query.addBindValue(groupIdList)
    query.addBindValue(groupNameList)
    query.addBindValue(dateGroupTestingList)

    if not query.execBatch():
        print(query.lastError())




createDataBase()
