from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle('Secure Access Tech')
        self.setFixedSize(1280,720)

        iconeDesbloquear = QIcon("icons/unlock-white.svg")
        iconeBloquear = QIcon("icons/lock-white.svg")
        iconeMonitor = QIcon("icons/monitor.svg")


        frameBackground = QFrame(self)
        frameBackground.setStyleSheet('''
        background-color: gray;
        ''')
        frameBackground.setGeometry(0,0,1280,720)

        frameSuperior = QFrame(self)
        frameSuperior.setStyleSheet('''
        background-color: lightgray;
        ''')
        frameSuperior.setGeometry(0,0,1280,40)

        frame1 = QFrame(self)
        frame1.setStyleSheet('''
        background-color: white;
        border-radius: 30px;
        ''')
        frame1.setGeometry(50,80,160,200)

        txt_PC1 = QLabel(self)
        txt_PC1.setText("PC  1")
        txt_PC1.setGeometry(117,90,50,25)
        txt_PC1.setStyleSheet('''
        background-color: lightgray;
        border-radius: 8px;
        font-family: Verdana;
        font-size: 18px bold;
        ''')

        btnDesbloquearPC1 = QPushButton(self)
        btnDesbloquearPC1.setGeometry(60,230,50,40)
        btnDesbloquearPC1.setCursor(Qt.PointingHandCursor)
        btnDesbloquearPC1.setIcon(iconeDesbloquear)
        btnDesbloquearPC1.setIconSize(QSize(28,28))
        btnDesbloquearPC1.setStyleSheet('''
        background-color: green;
        border-radius: 20px;
        color: white;
        font-size: 18px;
        ''')

        btnBloquearPC1 = QPushButton(self)
        btnBloquearPC1.setGeometry(170,230,50,40)
        btnBloquearPC1.setCursor(Qt.PointingHandCursor)
        btnBloquearPC1.setIcon(iconeBloquear)
        btnBloquearPC1.setIconSize(QSize(28,28))
        btnBloquearPC1.setStyleSheet('''
        background-color: red;
        border-radius: 20px;
        color: white;
        font-size: 18px;
        ''')


        frame2 = QFrame(self)
        frame2.setStyleSheet('''
        background-color: white;
        border-radius: 30px;
        ''')
        frame2.setGeometry(370,80,160,200)

        btnDesbloquearPC2 = QPushButton(self)
        btnDesbloquearPC2.setGeometry(380,230,50,40)
        btnDesbloquearPC2.setCursor(Qt.PointingHandCursor)
        btnDesbloquearPC2.setIcon(iconeDesbloquear)
        btnDesbloquearPC2.setIconSize(QSize(28,28))
        btnDesbloquearPC2.setStyleSheet('''
        background-color: green;
        border-radius: 20px;
        color: white;
        font-size: 18px;
        ''')

        btnBloquearPC2 = QPushButton(self)
        btnBloquearPC2.setGeometry(490,230,50,40)
        btnBloquearPC2.setCursor(Qt.PointingHandCursor)
        btnBloquearPC2.setIcon(iconeBloquear)
        btnBloquearPC2.setIconSize(QSize(28,28))
        btnBloquearPC2.setStyleSheet('''
        background-color: red;
        border-radius: 20px;
        color: white;
        font-size: 18px;
        ''')


        frame3 = QFrame(self)
        frame3.setStyleSheet('''
        background-color: white;
        border-radius: 30px;
        ''')
        frame3.setGeometry(670,80,160,200)

        btnDesbloquearPC3 = QPushButton(self)
        btnDesbloquearPC3.setGeometry(680,230,50,40)
        btnDesbloquearPC3.setCursor(Qt.PointingHandCursor)
        btnDesbloquearPC3.setIcon(iconeDesbloquear)
        btnDesbloquearPC3.setIconSize(QSize(28,28))
        btnDesbloquearPC3.setStyleSheet('''
        background-color: green;
        border-radius: 20px;
        color: white;
        font-size: 18px;
        ''')

        btnBloquearPC3 = QPushButton(self)
        btnBloquearPC3.setGeometry(790,230,50,40)
        btnBloquearPC3.setCursor(Qt.PointingHandCursor)
        btnBloquearPC3.setIcon(iconeBloquear)
        btnBloquearPC3.setIconSize(QSize(28,28))
        btnBloquearPC3.setStyleSheet('''
        background-color: red;
        border-radius: 20px;
        color: white;
        font-size: 18px;
        ''')


        def desbloquear_PC1():
            print('PC 1 desbloqueado!')
        def desbloquear_PC2():
            print('PC 2 desbloqueado!')
        def desbloquear_PC3():
            print('PC 3 desbloqueado!')
        # def desbloquear_PC4():
        #     print('PC 4 desbloqueado!')
        # def desbloquear_PC5():
        #     print('PC 5 desbloqueado!')
        # def desbloquear_PC6():
        #     print('PC 6 desbloqueado!')

        btnDesbloquearPC1.clicked.connect(desbloquear_PC1)
        btnDesbloquearPC2.clicked.connect(desbloquear_PC2)
        btnDesbloquearPC3.clicked.connect(desbloquear_PC3)
        # btnDesbloquearPC4.clicked.connect(desbloquear_PC4)
        # btnDesbloquearPC5.clicked.connect(desbloquear_PC5)
        # btnDesbloquearPC6.clicked.connect(desbloquear_PC6)


        def bloquear_PC1():
            print('PC 1 bloqueado!')
        def bloquear_PC2():
            print('PC 2 bloqueado!')
        def bloquear_PC3():
            print('PC 3 bloqueado!')
        # def bloquear_PC4():
        #     print('PC 4 bloqueado!')
        # def bloquear_PC5():
        #     print('PC 5 bloqueado!')
        # def bloquear_PC6():
        #     print('PC 6 bloqueado!')
        
        btnBloquearPC1.clicked.connect(bloquear_PC1)
        btnBloquearPC2.clicked.connect(bloquear_PC2)
        btnBloquearPC3.clicked.connect(bloquear_PC3)
        # btnBloquearPC4.clicked.connect(bloquear_PC4)
        # btnBloquearPC5.clicked.connect(bloquear_PC5)
        # btnBloquearPC6.clicked.connect(bloquear_PC6)


app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec()
