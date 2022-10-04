from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets


class window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Rubiks Solver'
        self.left = 300
        self.top = 200
        self.width = 800
        self.height = 500
        self.createui()

    def createui(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)
        self.setStyleSheet("""
        background: 'white';
        """)
        self.grid = QGridLayout()
        self.initialisecube()
    #places the faces of the cube
    def initialisecube(self):
        self.redface = QPixmap("cubefacecolor/red.png")
        self.redfacelabel = QLabel(self)
        self.redfacelabel.setPixmap(self.redface)
        self.grid.addWidget(self.redfacelabel, 100, 100)

    
    def cubeface(self, cubeface):
        self.cubeface.setText('Click')
        
