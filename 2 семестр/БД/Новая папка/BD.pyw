import sys
# Импортируем наш интерфейс из файла
from intr import *
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QTableWidgetItem as QWT


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Здесь прописываем событие нажатия на кнопку        
        self.ui.pushButton.clicked.connect(self.MyFunction)
        a=self.ui.radioButton_2.isChecked()
        
       
    # Пока пустая функция которая выполняется
    # при нажатии на кнопку
    def MyFunction(self):
        #! BD
        connection = sqlite3.connect('sqlite_bd.db')

        cursor = connection.cursor()

        cursor.execute('SELECT * FROM Pacient')

        results = cursor.fetchall()

        k = results
        
        self.ui.tableWidget.clear()
        self.insTb(k,self.ui.tableWidget)

        #print(results)

        connection.commit()

        connection.close()

    def insTb(self,k,tbl):  #Функция заполнения таблицы
        
        a=self.ui.lineEdit.text()
        
        if self.ui.radioButton.isChecked()==True:
            s=0
            ss=0
            for i in range (len(k)):
    
                if str(k[s][0])==str(a):

                    tbl.setRowCount(1)
                    tbl.setColumnCount(7)
                    for j in range(1):
                        for i in range(len(k[i])):
                            tbl.setItem(j, i, QWT(str(k[s][i])))
                    
                s+=1
       
        if self.ui.radioButton_2.isChecked()==True:
            s=0
            ss=0
            b = []
            for i in range (len(k)):
                if str(a).lower() in str(k[s][2]).lower():
                    b.append(k[s])
                s+=1
            tbl.setRowCount(len(b))
            tbl.setColumnCount(7)
            for j in range(len(b)):
                    for i in range(len(b[j])):
                        tbl.setItem(j, i, QWT(str(b[j][i])))

        if self.ui.radioButton_3.isChecked()==True:
            s=0
            ss=0
            for i in range (len(k)):
                if str(k[s][1])==str(a):
                    tbl.setRowCount(1)
                    tbl.setColumnCount(7)
                    for j in range(1):
                        for i in range(len(k[i])):
                            tbl.setItem(j, i, QWT(str(k[s][i])))
                s+=1

        if self.ui.radioButton_4.isChecked()==True:
            
            tbl.setRowCount(len(k))
            tbl.setColumnCount(len(k[0]))
            for j in range(len(k)):
                for i in range(len(k[0])):
                    tbl.setItem(j, i, QWT(str(k[j][i])))
          
        self.ui.tableWidget.setHorizontalHeaderLabels(['Номер_медполиса',"Номер_участника","ФИО_пациента","Дата_рождения","Пол(мужской)","Диагноз","Дата_посещения"])        

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
