import sys

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
        ### self.ui.tableWidget.resizeColumnsToContents()

        # Здесь прописываем событие нажатия на кнопку        
        self.ui.pushButton_4.clicked.connect(self.close)

        self.ui.pushButton.clicked.connect(self.MyFunction)
        self.ui.pushButton_2.clicked.connect(self.Ruch)
        self.ui.pushButton_3.clicked.connect(self.Rund)
        self.ui.pushButton_5.clicked.connect(self.sort)

        # Кнопки меню
        self.ui.actionAbout_the_program.triggered.connect(self.clickMethod)
        self.ui.actionAbout_the_author.triggered.connect(self.clickMethod_2)
        
        self.ui.actionExit.triggered.connect(self.close)

        # 
    
    def sort(self):
        a = []
        q = 0
        colCount = self.ui.tableWidget.columnCount()
        if self.ui.comboBox.currentIndex() == 0:
            for k in range(colCount):
                try:
                    col = int(self.ui.tableWidget.item(0,k).text())
                    a.append(col)
                except:
                    pass
            for i in a:
                q = q + i
            self.ui.label_4.setText(str(q))

        if self.ui.comboBox.currentIndex() == 1:
            for k in range(colCount):
                try:
                    col = int(self.ui.tableWidget.item(1,k).text())
                    a.append(col)
                except:
                    pass
            for i in a:
                q = q + i
            self.ui.label_4.setText(str(q))

        if self.ui.comboBox.currentIndex() == 2:
            for k in range(colCount):
                try:
                    col = int(self.ui.tableWidget.item(2,k).text())
                    a.append(col)
                except:
                    pass
            for i in a:
                q = q + i    
            self.ui.label_4.setText(str(q))

        if self.ui.comboBox.currentIndex() == 3:
            for k in range(colCount):
                try:
                    col = int(self.ui.tableWidget.item(3,k).text())
                    a.append(col)
                except:
                    pass
            for i in a:
                q = q + i    
            self.ui.label_4.setText(str(q))

        if self.ui.comboBox.currentIndex() == 4:
            for k in range(colCount):
                try:
                    col = int(self.ui.tableWidget.item(4,k).text())
                    a.append(col)
                except:
                    pass
            for i in a:
                q = q + i    
            self.ui.label_4.setText(str(q))
    
    def insTb(self,k,tbl):
        tbl.setRowCount(len(k))
        tbl.setColumnCount(len(k[0]))
        for j in range(len(k)):
            for i in range(len(k[0])):
                tbl.setItem(j, i, QWT(str(k[j][i])))

    
    def MyFunction(self):
        with open("Matrix.txt",'r',encoding = 'utf-8') as f:
            k = f.readline()
            k = eval(k)
            self.insTb(k,self.ui.tableWidget)
            

    def Ruch(self):
        if not(self.ui.tableWidget.isEnabled()):
            self.ui.tableWidget.setEnabled(True)
            self.ui.pushButton_2.setText('Close for edit')
        else:
            self.ui.tableWidget.setEnabled(False)
            self.ui.pushButton_2.setText('Enter manually')

    def Rund(self):
        k = [[rd(10,50) for i in range(6)] for i in range(5)]
        self.insTb(k,self.ui.tableWidget)

        

    #! Функции для открытия сообщений
    def  clickMethod(self): 
         QMessageBox.about(self, "About the program", "This program allows you to sort the matrix row at the user's choice." )

    def  clickMethod_2(self):
         QMessageBox.about(self, "About the author", "The program was developed by a cadet of 331 group of Troitsk Aviation Technical College, a branch of Moscow State Technical University of Civil Aviation of Russia\nShabalin Dmitry Alekseevich")
         self.ui.statusbar.showMessage('Dmitry Shabalin')

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
