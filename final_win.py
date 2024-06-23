#The final_win.py file

from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # checking the types of input values
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout, QGridLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)
      
from instruction import *

class Experiment():
   def __init__(self, age, test1, test2, test3):
       self.age = age
       self.t1 = test1
       self.t2 = test2
       self.t3 = test3

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
              self.index = (4 * (int(self.exp.t1) + int(self.exp.t2) + int(self.exp.t3)) - 200) / 10
              if self.exp.age >= 15:
                     if self.index >= 15:
                            return txt_res1
                     elif self.index < 15 and self.index >= 11:
                            return txt_res2
                     elif self.index < 11 and self.index >= 6:
                            return txt_res3
                     elif self.index < 6 and self.index >= 0.5:
                            return txt_res4
                     else:
                            return txt_res5

