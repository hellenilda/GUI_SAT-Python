from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel
from PySide6.QtCore import Qt, QSize
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Estudos')

        widget = QLabel('LABEL')
        fonte = widget.font()
        fonte.setPointSize(25)
        widget.setFont(fonte)

        widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.setFixedSize(QSize(400,300))
        self.setCentralWidget(widget)

app = QApplication(sys.argv)

janela = MainWindow()
janela.show()

app.exec()
