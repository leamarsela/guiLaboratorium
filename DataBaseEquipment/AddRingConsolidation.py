import sys

from addRingConsolidationUi import *

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *


class AddRingConsolidation(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.addRingConsolidation = Ui_addRingConsolidation()
        self.addRingConsolidation.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = AddRingConsolidation()
    main.show()

    app.exec_()
