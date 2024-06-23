from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont 
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout, QGridLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)
      
from instruction import *


class FinalWin(QWidget):
       def __init__(self, exp):
              super().__init__()
              self.exp = exp
              self.initUI()
              self.set_appear()
              self.show()
       
       def initUI(self):
              self.work_text = QLabel(txt_workheart + str(self.results()))
              self.index_text = QLabel(txt_index + str(self.index))
              
              self.work_text.setStyleSheet("font-size: 18px; color: #444;")
              self.index_text.setStyleSheet("font-size: 18px; color: #444;")


              self.layout_line = QVBoxLayout()
              self.layout_line.addWidget(self.index_text, alignment = Qt.AlignCenter)
              self.layout_line.addWidget(self.work_text, alignment = Qt.AlignCenter)        
              self.setLayout(self.layout_line)

       def set_appear(self):
              self.setWindowTitle(txt_finalwin)
              self.resize(win_width, win_height)
              self.move(win_x, win_y)

       def results(self):
              self.index = (4*(int(self.exp.t1)+int(self.exp.t2)+int(self.exp.t3))-200)/10
              if int(self.exp.age) >= 15:
                     if self.index >= 15:
                            return txt_res1
                     elif self.index < 15 and self.index >= 11 :
                            return txt_res2
                     elif self.index < 11 and self.index >= 6 :
                            return txt_res3
                      elif self.index < 6 and self.index >= 0.5 :
                            return txt_res4
                      elif self.index < 0.4 :
                            return txt_res5
                     
             
