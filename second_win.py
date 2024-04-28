from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QFont

from instr import *
from final_win import *

class SecondScreen(QWidget):

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
        
        main_linescr2 = QHBoxLayout()
        v_line1 = QVBoxLayout()
        v_line2 = QVBoxLayout()

        name = QLabel(txt_name)
        v_line1.addWidget(name, alignment=Qt.AlignLeft)

        hintname = QLineEdit(txt_hintname)
        v_line1.addWidget(hintname, alignment=Qt.AlignLeft)

        kage = QLabel(txt_kage)
        v_line1.addWidget(kage, alignment=Qt.AlignLeft)

        self.hintkage = QLineEdit(txt_hintkage)
        v_line1.addWidget(self.hintkage, alignment=Qt.AlignLeft)

        guide1 = QLabel(txt_guide1)
        v_line1.addWidget(guide1, alignment=Qt.AlignLeft)

        self.testbutton1 = QPushButton('Начать первый тест')
        v_line1.addWidget(self.testbutton1, alignment=Qt.AlignLeft)
        
        self.hinttest1 = QLineEdit(txt_hinttest1)
        v_line1.addWidget(self.hinttest1, alignment=Qt.AlignLeft)

        guide2 = QLabel(txt_guide2)
        v_line1.addWidget(guide2, alignment=Qt.AlignLeft)

        self.testbutton2 = QPushButton('Начать делать приседания')
        v_line1.addWidget(self.testbutton2, alignment=Qt.AlignLeft)
        
        guide3 = QLabel(txt_guide3)
        v_line1.addWidget(guide3, alignment=Qt.AlignLeft)

        self.testbutton3 = QPushButton('Начать финальный тест')
        v_line1.addWidget(self.testbutton3, alignment=Qt.AlignLeft)

        self.hinttest2 = QLineEdit(txt_hinttest2)
        v_line1.addWidget(self.hinttest2, alignment=Qt.AlignLeft)

        self.hinttest3 = QLineEdit(txt_hinttest3)
        v_line1.addWidget(self.hinttest3, alignment=Qt.AlignLeft)

        self.finaltestbutton = QPushButton('Отправить результаты')
        v_line1.addWidget(self.finaltestbutton, alignment=Qt.AlignCenter)

        self.timer_label = QLabel('00:00:00')
        self.timer_label.setFont(QFont('Times', 36, QFont.Bold))
        v_line2.addWidget(self.timer_label, alignment=Qt.AlignRight)

        main_linescr2.addLayout(v_line1)
        main_linescr2.addLayout(v_line2)
        self.setLayout(main_linescr2)

    def timer1(self):
        global time
        time = QTime(0, 0, 16)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_event)
        self.timer.start(1000)

    def timer2(self):
        global time
        time = QTime(0, 0, 31)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_event)
        self.timer.start(1500)
    
    def timer3(self):
        global time
        time = QTime(0, 1, 1)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_event)
        self.timer.start(1000)
    
        
    def connects(self):
        self.finaltestbutton.clicked.connect(self.next_screen)
        self.testbutton1.clicked.connect(self.timer1)
        self.testbutton2.clicked.connect(self.timer2)
        self.testbutton3.clicked.connect(self.timer3)

    def next_screen(self):
        data = Data(int(self.hintkage.text()), int(self.hinttest1.text()), int(self.hinttest2.text()), int(self.hinttest3.text()))
        self.screen3 = ThirdScreen(data)
        self.hide()
    
    def timer_event(self):
        global time
        time = time.addSecs(-1)
        self.timer_label.setText(time.toString('hh:mm:ss'))
        self.timer_label.setFont(QFont('Times', 36, QFont.Bold))
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()

class Data():
    def __init__(self, age, pulse1, pulse2, pulse3):
        self.age = age
        self.pulse1 = pulse1
        self.pulse2 = pulse2
        self.pulse3 = pulse3
    

