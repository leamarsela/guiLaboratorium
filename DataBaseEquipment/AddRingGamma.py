import sys

from addRingGammaUi import *

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *

class AddRingGamma(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.addRingGamma = Ui_addRingGamma()
        self.addRingGamma.setupUi(self)

        
if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = AddRingGamma()
    main.show()

    app.exec_()
