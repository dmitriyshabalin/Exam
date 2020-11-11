import sys
from Pac import *
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QTableWidgetItem as QWT


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.s=0
        self.ui.pushButton.clicked.connect(self.Podkl)
        self.ui.pushButton_2.clicked.connect(self.dell)
        self.ui.pushButton_3.clicked.connect(self.addPAC)
        self.ui.pushButton_77.clicked.connect(self.close)

        self.ui.tableWidget.resizeColumnsToContents()
        self.ui.tableWidget.resizeRowsToContents()
        
    def Podkl(self):
        
        connection = sqlite3.connect('IND.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM Pac')
        results = cursor.fetchall()
        k = results
        self.insTb(k,self.ui.tableWidget)
        connection.commit()
        connection.close()
        
        
    def insTb(self,k,tbl):  #Функция заполнения таблицы
        
        a=self.ui.lineEdit.text()

        if self.ui.radioButton.isChecked()==True:
            s=0
            for i in range (len(k)):
                if str(k[s][0]) == str(a):
                    tbl.setRowCount(1)
                    tbl.setColumnCount(7)
                    for j in range(1):
                        for i in range(len(k[i])):
                            tbl.setItem(j, i, QWT(str(k[s][i])))
            
                s+=1
        if self.ui.radioButton_2.isChecked()==True:
            s=0
            ss=0
            d=[]
            for i in range (len(k)):
                if str(a) in str(k[s][2]):
                    d.append(k[s])
                    
                s+=1
            s=0
            tbl.setRowCount(len(d))
            tbl.setColumnCount(7)
            for j in range(len(d)):
                    for i in range(len(d[j])):
                        tbl.setItem(j, i, QWT(str(d[j][i])))
                        
        if self.ui.radioButton_3.isChecked()==True:
            s=0
            ss=0
            d=[]
            for i in range (len(k)):
                if str(a) in str(k[s][6]):
                    d.append(k[s])
                    
                s+=1
            s=0
            tbl.setRowCount(len(d))
            tbl.setColumnCount(7)
            for j in range(len(d)):
                    for i in range(len(d[j])):
                        tbl.setItem(j, i, QWT(str(d[j][i])))
                        
        if self.ui.radioButton_4.isChecked()==True:
            
            tbl.setRowCount(len(k))
            tbl.setColumnCount(len(k[0]))
            for j in range(len(k)):
                for i in range(len(k[0])):
                    tbl.setItem(j, i, QWT(str(k[j][i])))
           
        if self.s>0:
            
            tbl.setRowCount(len(k))
            tbl.setColumnCount(len(k[0]))
            for j in range(len(k)):
                for i in range(len(k[0])):
                    tbl.setItem(j, i, QWT(str(k[j][i])))
        self.s=0

        self.ui.tableWidget.resizeColumnsToContents()
        self.ui.tableWidget.resizeRowsToContents()


    def addPAC(self): #Добавление в БД
        self.s+=1
        connection = sqlite3.connect('IND.db')
        cursor = connection.cursor()
        a=[]
        a.append(self.ui.lineEdit_2.text())
        a.append(self.ui.lineEdit_3.text())
        a.append(self.ui.lineEdit_4.text())
        a.append(self.ui.lineEdit_5.text())
        a.append(self.ui.lineEdit_6.text())
        a.append(self.ui.lineEdit_7.text())
        a.append(self.ui.lineEdit_8.text())
        a=tuple(a)

        cursor.execute('INSERT INTO Pac VALUES(?,?,?,?,?,?,?)',a)

        connection.commit()
        connection.close()
        self.Podkl()

#Удаление записи в БД
        
    def dell(self): 
        self.s+=1
        connection = sqlite3.connect('IND.db')
        cursor = connection.cursor()
        self.dell2(cursor)
        connection.commit()
        cursor.close()
        connection.close()
        self.Podkl()
        
    def dell2(self,cursor):
        text=self.ui.lineEdit.text()
        if self.ui.radioButton.isChecked()==True:
            cursor.execute ('DELETE FROM Pac WHERE Фамилия=?',(text,))
        if self.ui.radioButton_2.isChecked()==True:
            cursor.execute ('DELETE FROM Pac WHERE Диагноз=?',(text,))
        if self.ui.radioButton_3.isChecked()==True:
            cursor.execute ('DELETE FROM Pac WHERE Дата_рождения=?',(text,))
        
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())

