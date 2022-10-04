import sys
import PyQt5

from interface import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = window()
    #win.setCentralWidget(cubeface)
    win.show()
    sys.exit(app.exec())

