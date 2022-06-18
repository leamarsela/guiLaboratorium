from PyQt5.QtWidgets import QWidget, QPushButton


class Classification(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(300, 200)
        self.move(350, 250)
        self.setWindowTitle('Classification')

        self.button = QPushButton('Tutup')
        self.button.move(50, 50)
        self.button.setParent(self)

        self.button.clicked.connect(self.buttonClick)

    def buttonClick(self):
        self.close()
