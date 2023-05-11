from PySide6.QtWidgets import *
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
        frame1.setGeometry(100,80,120,140)


        btnDesbloquearPC1 = QPushButton(self)
        btnDesbloquearPC1.setText('V')
        btnDesbloquearPC1.setGeometry(108,188,35,25)
        btnDesbloquearPC1.setStyleSheet('''
        background-color: green;
        border-radius: 8px;
        color: white;
        font-size: 18px;
        ''')

        btnBloquearPC1 = QPushButton(self)
        btnBloquearPC1.setText('X')
        btnBloquearPC1.setGeometry(175,188,35,25)
        btnBloquearPC1.setStyleSheet('''
        background-color: red;
        border-radius: 8px;
        color: white;
        font-size: 18px;
        ''')

        def desbloquear_PC1():
            print('PC 1 desbloqueado!')
        # def desbloquear_PC2():
        #     print('PC 2 desbloqueado!')
        # def desbloquear_PC3():
        #     print('PC 3 desbloqueado!')
        # def desbloquear_PC4():
        #     print('PC 4 desbloqueado!')
        # def desbloquear_PC5():
        #     print('PC 5 desbloqueado!')
        # def desbloquear_PC6():
        #     print('PC 6 desbloqueado!')

        btnDesbloquearPC1.clicked.connect(desbloquear_PC1)
        # btnDesbloquearPC2.clicked.connect(desbloquear_PC2)
        # btnDesbloquearPC3.clicked.connect(desbloquear_PC3)
        # btnDesbloquearPC4.clicked.connect(desbloquear_PC4)
        # btnDesbloquearPC5.clicked.connect(desbloquear_PC5)
        # btnDesbloquearPC6.clicked.connect(desbloquear_PC6)


        def bloquear_PC1():
            print('PC 1 bloqueado!')
        # def bloquear_PC2():
        #     print('PC 2 bloqueado!')
        # def bloquear_PC3():
        #     print('PC 3 bloqueado!')
        # def bloquear_PC4():
        #     print('PC 4 bloqueado!')
        # def bloquear_PC5():
        #     print('PC 5 bloqueado!')
        # def bloquear_PC6():
        #     print('PC 6 bloqueado!')
        
        btnBloquearPC1.clicked.connect(bloquear_PC1)
        # btnDesbloquearPC2.clicked.connect(bloquear_PC2)
        # btnDesbloquearPC3.clicked.connect(bloquear_PC3)
        # btnDesbloquearPC4.clicked.connect(bloquear_PC4)
        # btnDesbloquearPC5.clicked.connect(bloquear_PC5)
        # btnDesbloquearPC6.clicked.connect(bloquear_PC6)


app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec()
