import sys

from addContainerUi import *

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *

class AddContainer(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.addContainer = Ui_addContainer()
        self.addContainer.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = AddContainer()
    main.show()

    app.exec_()
