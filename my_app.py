from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QFont

from instr import *
from second_win import *
from final_win import *

class FirstScreen(QWidget):

    def __init__(self):
        super().__init__()
        self.setup_screen()
        self.setup_ui()
        self.connects()

    def setup_screen(self):
        self.setWindowTitle(screen_title)
        self.resize(win_width, win_height)
        self.show()

    def setup_ui(self):
        
        main_line = QVBoxLayout()
        
        text1 = QLabel(txt_hello)
        main_line.addWidget(text1, alignment=Qt.AlignLeft)

        instruction = QLabel(txt_instruction)
        main_line.addWidget(instruction, alignment=Qt.AlignLeft)

        self.startbutton = QPushButton('Начать')
        main_line.addWidget(self.startbutton, alignment=Qt.AlignCenter)
        
        self.setLayout(main_line)
    
    def connects(self):
        self.startbutton.clicked.connect(self.next_screen)
        

    def next_screen(self):
        self.screen2 = SecondScreen()
        self.hide()

app = QApplication([])

screen = FirstScreen()

app.exec_()