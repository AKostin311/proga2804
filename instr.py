
win_x, win_y = 200, 100
win_width, win_height = 1000, 600
screen_title = 'MyApp'


txt_hello = 'Добро пожаловать в программу по определению состояния здоровья!'
txt_next = ''
txt_instruction = 'Данное приложение позволит вам с помощью теста Руфье провести первичную диагностику вашего здоровья\n Проба Руфье представляет собой нагрузочный комплекс, предназначенный для, оценки работоспособности сердца при физической нагрузке.\n У испытуемого, находящегося в положении лежа на спине в течении 5 мин, определяют частоту пульса за 15 секунд; ' 
txt_title = ''
txt_name = 'Введите ФИО:'
txt_hintname = "Иванов Иван Иванович"
txt_kage = 'Полных лет:'
txt_hintkage = "99"
txt_guide1 = 'Лягте на спину и замерьте пульс на 15 секунд. Нажмите кнопку "Начать первый тест", чтобы запустить таймер. Результат запишите в соответствующее поле.'
txt_guide2 = 'Выполните 30 приседаний за 45 секунд. Для этого нажмите кнопку "Начать делать приседания", чтобы запустить счётчик приседаний.'
txt_guide3 = 'Лягте на спину и замерьте пульс сначала за первые 15 секунд минуты, затем за последние 15 секунд.\n Нажмите кнопку начать финальный тест, чтобы запустить таймер.\n Зелёным обозначены секунды, в течение которых необходимо проводить измерения,\n черным - минуты без замера пульсаций. Результаты запишите в соответствующие поля.'
txt_sendresults = ''
txt_hinttest1 = '0'
txt_hinttest2 = '0'
txt_hinttest3 = '0'

txt_age = ''
txt_finalwin = ''
txt_index = 'Индекс Руфье:'
txt_workheart = 'Работоспособность сердца:'




 
# import random

# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
# from PyQt5.QtCore import Qt

# # def change_text():
# #     text1.setText(str(random.randint(1, 100)))
# #     text2.setText(str(random.random()))

# app = QApplication([])

# screen = QWidget()
# screen.setWindowTitle('Испытай удачу, друг!')
# screen.resize(800, 600)
# screen.show()

# main_line = QVBoxLayout()

# h_line1 = QHBoxLayout()
# h_line2 = QHBoxLayout()
# h_line3 = QHBoxLayout()

# # text1 = QLabel('Пример текста 1')
# # main_line.addWidget(text1, alignment=Qt.AlignCenter)

# # text2 = QLabel('Пример текста 2')
# # main_line.addWidget(text2, alignment=Qt.AlignCenter)

# button1 = QPushButton('1')
# h_line1.addWidget(button1, alignment=Qt.AlignLeft)

# button2 = QPushButton('2')
# h_line1.addWidget(button2, alignment=Qt.AlignRight)

# button3 = QPushButton('3')
# h_line2.addWidget(button3, alignment=Qt.AlignCenter)

# button4 = QPushButton('4')
# h_line3.addWidget(button4, alignment=Qt.AlignLeft)

# button5 = QPushButton('5')
# h_line3.addWidget(button5, alignment=Qt.AlignRight)

# main_line.addLayout(h_line1)
# main_line.addLayout(h_line2)
# main_line.addLayout(h_line3)

# screen.setLayout(main_line)

# app.exec_()