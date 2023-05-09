from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Color(QWidget):
    def __init__(self, color):
        super().__init__

        self.setAutoFillBackground(True)

        paleta = self.palette()
        paleta.setColor(QPalette.Window, QColor(color))
        self.setPalette(paleta)