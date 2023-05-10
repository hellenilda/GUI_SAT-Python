from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtSvgWidgets import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle('Secure Access Tech')
        self.setFixedSize(700,500)

        frameSuperior = QFrame(self)
        frameSuperior.setStyleSheet('''
        background-color: lightgray;
        ''')
        frameSuperior.setGeometry(0,0,700,40)

        frameLateral = QFrame(self)
        frameLateral.setStyleSheet('''
        background-color: gray;
        ''')
        frameLateral.setGeometry(0,40,60,460)

        frame1 = QFrame(self)
        frame1.setStyleSheet('''
        background-color: gray;
        border-radius: 10px;
        ''')
        frame1.setGeometry(80,60,110,100)

        btnPC1 = QPushButton(self)
        btnPC1.setText('PC 1')
        btnPC1.setGeometry(100,200,60,30)

        # btnPC1.setStyleSheet('''
        # background-color: white;
        # border: 5px black;
        # border-radius: 10px;
        # height: 30px;
        # ''')

        # def PC1_clicado():
        #     print('PC 1')
        # def PC2_clicado():
        #     print('PC 2')
        # def PC3_clicado():
        #     print('PC 3')
        # def PC4_clicado():
        #     print('PC 4')
        # def PC5_clicado():
        #     print('PC 5')
        # def PC6_clicado():
        #     print('PC 6')

        # btnPC1.clicked.connect(PC1_clicado)
        # btnPC2.clicked.connect(PC2_clicado)
        # btnPC3.clicked.connect(PC3_clicado)
        # btnPC4.clicked.connect(PC4_clicado)
        # btnPC5.clicked.connect(PC5_clicado)
        # btnPC6.clicked.connect(PC6_clicado)


app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec()
