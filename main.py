from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QHBoxLayout
from PySide6.QtCore import QSize
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
 
        self.setWindowTitle('Secure Access Tech')
        self.setFixedSize(QSize(700,500))

        layout = QHBoxLayout()

        widget = QWidget()
        widget.setLayout(layout)

        self.centralWidget(widget)

        txtPC1 = QLabel('PC 1')
        txtPC2 = QLabel('PC 2')
        txtPC3 = QLabel('PC 3')
        txtPC4 = QLabel('PC 4')
        txtPC5 = QLabel('PC 5')
        txtPC6 = QLabel('PC 6')

        self.btnPC1 = QPushButton('PC 1')
        self.btnPC2 = QPushButton('PC 2')
        self.btnPC3 = QPushButton('PC 3')
        self.btnPC4 = QPushButton('PC 4')
        self.btnPC5 = QPushButton('PC 5')
        self.btnPC6 = QPushButton('PC 6')

        fonte = txtPC1.font()
        fonte.setPointSize(35)
        txtPC1.setFont(fonte)

        self.btnPC1.clicked.connect(self.clicked_button)

    def clicked_button(self):
        print('PC 1')


app = QApplication(sys.argv)

janela = MainWindow()
janela.show()

app.exec()