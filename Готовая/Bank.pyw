import sys
from menu import * #! Импортируем интерфейс
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem as TWI

from PyQt5.QtWidgets import QMessageBox

import matplotlib.pyplot as plt
import numpy as np
import os


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Здесь прописываем событие нажатия на кнопки       
        self.ui.pushButton.clicked.connect(self.MyFunction)
        
        self.ui.pushButton_2.clicked.connect(self.MyFunction_2)
        
        self.ui.pushButton_3.clicked.connect(self.changeRow)
        
        self.ui.pushButton_4.clicked.connect(self.cancelChange)
        
        self.ui.tableWidget.itemChanged.connect(self.res)
        self.res()
        
        self.ui.pushButton_5.clicked.connect(self.diagramm)
        
        self.ui.pushButton_6.clicked.connect(self.close)
        
        self.ui.action_4.triggered.connect(self.close) #! Событие выхода через меню

        self.ui.action_6.triggered.connect(self.clickMethod)
        self.ui.action_7.triggered.connect(self.clickMethod_2)

        self.ui.action_3.triggered.connect(self.MyFunction)

        self.ui.action_9.triggered.connect(self.MyFunction_2)

        #self.ui.action_11.triggered.connect(self.obnov)

        self.ui.action_13.triggered.connect(self.diagramm)
        
        self.ui.statusbar.showMessage ('Шабалин Дмитрий Алексеевич')
            
    def MyFunction(self): #! Функция для добавления новой строки
        self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())
        
    def MyFunction_2(self): #! Переход в другое окно программы
        self.ui.stackedWidget.setCurrentIndex(1)

    def changeRow(self): #! Кнопка сохранения
        
        self.ui.tableWidget.setItem(self.ui.tableWidget.currentRow(),0,TWI(str(self.ui.lineEdit.text()))) #! Запись информации 
        self.ui.tableWidget.setItem(self.ui.tableWidget.currentRow(),1,TWI(str(self.ui.lineEdit_2.text())))
        
        #! Считывание информации из comboBox 
        if self.ui.comboBox.currentIndex() == 0:
            self.ui.tableWidget.setItem(self.ui.tableWidget.currentRow(),2,TWI(str('15%')))
        elif self.ui.comboBox.currentIndex() == 1:
            self.ui.tableWidget.setItem(self.ui.tableWidget.currentRow(),2,TWI(str('25%')))
        elif self.ui.comboBox.currentIndex() == 2:
            self.ui.tableWidget.setItem(self.ui.tableWidget.currentRow(),2,TWI(str('30%')))
        self.ui.tableWidget.setItem(self.ui.tableWidget.currentRow(),3,TWI(str(self.ui.lineEdit_3.text())))
        
        self.ui.stackedWidget.setCurrentIndex(0) #! Переход в главное окно
    
        
        #! Обновление информации и подсчет
        rowCount = self.ui.tableWidget.rowCount()
        global vvv
        vvv = []
        my_file = open('snake.txt', 'w')
        for k in range(rowCount):
            try:
                vklad = int(self.ui.tableWidget.item(k,3).text())
                proc = int(self.ui.tableWidget.item(k,2).text()[:-1])
                vvv.append(proc)
                self.ui.tableWidget.setItem(k,4,TWI(str(vklad * proc / 100)))
                self.ui.tableWidget.setItem(k,5,TWI(str(vklad + float(self.ui.tableWidget.item(k,4).text()))))
                ###
                
                my_file = open('snake.txt', 'a')

                text_for_file = str(vklad)
                my_file.write('Размер вклада: ')
                my_file.write(text_for_file)
                my_file.write('\n')
     
                my_file.close()
            except:
                pass
    def cancelChange(self): #! Отмена
        self.ui.stackedWidget.setCurrentIndex(0)

    def res(self): #! Функция для правильного отображения
        self.ui.tableWidget.resizeColumnsToContents()
        self.ui.tableWidget.resizeRowsToContents()
        

    '''def obnov(self): #! При самостоятельном вводе
        rowCount = self.ui.tableWidget.rowCount()
        for k in range(rowCount):
            try:
                vklad = int(self.ui.tableWidget.item(k,3).text())
                proc = int(self.ui.tableWidget.item(k,2).text()[:-1])
                self.ui.tableWidget.setItem(k,4,TWI(str(vklad * proc / 100)))
                self.ui.tableWidget.setItem(k,5,TWI(str(vklad + float(self.ui.tableWidget.item(k,4).text()))))
            except:
                pass'''


    def diagramm(self): #! Диаграмма
        try:
            pya = 0
            dva = 0
            tri = 0
            for i in vvv:
                if i == 15:
                    pya += 1
                elif i == 25:
                    dva += 1
                elif i == 30:
                    tri += 1
            q="Срочный"
            w="Обычный"
            e="На детей"

            s = ['one','two','three']
            x = [q, w, e]

            z1 = [dva,pya,tri]

            fig = plt.figure()
            plt.bar(x, z1)
            plt.title('Количество человек\n по типу вклада')
            plt.grid(True)
            plt.show()
        except:
            pass

    #! Функции для открытия сообщений
    def  clickMethod(self): 
         QMessageBox.about(self, "О программе" , "Данная программа позволяет открывать файлы с расширением .txt, менять шрифт, а так же, проходить тест, заранее прописанный разработчиком." )

    def  clickMethod_2(self):
         QMessageBox.about(self, "Об авторе" , "Программу разработал курсант 331 группы Троицкого Авиационного\nТехнического Колледжа - филиала Московского\nГосударственного Технического Университета Гражданской Авиации\nРоссии\nШарыгин Эмиль Андреевич.")
            
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
