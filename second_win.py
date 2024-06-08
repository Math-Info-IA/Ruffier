from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)


from intsr import *
from final_win import *


class TestWin(QWidget):
       def __init__(self):
              super().__init__()
              self.set_appear()
              self.initUI()
              self.connects()
              self.show()
       def set_appear(self):
              self.setWindowTitle(txt_title)
              self.resize(win_width, win_height)
              self.move(win_x, win_y)
       def initUI(self):
              self.h_line = QHBoxLayout()
              self.r_line = QVBoxLayout()
              self.l_line = QVBoxLayout()

              self.name = QLineEdit()
              self.age = QLineEdit()
              self.p1 = QLineEdit()
              self.p2 = QLineEdit()
              self.p3 = QLineEdit()
              self.p4 = QLineEdit()

              self.btn1 = QPushButton()
              self.btn2 = QPushButton()
              self.btn3 = QPushButton()
              self.btn4 = QPushButton()

              self.txt_name = QLabel(txt_name)
              self.txt_age = QLabel(txt_age)
              self.txt_test1 = QLabel(txt_test1)
              self.txt_test2 = QLabel(txt_test2)
              self.txt_test3 = QLabel(txt_test3)
              #Adding widgets
              self.l_line.addWidget(self.text_name)
              self.l_line.addWidget(self.name)
              self.l_line.addWidget(self.text_age)
              self.l_line.addWidget(self.age)
              self.l_line.addWidget(self.text_test1)
              self.l_line.addWidget(self.btn1)
              self.l_line.addWidget(self.p1)
              self.l_line.addWidget(self.text_test2)
              self.l_line.addWidget(self.btn2)
              self.l_line.addWidget(self.p2)
              self.l_line.addWidget(self.text_test3)
              self.l_line.addWidget(self.btn3)
              self.l_line.addWidget(self.p3) 
              self.r_line.addWidget(self.timer)
              self.l_line.addWidget(self.btn4, alignment=Qt.AlignCenter)

              self.h_line.addLayout(self.l_line)
              self.h_line.addLayout(self.r_line)
              self.setLayout(self.h_line)
       def connects(self):
              self.btn4.clicked.connect(self.next_click)
       def next_click(self):
              self.hide()
              self.fw=FinalWin()

              





