from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle('Secure Access Tech')
        self.setFixedSize(1280,720)

        #   Ícones(.svg) dos botões
        iconeDesbloquear = QIcon("icons/unlock-white.svg")
        iconeBloquear = QIcon("icons/lock-white.svg")

        #   Frame pra cor de fundo da tela
        frameBackground = QFrame(self)
        frameBackground.setStyleSheet('''
        background-color: #ffffff;
        ''')
        frameBackground.setGeometry(0,0,1280,720)

        #   Frame da barra superior
        frameSuperior = QFrame(self)
        frameSuperior.setStyleSheet('''
        background-color: lightgray;
        ''')
        frameSuperior.setGeometry(0,0,1280,40)


        #   Frame do PC 1
        frame1 = QFrame(self)
        frame1.setStyleSheet('''
        background-color: #bdbdbd;
        border-radius: 40px;
        ''')
        frame1.setGeometry(150,80,200,240)

        #   Label/texto "PC 1"
        txt_PC1 = QLabel(self)
        txt_PC1.setText("PC  1")
        txt_PC1.setGeometry(217,90,50,25)
        txt_PC1.setStyleSheet('''
        background-color: #ffffff;
        border-radius: 8px;
        font-family: Verdana;
        font-size: 18px bold;
        ''')

        #   Ícone do monitor do PC 1
        iconeMonitor = QLabel(self)
        iconeMonitor.setPixmap(QPixmap("icons/monitor.png"))
        iconeMonitor.setGeometry(200,115,120,140)

        #   Botão para desbloquear o PC 1
        btnDesbloquearPC1 = QPushButton(self)
        btnDesbloquearPC1.setGeometry(165,255,60,50)
        btnDesbloquearPC1.setCursor(Qt.PointingHandCursor)
        btnDesbloquearPC1.setIcon(iconeDesbloquear)
        btnDesbloquearPC1.setIconSize(QSize(28,28))
        btnDesbloquearPC1.setStyleSheet('''
        background-color: green;
        border-radius: 25px;
        font-size: 18px;
        ''')

        #   Botão para bloquear o PC 1
        btnBloquearPC1 = QPushButton(self)
        btnBloquearPC1.setGeometry(275,255,60,50)
        btnBloquearPC1.setCursor(Qt.PointingHandCursor)
        btnBloquearPC1.setIcon(iconeBloquear)
        btnBloquearPC1.setIconSize(QSize(28,28))
        btnBloquearPC1.setStyleSheet('''
        background-color: red;
        border-radius: 25px;
        font-size: 18px;
        ''')


        #   Frame do PC 2
        frame2 = QFrame(self)
        frame2.setStyleSheet('''
        background-color: #bdbdbd;
        border-radius: 40px;
        ''')
        frame2.setGeometry(520,80,200,240)

        #   Botão para desbloquear o PC 2
        btnDesbloquearPC2 = QPushButton(self)
        btnDesbloquearPC2.setGeometry(380,255,60,50)
        btnDesbloquearPC2.setCursor(Qt.PointingHandCursor)
        btnDesbloquearPC2.setIcon(iconeDesbloquear)
        btnDesbloquearPC2.setIconSize(QSize(28,28))
        btnDesbloquearPC2.setStyleSheet('''
        background-color: green;
        border-radius: 25px;
        font-size: 18px;
        ''')

        #   Botão para bloquear o PC 2
        btnBloquearPC2 = QPushButton(self)
        btnBloquearPC2.setGeometry(470,255,60,50)
        btnBloquearPC2.setCursor(Qt.PointingHandCursor)
        btnBloquearPC2.setIcon(iconeBloquear)
        btnBloquearPC2.setIconSize(QSize(28,28))
        btnBloquearPC2.setStyleSheet('''
        background-color: red;
        border-radius: 25px;
        font-size: 18px;
        ''')


        #   Frame do PC 3
        frame3 = QFrame(self)
        frame3.setStyleSheet('''
        background-color: #bdbdbd;
        border-radius: 40px;
        ''')
        frame3.setGeometry(820,80,200,240)

        #   Botão para desbloquear o PC 3
        btnDesbloquearPC3 = QPushButton(self)
        btnDesbloquearPC3.setGeometry(680,255,60,50)
        btnDesbloquearPC3.setCursor(Qt.PointingHandCursor)
        btnDesbloquearPC3.setIcon(iconeDesbloquear)
        btnDesbloquearPC3.setIconSize(QSize(28,28))
        btnDesbloquearPC3.setStyleSheet('''
        background-color: green;
        border-radius: 25px;
        font-size: 18px;
        ''')

        #   Botão para bloquear o PC 3
        btnBloquearPC3 = QPushButton(self)
        btnBloquearPC3.setGeometry(770,255,60,50)
        btnBloquearPC3.setCursor(Qt.PointingHandCursor)
        btnBloquearPC3.setIcon(iconeBloquear)
        btnBloquearPC3.setIconSize(QSize(28,28))
        btnBloquearPC3.setStyleSheet('''
        background-color: red;
        border-radius: 25px;
        font-size: 18px;
        ''')


        #   Função para desbloquear o PC 1
        def desbloquear_PC1():
            print('PC 1 desbloqueado!')
        #   Função para desbloquear o PC 2
        def desbloquear_PC2():
            print('PC 2 desbloqueado!')
        #   Função para desbloquear o PC 3
        def desbloquear_PC3():
            print('PC 3 desbloqueado!')
        # def desbloquear_PC4():
        #     print('PC 4 desbloqueado!')
        # def desbloquear_PC5():
        #     print('PC 5 desbloqueado!')
        # def desbloquear_PC6():
        #     print('PC 6 desbloqueado!')


        #   Ligando a função ao btnDesbloquearPC1
        btnDesbloquearPC1.clicked.connect(desbloquear_PC1)
        #   Ligando a função ao btnDesbloquearPC2
        btnDesbloquearPC2.clicked.connect(desbloquear_PC2)
        #   Ligando a função ao btnDesbloquearPC3
        btnDesbloquearPC3.clicked.connect(desbloquear_PC3)
        # btnDesbloquearPC4.clicked.connect(desbloquear_PC4)
        # btnDesbloquearPC5.clicked.connect(desbloquear_PC5)
        # btnDesbloquearPC6.clicked.connect(desbloquear_PC6)


        #   Função que altera o ícone dos PCs para bloqueado
        def pc_Bloqueado(x,y,width,height):
            bloqueado = QPixmap("icons/lock-black.png")
            iconeMonitor.setPixmap(bloqueado)
            iconeMonitor.setGeometry(x,y,width,height)


        #   Função para bloquear o PC 1
        def bloquear_PC1():
            pc_Bloqueado(200,115,120,140)
        #   Função para bloquear o PC 2
        def bloquear_PC2():
            pc_Bloqueado()
            print('PC 2 bloqueado!')
        #   Função para bloquear o PC 3
        def bloquear_PC3():
            pc_Bloqueado()
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