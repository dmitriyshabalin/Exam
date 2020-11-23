# Подключает вспомогательные модули
import sys
import time
import itertools


# Импортируем интерфейса
from guess import *
from PyQt5 import QtCore, QtGui, QtWidgets

# Главный класс
class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow() # Подключается к графическому интерфейсу
        self.ui.setupUi(self) # Запускает графический интерфейс
        
        self.ui.comboBox.setCurrentIndex(0) # Задает выбранный элемент в комбо боксе
        self.ui.comboBox.addItems(["3", "4"]) # Задает варианты в комбо бокс
        

        # Задается событие по нажатию на кнопку       
        self.ui.pushButton.clicked.connect(self.start1)


    # Функция при нажатии на кнопку
    def start1(self):
        # Проверяет выбранный тип поиска
        if self.ui.comboBox.currentIndex() == 0:
            self.FindWord(3)
        elif self.ui.comboBox.currentIndex() == 1:
            self.FindWord(4)

    # Функция поиска слов
    def FindWord(self, count):
        # Открывает файл исходя из выбранного колличества символов
        if count == 3:
            f = open("3.txt",'r').read().split(" ")
        if count == 4:
            f = open("4.txt",'r').read().split(" ")
            
        print(f)
        self.t1 = time.time() # Сохраняет начало выполнения поиска

        word = self.ui.lineEdit.text() # Считывает введенное слово из лайн эдита
        print(word)

        # Создает список из всевозможных комбинаций символов
        massVariable = list(map("".join, itertools.permutations(word)))

        print(massVariable)
        finding = [] # Найденные варианты конфигурации

        # Идет по всем считынм словам из файла
        for i in f:
            # Если текущее слово  из файла найденно в списке комбинаций символов, то оно записывает в словарь найденных слов
            if i in massVariable:
                finding.append(i)
                print(f"{i}")

        # Выводит сообщение в текст едит
        self.ui.plainTextEdit.appendPlainText("Найденно " + str(len(finding)) + " слова.") # Выводит колличество совподений
        self.ui.plainTextEdit.appendPlainText("такие слова как " + str(finding)) # Выводит все слова которые можно было составить из введенного текста
        self.ui.plainTextEdit.appendPlainText("за " + str(time.time()-self.t1)) # Расчитывает разницу во времени
        self.ui.plainTextEdit.appendPlainText("\n")


# Запускает основной класс
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
