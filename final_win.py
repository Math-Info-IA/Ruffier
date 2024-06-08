from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # checking the types of input values
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout, QGridLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)
      
from instr import *


class FinalWin(QWidget):
    def __init__(self, exp):
        ''' the window in which the survey is being conducted '''
        super().__init__()

        #getting data about the experiment
        self.exp = exp

        # creating and configuring graphic elements:
        self.initUI()

        # sets what the window will look like (label, size, location)
        self.set_appear()
        
        # start:
        self.show()



    def initUI(self):
        ''' creates graphic elements '''
        self.work_text = QLabel(txt_workheart + self.results())
        self.index_text = QLabel(txt_index + str(self.index))
        
        self.work_text.setStyleSheet("font-size: 18px; color: #444;")
        self.index_text.setStyleSheet("font-size: 18px; color: #444;")


        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.index_text, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.work_text, alignment = Qt.AlignCenter)        
        self.setLayout(self.layout_line)


    ''' sets what the window will look like (label, size, location) '''
    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def results(self):
        self.index= "TO DO"
        return "TO DO"


