# import sys
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
#
# from PyQt5.QtSql import *
#
#
# def connectDB():
#     db = QSqlDatabase.addDatabase('QSQLITE')
#     db.setDatabaseName('testdb')
#     if db.open():
#         print('koneksi berhasil')
#         print(db.isOpen())
#     else:
#         print('error')
#
# connectDB()
#
#
# querry = QSqlQuery()
# sql = '''
#         CREATE TABLE phonebook (
#             id INTEGER NOT NULL PRIMARY KEY,
#             nama VARCHAR(25),
#             nohp VARCHAR(15)
#         )
#
#     '''
#
# querry.exec_(sql)
#
#
#
# # querry = QSqlQuery()
#
# # sql = '''
# #         INSERT INTO phonebook VALUES (4, 'Dedi Ghani', '08123456784')
# #     '''
#
#
# # sql = '''
# #         UPDATE phonebook
# #         SET nohp = '0123456789'
# #         WHERE id = 1
# # '''
#
# # querry.exec_(sql)
#
#
# def loadAllData():
#     querry = QSqlQuery()
#     ID, NAMA, NOHP = range(3)
#
#     querry.exec_('SELECT * FROM phonebook')
#     while querry.next():
#         for i in range(3):
#             id = querry.value(ID)
#             nama = querry.value(NAMA)
#             nohp = querry.value(NOHP)
#
#         print('%d\t%s\t%s' % (id, nama, nohp))
#
# loadAllData()

import sys

from PyQt5.QtWidgets import QApplication

from MainForm import *

if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainForm = MainForm()
    mainForm.show()

    app.exec_()
