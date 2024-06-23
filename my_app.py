from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit)

from instruction import *
from second_win import *

       
class MainWin(QWidget):
    def __init__(self):
        ''' the window which the greeting is located in '''
        super().__init__()

        self.initUI()
        self.connects()
        self.set_appear()

        self.show()

    def initUI(self):
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.btn_next = QPushButton(txt_next, self)
        self.btn_next.setStyleSheet("""
                    QPushButton {   background-color: #3498db; 
                                    color: white; 
                                    font-size: 30px;
                                    border-radius:20px;
                                    padding: 15px 50px;
                                }
                    QPushButton:hover { color: blue;
                                        background-color: gray;}
                                        
                    QPushButton:pressed {  
                                    color: black;
                                    background-color : red;  
                                            }
                    """)             
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.hello_text, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.instruction, alignment = Qt.AlignLeft) 
        self.layout_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)          
        self.setLayout(self.layout_line)

    
    def next_click(self):
        self.tw = TestWin()
        self.hide()
    

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

app = QApplication([])
mw = MainWin()
app.exec_()

