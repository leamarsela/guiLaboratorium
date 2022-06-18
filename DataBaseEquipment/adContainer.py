import sys

from adContainerUi import *

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *

class AdContainer(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        super().__init__()
        self.adContainer = Ui_Dialog()
        self.adContainer.setupUi(self)

        self.adContainer.buttonBox.accepted.connect(self.cetak)

    def cetak(self):
        self.accept()
        self.adContainerLineEditId = self.adContainer.lineEditContainerId.text()



if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = AdContainer()
    main.show()

    app.exec_()
