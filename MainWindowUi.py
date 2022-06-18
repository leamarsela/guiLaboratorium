# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuDatabase_Equipment = QtWidgets.QMenu(self.menuFile)
        self.menuDatabase_Equipment.setObjectName("menuDatabase_Equipment")
        self.menuContainer = QtWidgets.QMenu(self.menuDatabase_Equipment)
        self.menuContainer.setObjectName("menuContainer")
        self.menuRing_Gamma = QtWidgets.QMenu(self.menuDatabase_Equipment)
        self.menuRing_Gamma.setObjectName("menuRing_Gamma")
        self.menuPycnometer = QtWidgets.QMenu(self.menuDatabase_Equipment)
        self.menuPycnometer.setObjectName("menuPycnometer")
        self.menuMold = QtWidgets.QMenu(self.menuDatabase_Equipment)
        self.menuMold.setObjectName("menuMold")
        self.menuCBR = QtWidgets.QMenu(self.menuDatabase_Equipment)
        self.menuCBR.setObjectName("menuCBR")
        self.menuRing_Consolidation = QtWidgets.QMenu(self.menuDatabase_Equipment)
        self.menuRing_Consolidation.setObjectName("menuRing_Consolidation")
        self.menuProving_Ring = QtWidgets.QMenu(self.menuDatabase_Equipment)
        self.menuProving_Ring.setObjectName("menuProving_Ring")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdd_New_Container = QtWidgets.QAction(MainWindow)
        self.actionAdd_New_Container.setObjectName("actionAdd_New_Container")
        self.actionShow_Data_Container = QtWidgets.QAction(MainWindow)
        self.actionShow_Data_Container.setObjectName("actionShow_Data_Container")
        self.actionAdd_New_RingGamma = QtWidgets.QAction(MainWindow)
        self.actionAdd_New_RingGamma.setObjectName("actionAdd_New_RingGamma")
        self.actionShow_Data_RingGamma = QtWidgets.QAction(MainWindow)
        self.actionShow_Data_RingGamma.setObjectName("actionShow_Data_RingGamma")
        self.actionAdd_New_Pycnometer = QtWidgets.QAction(MainWindow)
        self.actionAdd_New_Pycnometer.setObjectName("actionAdd_New_Pycnometer")
        self.actionShow_Data_Pycnometer = QtWidgets.QAction(MainWindow)
        self.actionShow_Data_Pycnometer.setObjectName("actionShow_Data_Pycnometer")
        self.actionAdd_New_Mold = QtWidgets.QAction(MainWindow)
        self.actionAdd_New_Mold.setObjectName("actionAdd_New_Mold")
        self.actionShow_Data_Mold = QtWidgets.QAction(MainWindow)
        self.actionShow_Data_Mold.setObjectName("actionShow_Data_Mold")
        self.actionAdd_New_Cbr = QtWidgets.QAction(MainWindow)
        self.actionAdd_New_Cbr.setObjectName("actionAdd_New_Cbr")
        self.actionShow_Data_Cbr = QtWidgets.QAction(MainWindow)
        self.actionShow_Data_Cbr.setObjectName("actionShow_Data_Cbr")
        self.actionAdd_New_Consolidation = QtWidgets.QAction(MainWindow)
        self.actionAdd_New_Consolidation.setObjectName("actionAdd_New_Consolidation")
        self.actionShow_Data_Consolidation = QtWidgets.QAction(MainWindow)
        self.actionShow_Data_Consolidation.setObjectName("actionShow_Data_Consolidation")
        self.actionAdd_New_ProvingRing = QtWidgets.QAction(MainWindow)
        self.actionAdd_New_ProvingRing.setObjectName("actionAdd_New_ProvingRing")
        self.actionShow_Data_ProvingRing = QtWidgets.QAction(MainWindow)
        self.actionShow_Data_ProvingRing.setObjectName("actionShow_Data_ProvingRing")
        self.menuContainer.addAction(self.actionShow_Data_Container)
        self.menuRing_Gamma.addAction(self.actionShow_Data_RingGamma)
        self.menuPycnometer.addAction(self.actionShow_Data_Pycnometer)
        self.menuMold.addAction(self.actionShow_Data_Mold)
        self.menuCBR.addAction(self.actionShow_Data_Cbr)
        self.menuRing_Consolidation.addAction(self.actionShow_Data_Consolidation)
        self.menuProving_Ring.addAction(self.actionShow_Data_ProvingRing)
        self.menuDatabase_Equipment.addAction(self.menuContainer.menuAction())
        self.menuDatabase_Equipment.addAction(self.menuRing_Gamma.menuAction())
        self.menuDatabase_Equipment.addAction(self.menuPycnometer.menuAction())
        self.menuDatabase_Equipment.addAction(self.menuMold.menuAction())
        self.menuDatabase_Equipment.addAction(self.menuCBR.menuAction())
        self.menuDatabase_Equipment.addAction(self.menuRing_Consolidation.menuAction())
        self.menuDatabase_Equipment.addAction(self.menuProving_Ring.menuAction())
        self.menuFile.addAction(self.menuDatabase_Equipment.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuDatabase_Equipment.setTitle(_translate("MainWindow", "Database Equipment"))
        self.menuContainer.setTitle(_translate("MainWindow", "Container"))
        self.menuRing_Gamma.setTitle(_translate("MainWindow", "Ring Gamma"))
        self.menuPycnometer.setTitle(_translate("MainWindow", "Pycnometer"))
        self.menuMold.setTitle(_translate("MainWindow", "Mold"))
        self.menuCBR.setTitle(_translate("MainWindow", "CBR"))
        self.menuRing_Consolidation.setTitle(_translate("MainWindow", "Ring Consolidation"))
        self.menuProving_Ring.setTitle(_translate("MainWindow", "Proving Ring"))
        self.actionAdd_New_Container.setText(_translate("MainWindow", "Add New"))
        self.actionShow_Data_Container.setText(_translate("MainWindow", "Show Data Container"))
        self.actionAdd_New_RingGamma.setText(_translate("MainWindow", "Add New"))
        self.actionShow_Data_RingGamma.setText(_translate("MainWindow", "Show Data Ring Gamma"))
        self.actionAdd_New_Pycnometer.setText(_translate("MainWindow", "Add New"))
        self.actionShow_Data_Pycnometer.setText(_translate("MainWindow", "Show Data Pycnometer"))
        self.actionAdd_New_Mold.setText(_translate("MainWindow", "Add New"))
        self.actionShow_Data_Mold.setText(_translate("MainWindow", "Show Data Mold"))
        self.actionAdd_New_Cbr.setText(_translate("MainWindow", "Add New"))
        self.actionShow_Data_Cbr.setText(_translate("MainWindow", "Show Data CBR"))
        self.actionAdd_New_Consolidation.setText(_translate("MainWindow", "Add New"))
        self.actionShow_Data_Consolidation.setText(_translate("MainWindow", "Show Data Ring Consolidation"))
        self.actionAdd_New_ProvingRing.setText(_translate("MainWindow", "Add New"))
        self.actionShow_Data_ProvingRing.setText(_translate("MainWindow", "Show Data Proving Ring"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())