from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtSvgWidgets import *
from corDoLayout import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle('Secure Access Tech')
        self.setFixedSize(700,500)

        layoutCima = QHBoxLayout()
        layoutBaixo = QHBoxLayout()

        # layoutCima.addWidget()

        layoutCima.addWidget(QPushButton('PC 1'))
        layoutCima.addWidget(QPushButton('PC 2'))
        layoutCima.addWidget(QPushButton('PC 3'))

        layoutBaixo.addWidget(QPushButton('PC 4'))
        layoutBaixo.addWidget(QPushButton('PC 5'))
        layoutBaixo.addWidget(QPushButton('PC 6'))

        widget = QWidget()
        mainLayout = QVBoxLayout()
        mainLayout.addLayout(layoutCima)
        mainLayout.addLayout(layoutBaixo)
        widget.setLayout(mainLayout)

        self.setCentralWidget(widget)

app = QApplication(sys.argv)

janela = MainWindow()
janela.show()

app.exec()
