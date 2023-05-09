from PySide6.QtWidgets import *
from PySide6.QtCore import QSize
from layout_color import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
 
        self.setWindowTitle('Secure Access Tech')
        self.setFixedSize(QSize(700,500))

        # layout = QHBoxLayout()
        # layout.addWidget(Color('red'))

        # widget = QWidget()
        # widget.setLayout(layout)

        # self.setCentralWidget(widget)

        self.btnPC1 = QPushButton('PC 1')
        self.btnPC2 = QPushButton('PC 2')
        self.btnPC3 = QPushButton('PC 3')
        self.btnPC4 = QPushButton('PC 4')
        self.btnPC5 = QPushButton('PC 5')
        self.btnPC6 = QPushButton('PC 6')

        self.btnPC1.clicked.connect(self.clicked_button)

    def clicked_button(self):
        print('PC 1')


app = QApplication(sys.argv)

janela = MainWindow()
janela.show()

app.exec()