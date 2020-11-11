import sys
import os
# Импортируем наш интерфейс из файла
from interface import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem as QWT
from PyQt5.QtWidgets import QMessageBox
from random import randint as rd

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.tableWidget.setEnabled(False)
        # self.ui.tableWidget.resizeColumnsToContents()

        # Здесь прописываем событие нажатия на кнопку

        self.ui.pushButton.clicked.connect(self.MyFunction)
        self.ui.pushButton_2.clicked.connect(self.Ruch)
        self.ui.pushButton_3.clicked.connect(self.Rund)
        self.ui.pushButton_5.clicked.connect(self.sort)

        # Кнопки меню
        self.ui.actionAbout_the_program.triggered.connect(self.Prog)
        self.ui.actionAbout_the_author.triggered.connect(self.Aut)

        self.ui.actionEnter_manually.triggered.connect(self.Ruch)
        self.ui.actionRandomly.triggered.connect(self.MyFunction)
        self.ui.actionRandomly_2.triggered.connect(self.Rund)

        self.ui.actionBlock_diagram.triggered.connect(self.Dia)

        self.ui.action_2.triggered.connect(self.LangR)
        self.ui.actionEnglish.triggered.connect(self.LangE)

        self.ui.actionInstruction_manual.triggered.connect(self.Instr)
        
        self.ui.actionExit.triggered.connect(self.close)

    
    def sort(self):  #Функция сортировки строки
        a = []
        colCount = self.ui.tableWidget.columnCount()
        try:
            for k in range(colCount):
                col = int(self.ui.tableWidget.item(self.ui.comboBox.currentIndex(),k).text())
                a.append(col)
        except:
                if flag == 0:
                    QMessageBox.critical(self, "Error", "The fields are filled in incorrectly!")
                else:
                    QMessageBox.critical(self, "Ошибка", "Поля заполнены неправильно!")
                self.ui.label_4.setText("")
        if len(a) == 5:
            a = sorted(a)
            a.reverse()    
            self.ui.label_4.setText(str(a))
            if flag == 0:
                self.ui.label_4.move(100,380)
            else:
                self.ui.label_4.move(170,380)
            
    
    def insTb(self,k,tbl):  #Функция заполнения таблицы
        tbl.setRowCount(len(k))
        tbl.setColumnCount(len(k[0]))
        for j in range(len(k)):
            for i in range(len(k[0])):
                tbl.setItem(j, i, QWT(str(k[j][i])))

    
    def MyFunction(self):  #Открытие файла
        with open("hh.txt",'r',encoding = 'utf-8') as f:
            k = f.readline()
            k = eval(k)
            self.insTb(k,self.ui.tableWidget)
            

    def Ruch(self):  #Ручной ввод
        if not(self.ui.tableWidget.isEnabled()):
            self.ui.tableWidget.setEnabled(True)
            if flag == 0:
                self.ui.pushButton_2.setText('Close for edit')
                self.ui.actionEnter_manually.setText('Close for edit')
            else:
                self.ui.pushButton_2.setText("Отмена")
                self.ui.actionEnter_manually.setText('Отмена')
        else:
            self.ui.tableWidget.setEnabled(False)
            if flag == 0:
                self.ui.pushButton_2.setText('Enter manually')
                self.ui.actionEnter_manually.setText('Enter manually')
            else:
                self.ui.pushButton_2.setText("Ввести вручную")
                self.ui.actionEnter_manually.setText("Ввести вручную")

    def Rund(self): #Задать случайным образом
        k = [[rd(10,50) for i in range(5)] for j in range(5)]
        self.insTb(k,self.ui.tableWidget)

    def Dia(self):   #Вывод блок схемы
        os.startfile('bs.png')

    def LangR(self):  #Русский язык
        self.ui.tableWidget.setEnabled(False)
        
        global flag
        flag = 1
        
        self.ui.pushButton.setText("Считать из файла")
        self.ui.pushButton_2.setText("Ввести вручную")
        self.ui.pushButton_3.setText("Случайно")
        self.ui.label.setText("Выберите способ заполнения матрицы:")
        self.ui.label_2.setText("Сортировать:")
        self.ui.label_3.setText("Отсортированная строка:")
        self.ui.pushButton_5.setText("Ок")
        self.ui.menuMenu.setTitle("Меню")
        self.ui.menuOption.setTitle("Опции")
        self.ui.menuLanguages.setTitle("Языки")
        self.ui.actionAbout_the_author.setText("Об авторе")
        self.ui.actionAbout_the_program.setText("О программе")
        self.ui.actionExit.setText("Выход")
        self.ui.actionRandomly.setText("Считать из файла")
        self.ui.actionEnter_manually.setText("Ввести вручную")
        self.ui.actionRandomly_2.setText("Случайно")
        self.ui.actionBlock_diagram.setText("Блок-схема")
        self.ui.action_2.setText("Русский")
        self.ui.actionEnglish.setText("English")
        self.ui.actionInstruction_manual.setText("Инструкция")

        self.ui.label_4.move(170,380)
        self.ui.label.move(170,0)

    def LangE(self):  #Английский язык
        self.ui.tableWidget.setEnabled(False)
        
        global flag
        flag = 0
        
        self.ui.pushButton.setText("Read from file")
        self.ui.pushButton_2.setText("Enter manually")
        self.ui.pushButton_3.setText("Accidentally")
        self.ui.label.setText("Choose a matrix filling method:")
        self.ui.label_2.setText("Select row:")
        self.ui.label_3.setText("Sorted string:")
        self.ui.pushButton_5.setText("Let\'s sort")
        self.ui.menuMenu.setTitle("Menu")
        self.ui.menuOption.setTitle("Option")
        self.ui.menuLanguages.setTitle("Languages")
        self.ui.actionAbout_the_author.setText("About the author")
        self.ui.actionAbout_the_program.setText("About the program")
        self.ui.actionExit.setText("Exit")
        self.ui.actionRandomly.setText("Read from file")
        self.ui.actionEnter_manually.setText("Enter manually")
        self.ui.actionRandomly_2.setText("Accidentally")
        self.ui.actionBlock_diagram.setText("Block diagram")
        self.ui.action_2.setText("Русский")
        self.ui.actionEnglish.setText("English")
        self.ui.actionInstruction_manual.setText("Instruction manual")

        self.ui.label_4.move(100,380)
        self.ui.label.move(210,0)
        


    #! Функции для открытия сообщений
        
    def  Prog(self): #О программе
        if  flag == 0:
            QMessageBox.about(self, "About the program", "This program allows you to sort the matrix row at the user's choice." )
        else:
            QMessageBox.about(self, "О программе", "Эта программа позволяет сортировать строки матрицы по выбору пользователя." )

    def  Aut(self):  #Об авторе
        if flag == 0:
            QMessageBox.about(self, "About the author", "The program was developed by a cadet of 331 group of Troitsk Aviation Technical College, a branch of Moscow State Technical University of Civil Aviation of Russia\nShabalin Dmitry Alekseevich")
            self.ui.statusbar.showMessage('Dmitry Shabalin')
        else:
            QMessageBox.about(self, "Об авторе", "Программа была разработана курсантом 331 группы Троицкого авиационного технического колледжа, филиала Московского государственного технического университета гражданской авиации России\nШабалин Дмитрий Алексеевич")
            self.ui.statusbar.showMessage('Дмитрий Шабалин')

    def Instr(self):  #Инструкция к программе
        if flag == 0:
            QMessageBox.about(self, "Instruction manual", "The main window of the program contains a table filled with elements. There are three ways to set a table: read from a file, enter it manually, or fill it in randomly. Next you need to select the row you want to sort. And after all the manipulations are performed, click on the 'Let\'s sort' button. The program has two different interface languages, which can be changed in the options menu. You can also view the flowchart of the program by clicking on the corresponding button in the menu." )
        else:
            QMessageBox.about(self, "Инструкция", "На главном окне программы расположена таблица, которая заполнена элементами. Таблицу можно задать тремя способами: считать из файла, ввести вручную или заполнить случайным образом. Далее нужно выбрать строку, которую следует отсортировать. И после того как все манипуляции проведены нажмите на кнопку 'Ок'. Программа имеет два различных языка интерфейса, изменить которые можно в меню опций. Также вы можете просмотреть блок схему программы нажав на соответствующую кнопку в меню.")

    def closeEvent(self,e): #Событие выхода через диалог
        if flag == 0:
            result = QtWidgets.QMessageBox.question(self,"Confirm action",
            "Really quit?",QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
            if result == QtWidgets.QMessageBox.Yes:
                e.accept()
            else:
                e.ignore()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            # msg.setIconPixmap(pixmap)  # Своя картинка
              
            msg.setWindowTitle("Подтвердите действие")
            msg.setText("Вы действительно хотите выйти?")
            
            '''msg.setInformativeText("InformativeText")
            msg.setDetailedText("DetailedText")'''
              
            okButton = msg.addButton('Да', QMessageBox.AcceptRole)
            msg.addButton('Нет', QMessageBox.RejectRole)
              
            msg.exec()
            if msg.clickedButton() == okButton:
                e.accept()
            else:
                e.ignore()
            

global flag
flag = 0

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
