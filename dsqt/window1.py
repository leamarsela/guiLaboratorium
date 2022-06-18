# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\window1.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from table import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(664, 578)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 664, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuShow_Database_Equipment = QtWidgets.QMenu(self.menuFile)
        self.menuShow_Database_Equipment.setObjectName("menuShow_Database_Equipment")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuForm = QtWidgets.QMenu(self.menubar)
        self.menuForm.setObjectName("menuForm")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionNew_Project = QtWidgets.QAction(MainWindow)
        self.actionNew_Project.setObjectName("actionNew_Project")
        self.actionList_Project = QtWidgets.QAction(MainWindow)
        self.actionList_Project.setObjectName("actionList_Project")
        self.actionDatabase_Equipment = QtWidgets.QAction(MainWindow)
        self.actionDatabase_Equipment.setObjectName("actionDatabase_Equipment")
        self.actionEdit_Database_Equipment = QtWidgets.QAction(MainWindow)
        self.actionEdit_Database_Equipment.setObjectName("actionEdit_Database_Equipment")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionContainer = QtWidgets.QAction(MainWindow)
        self.actionContainer.setObjectName("actionContainer")
        self.actionRing_Gamma = QtWidgets.QAction(MainWindow)
        self.actionRing_Gamma.setObjectName("actionRing_Gamma")
        self.actionPycnometer = QtWidgets.QAction(MainWindow)
        self.actionPycnometer.setObjectName("actionPycnometer")
        self.actionMold = QtWidgets.QAction(MainWindow)
        self.actionMold.setObjectName("actionMold")
        self.actionCBR = QtWidgets.QAction(MainWindow)
        self.actionCBR.setObjectName("actionCBR")
        self.actionConsolidation = QtWidgets.QAction(MainWindow)
        self.actionConsolidation.setObjectName("actionConsolidation")
        self.actionExit_2 = QtWidgets.QAction(MainWindow)
        self.actionExit_2.setObjectName("actionExit_2")
        self.actionExit_3 = QtWidgets.QAction(MainWindow)
        self.actionExit_3.setObjectName("actionExit_3")
        self.actionNew_Form = QtWidgets.QAction(MainWindow)
        self.actionNew_Form.setObjectName("actionNew_Form")
        self.actionNew_Edit = QtWidgets.QAction(MainWindow)
        self.actionNew_Edit.setObjectName("actionNew_Edit")
        self.actionNew_Help = QtWidgets.QAction(MainWindow)
        self.actionNew_Help.setObjectName("actionNew_Help")
        self.menuShow_Database_Equipment.addAction(self.actionContainer)
        self.menuShow_Database_Equipment.addAction(self.actionRing_Gamma)
        self.menuShow_Database_Equipment.addAction(self.actionPycnometer)
        self.menuShow_Database_Equipment.addAction(self.actionMold)
        self.menuShow_Database_Equipment.addAction(self.actionCBR)
        self.menuShow_Database_Equipment.addAction(self.actionConsolidation)
        self.menuFile.addAction(self.actionNew_Project)
        self.menuFile.addAction(self.actionList_Project)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionDatabase_Equipment)
        self.menuFile.addAction(self.actionEdit_Database_Equipment)
        self.menuFile.addAction(self.menuShow_Database_Equipment.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuFile.addAction(self.actionExit_2)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit_3)
        self.menuEdit.addAction(self.actionNew_Edit)
        self.menuForm.addAction(self.actionNew_Form)
        self.menuHelp.addAction(self.actionNew_Help)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuForm.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.actionExit.triggered.connect(MainWindow.close) # type: ignore

        self.menuFile.triggered.connect(self.tableShow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def tableShow(self):
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.Form)
        self.Form.show()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuShow_Database_Equipment.setTitle(_translate("MainWindow", "Show Database Equipment"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuForm.setTitle(_translate("MainWindow", "Form"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionNew_Project.setText(_translate("MainWindow", "New Project"))
        self.actionList_Project.setText(_translate("MainWindow", "List Project"))
        self.actionDatabase_Equipment.setText(_translate("MainWindow", "Database Equipment"))
        self.actionEdit_Database_Equipment.setText(_translate("MainWindow", "Edit Database Equipment"))
        self.actionExit.setText(_translate("MainWindow", "New Client"))
        self.actionContainer.setText(_translate("MainWindow", "Container"))
        self.actionRing_Gamma.setText(_translate("MainWindow", "Ring Gamma"))
        self.actionPycnometer.setText(_translate("MainWindow", "Pycnometer"))
        self.actionMold.setText(_translate("MainWindow", "Mold"))
        self.actionCBR.setText(_translate("MainWindow", "CBR"))
        self.actionConsolidation.setText(_translate("MainWindow", "Consolidation"))
        self.actionExit_2.setText(_translate("MainWindow", "Show List Client"))
        self.actionExit_3.setText(_translate("MainWindow", "Exit"))
        self.actionNew_Form.setText(_translate("MainWindow", "New Form"))
        self.actionNew_Edit.setText(_translate("MainWindow", "New Edit"))
        self.actionNew_Help.setText(_translate("MainWindow", "New Help"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
