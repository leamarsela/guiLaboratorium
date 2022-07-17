import sys

from ListSampleUi import *

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *


class ListSample(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.listSample = Ui_Form()
        self.listSample.setupUi(self)
        self.label = self.listSample.label
        self.cobaTable()

    def buatCheckBox(self, namaCb):
        temp = QCheckBox(self)
        temp.setChecked(True)
        temp.setObjectName(str(namaCb))
        temp.stateChanged.connect(lambda: self.pencet(temp))

        return temp

    def cobaTable(self):
        self.listSample.tableWidget.clear()
        columnHeaders = ['List Sample', 'Moisture Content', 'Atterberg Limit']
        self.listSample.tableWidget.setColumnCount(len(columnHeaders))
        self.listSample.tableWidget.setHorizontalHeaderLabels(columnHeaders)

        self.cb1 = QCheckBox()
        self.cb1.setObjectName('cb1')
        self.cb1.toggled.connect(lambda: self.pencet)

        self.cb2 = QCheckBox()
        self.cb2.setObjectName('cb2')
        self.cb2.toggled.connect(lambda: self.pencet)

        for i in range(3):
            for col in range(2):
                layout = QWidget()
                hBox = QHBoxLayout()
                hBox.setAlignment(Qt.AlignCenter)
                hBox.addWidget(self.buatCheckBox('bx' + str(i) + str(col)))
                layout.setLayout(hBox)

                self.listSample.tableWidget.setCellWidget(i, col + 1, layout)


    def pencet(self, b):
        if b.isChecked() == True:
            print(b.objectName() + 'True')
        else:
            print(b.objectName() + 'False')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = ListSample()
    main.show()

    app.exec_()
