import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from core import scrappy


class Application(QMainWindow):
    def __init__(self, master=None):
        super().__init__(master)
        self.setGeometry(400,250,300,400)
        self.setWindowTitle("data_scrapper_demo")
        self.setWindowIcon(QIcon("icon.png"))
        

        btn = QPushButton("Download", self)
        btn.move(97, 350)
        btn.clicked.connect(self.core)
    
    def core(self):
        scrappy

        self.sleep(1)

app = QApplication(sys.argv)
window = Application()
window.show()
app.exec_()