# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\addRingGamma.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addRingGamma(object):
    def setupUi(self, addRingGamma):
        addRingGamma.setObjectName("addRingGamma")
        addRingGamma.resize(359, 313)
        self.buttonBox = QtWidgets.QDialogButtonBox(addRingGamma)
        self.buttonBox.setGeometry(QtCore.QRect(20, 260, 321, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lineEditRingId = QtWidgets.QLineEdit(addRingGamma)
        self.lineEditRingId.setGeometry(QtCore.QRect(200, 20, 141, 41))
        self.lineEditRingId.setObjectName("lineEditRingId")
        self.lineEditWeightRing = QtWidgets.QLineEdit(addRingGamma)
        self.lineEditWeightRing.setGeometry(QtCore.QRect(200, 80, 141, 41))
        self.lineEditWeightRing.setObjectName("lineEditWeightRing")
        self.lineEditDiameterRing = QtWidgets.QLineEdit(addRingGamma)
        self.lineEditDiameterRing.setGeometry(QtCore.QRect(200, 130, 141, 41))
        self.lineEditDiameterRing.setObjectName("lineEditDiameterRing")
        self.lineEditThickRing = QtWidgets.QLineEdit(addRingGamma)
        self.lineEditThickRing.setGeometry(QtCore.QRect(200, 190, 141, 41))
        self.lineEditThickRing.setObjectName("lineEditThickRing")
        self.layoutWidget = QtWidgets.QWidget(addRingGamma)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 130, 181, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.widget = QtWidgets.QWidget(addRingGamma)
        self.widget.setGeometry(QtCore.QRect(20, 20, 181, 101))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        self.retranslateUi(addRingGamma)
        self.buttonBox.accepted.connect(addRingGamma.accept) # type: ignore
        self.buttonBox.rejected.connect(addRingGamma.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(addRingGamma)

    def retranslateUi(self, addRingGamma):
        _translate = QtCore.QCoreApplication.translate
        addRingGamma.setWindowTitle(_translate("addRingGamma", "Add Ring Gamma"))
        self.label_3.setText(_translate("addRingGamma", "Diameter (mm) :"))
        self.label_4.setText(_translate("addRingGamma", "Thickness (mm.) :"))
        self.label.setText(_translate("addRingGamma", "Ring Gamma ID :"))
        self.label_2.setText(_translate("addRingGamma", "Weight Ring (gr.) :"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     addRingGamma = QtWidgets.QDialog()
#     ui = Ui_addRingGamma()
#     ui.setupUi(addRingGamma)
#     addRingGamma.show()
#     sys.exit(app.exec_())
