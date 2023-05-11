from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle('Secure Access Tech')
        self.setFixedSize(700,500)

        iconUnlock = QIcon("icons/unlock-white.png")
        iconLock = QIcon("icons/lock-white.png")

        frameSuperior = QFrame(self)
        frameSuperior.setStyleSheet('''
        background-color: lightgray;
        ''')
        frameSuperior.setGeometry(0,0,700,40)

        # frameLateral = QFrame(self)
        # frameLateral.setStyleSheet('''
        # background-color: gray;
        # ''')
        # frameLateral.setGeometry(0,40,60,460)

        frame1 = QFrame(self)
        frame1.setStyleSheet('''
        background-color: gray;
        border-radius: 10px;
        ''')
        frame1.setGeometry(75,80,120,140)


        btnDesbloquearPC1 = QPushButton(self)
        btnDesbloquearPC1.setGeometry(83,188,35,25)
        btnDesbloquearPC1.setCursor(Qt.PointingHandCursor)
        btnDesbloquearPC1.setIcon(iconUnlock)
        btnDesbloquearPC1.setIconSize(QSize(18,18))
        btnDesbloquearPC1.setStyleSheet('''
        background-color: green;
        border-radius: 8px;
        color: white;
        font-size: 18px;
        ''')

        btnBloquearPC1 = QPushButton(self)
        btnBloquearPC1.setGeometry(150,188,35,25)
        btnBloquearPC1.setCursor(Qt.PointingHandCursor)
        btnBloquearPC1.setIcon(iconLock)
        btnBloquearPC1.setIconSize(QSize(18,18))
        btnBloquearPC1.setStyleSheet('''
        background-color: red;
        border-radius: 8px;
        color: white;
        font-size: 18px;
        ''')

        frame2 = QFrame(self)
        frame2.setStyleSheet('''
        background-color: gray;
        border-radius: 10px;
        ''')
        frame2.setGeometry(290,80,120,140)


        btnDesbloquearPC2 = QPushButton(self)
        btnDesbloquearPC2.setGeometry(298,188,35,25)
        btnDesbloquearPC2.setCursor(Qt.PointingHandCursor)
        btnDesbloquearPC2.setIcon(iconUnlock)
        btnDesbloquearPC2.setIconSize(QSize(18,18))
        btnDesbloquearPC2.setStyleSheet('''
        background-color: green;
        border-radius: 8px;
        color: white;
        font-size: 18px;
        ''')

        btnBloquearPC2 = QPushButton(self)
        btnBloquearPC2.setGeometry(368,188,35,25)
        btnBloquearPC2.setCursor(Qt.PointingHandCursor)
        btnBloquearPC2.setIcon(iconLock)
        btnBloquearPC2.setIconSize(QSize(18,18))
        btnBloquearPC2.setStyleSheet('''
        background-color: red;
        border-radius: 8px;
        color: white;
        font-size: 18px;
        ''')

        frame3 = QFrame(self)
        frame3.setStyleSheet('''
        background-color: gray;
        border-radius: 10px;
        ''')
        frame3.setGeometry(500,80,120,140)


        btnDesbloquearPC3 = QPushButton(self)
        btnDesbloquearPC3.setGeometry(508,188,35,25)
        btnDesbloquearPC3.setCursor(Qt.PointingHandCursor)
        btnDesbloquearPC3.setIcon(iconUnlock)
        btnDesbloquearPC3.setIconSize(QSize(18,18))
        btnDesbloquearPC3.setStyleSheet('''
        background-color: green;
        border-radius: 8px;
        color: white;
        font-size: 18px;
        ''')

        btnBloquearPC3 = QPushButton(self)
        btnBloquearPC3.setGeometry(575,188,35,25)
        btnBloquearPC3.setCursor(Qt.PointingHandCursor)
        btnBloquearPC3.setIcon(iconLock)
        btnBloquearPC3.setIconSize(QSize(18,18))
        btnBloquearPC3.setStyleSheet('''
        background-color: red;
        border-radius: 8px;
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
