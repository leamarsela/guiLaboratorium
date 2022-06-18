import sys

from PyQt5.QtWidgets import (
    QDialog,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton
)


class DbProject(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(500, 400)
        self.move(500, 500)
        self.setWindowTitle('Tambah/Edit Data Project')

        self.mode = -1  #0: mode tambah, 1: mode ubah

        self.okButton = QPushButton('Ok')
        self.cancelButton = QPushButton('Batal')

        hbox = QHBoxLayout()
        hbox.addWidget(self.okButton)
        hbox.addWidget(self.cancelButton)

        self.label1 = QLabel('PROJECT NUMBER:')
        self.projectNumberLineEdit = QLineEdit()
        self.label2 = QLabel('CLIENT:')
        self.clientLineEdit = QLineEdit()
        self.label3 = QLabel('PROJECT')
        self.projectLinetEdit = QLineEdit()

        if self.mode == 0:
            self.projectNumberLineEdit.clear()
            self.clientLineEdit.clear()
            self.projectLinetEdit.clear()

        layout = QGridLayout()
        layout.addWidget(self.label1, 0, 0)
        layout.addWidget(self.projectNumberLineEdit, 0, 1)
        layout.addWidget(self.label2, 1, 0)
        layout.addWidget(self.clientLineEdit, 1, 1)
        layout.addWidget(self.label3, 2, 0)
        layout.addWidget(self.projectLinetEdit, 2, 1)
        layout.addLayout(hbox, 3, 1)
        self.setLayout(layout)

        self.okButton.clicked.connect(self.accept)
        self.cancelButton.clicked.connect(self.reject)
