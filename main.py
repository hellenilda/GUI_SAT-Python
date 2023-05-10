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

        btnPC1 = QPushButton('PC 1')
        btnPC2 = QPushButton('PC 2')
        btnPC3 = QPushButton('PC 3')
        btnPC4 = QPushButton('PC 4')
        btnPC5 = QPushButton('PC 5')
        btnPC6 = QPushButton('PC 6')

        mainLayout = QVBoxLayout()
        widget = QWidget()

        widget.setLayout(mainLayout)
        self.setCentralWidget(widget)


        btnPC1.setStyleSheet('''
        background-color: white;
        border: 5px black;
        border-radius: 10px;
        height: 30px;
        ''')

        btnPC2.setStyleSheet('''
        background-color: white;
        border: 5px black;
        border-radius: 10px;
        height: 30px;
        ''')

        btnPC3.setStyleSheet('''
        background-color: white;
        border: 5px black;
        border-radius: 10px;
        height: 30px;
        ''')

        btnPC4.setStyleSheet('''
        background-color: white;
        border: 5px black;
        border-radius: 10px;
        height: 30px;
        ''')

        btnPC5.setStyleSheet('''
        background-color: white;
        border: 5px black;
        border-radius: 10px;
        height: 30px;
        ''')

        btnPC6.setStyleSheet('''
        background-color: white;
        border: 5px black;
        border-radius: 10px;
        height: 30px;
        ''')

        def PC1_clicado():
            print('PC 1')
        def PC2_clicado():
            print('PC 2')
        def PC3_clicado():
            print('PC 3')
        def PC4_clicado():
            print('PC 4')
        def PC5_clicado():
            print('PC 5')
        def PC6_clicado():
            print('PC 6')

        btnPC1.clicked.connect(PC1_clicado)
        btnPC2.clicked.connect(PC2_clicado)
        btnPC3.clicked.connect(PC3_clicado)
        btnPC4.clicked.connect(PC4_clicado)
        btnPC5.clicked.connect(PC5_clicado)
        btnPC6.clicked.connect(PC6_clicado)


app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec()
