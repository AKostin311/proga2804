from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit
from PyQt5.QtCore import Qt

from instr import *

class ThirdScreen(QWidget):

    def __init__(self, data):
        super().__init__()
        self.age = data.age
        self.pulse1 = data.pulse1
        self.pulse2 = data.pulse2
        self.pulse3 = data.pulse3
        self.indexruf = (4 * (self.pulse1 + self.pulse2 + self.pulse3) - 200) / 10
        self.result = self.get_result()
        self.setup_screen()
        self.setup_ui()

    def setup_screen(self):
        self.setWindowTitle(screen_title)
        self.resize(win_width, win_height)
        self.show()
    
    def setup_ui(self):
        
        main_line = QVBoxLayout()
        
        index = QLabel(txt_index + str(self.indexruf))
        main_line.addWidget(index, alignment=Qt.AlignCenter)

        workheart = QLabel(txt_workheart + str(self.result))
        main_line.addWidget(workheart, alignment=Qt.AlignCenter)
        
        self.setLayout(main_line)

    def get_result(self):
        if self.age >= 15:
            if self.indexruf >= 15:
                return 'низкая'
            elif 11 <= self.indexruf <= 14.9:
                return 'удовлетворительная'
            elif 6 <= self.indexruf <= 10.9:
                return 'средняя'
            elif 0.5 <= self.indexruf <= 5.9:
                return 'выше среднего'
            elif self.indexruf <= 0.4:
                return 'высокая'
        elif 13 <= self.age <= 14:
            if self.indexruf >= 16.5:
                return 'низкая'
            elif 12.5 <= self.indexruf <= 16.4:
                return 'удовлетворительная'
            elif 7.5 <= self.indexruf <= 12.4:
                return 'средняя'
            elif 2 <= self.indexruf <= 7.4:
                return 'выше среднего'
            elif self.indexruf <= 1.9:
                return 'высокая'
        elif 11 <= self.age <= 12:
            if self.indexruf >= 18:
                return 'низкая'
            elif 14 <= self.indexruf <= 17.9:
                return 'удовлетворительная'
            elif 9 <= self.indexruf <= 13.9:
                return 'средняя'
            elif 3.5 <= self.indexruf <= 8.9:
                return 'выше среднего'
            elif self.indexruf <= 3.4:
                return 'высокая'
        elif 9 <= self.age <= 10:
            if self.indexruf >= 19.5:
                return 'низкая'
            elif 15.5 <= self.indexruf <= 19.4:
                return 'удовлетворительная'
            elif 10.5 <= self.indexruf <= 15.4:
                return 'средняя'
            elif 5 <= self.indexruf <= 10.4:
                return 'выше среднего'
            elif self.indexruf <= 4.9:
                return 'высокая'
        elif 7 <= self.age <= 8:
            if self.indexruf >= 21:
                return 'низкая'
            elif 17 <= self.indexruf <= 20.9:
                return 'удовлетворительная'
            elif 12 <= self.indexruf <= 16.9:
                return 'средняя'
            elif 6.5 <= self.indexruf <= 11.9:
                return 'выше среднего'
            elif self.indexruf <= 6.4:
                return 'высокая'
