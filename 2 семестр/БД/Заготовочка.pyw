import sys
# Импортируем наш интерфейс из файла
from menu import *
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


from PyQt5.QtWidgets import QTableWidgetItem as QWT

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
       
        self.ui.action.triggered.connect(self.insBD)

        self.ui.action_2.triggered.connect(self.insRow)
        
        self.ui.action_6.triggered.connect(self.Savee)

        self.ui.action_5.triggered.connect(self.close)        

        self.ui.tableWidget.setEnabled(False)

    # при нажатии на кнопку
    def insBD(self):
        #! BD

        global flag
        flag = 1

        connection = sqlite3.connect('sqlite_bd.db')

        cursor = connection.cursor()

        cursor.execute('SELECT * FROM Pacient')

        results = cursor.fetchall()

        k = results

        self.insTb(k,self.ui.tableWidget)

        connection.commit()

        connection.close()
     

    def insTb(self,k,tbl):  #Функция заполнения таблицы
            tbl.setRowCount(len(k))
            tbl.setColumnCount(len(k[0]))
            for j in range(len(k)):
                for i in range(len(k[0])):
                    tbl.setItem(j, i, QWT(str(k[j][i])))


    def insRow(self):
        if flag == 0:

            self.ui.tableWidget.setEnabled(True)

            connection = sqlite3.connect('sqlite_bd.db')

            cursor = connection.cursor()

            cursor.execute('SELECT * FROM Pacient')

            results = cursor.fetchall()

            k = results

            self.insTb(k,self.ui.tableWidget)

            connection.commit()

            connection.close()

            self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())

        else:
        
            self.ui.tableWidget.setEnabled(True)

            self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())

            

    def Savee(self):

        global q
        q += 1
        
        self.ui.tableWidget.setEnabled(True)

        a = []
        colCount = self.ui.tableWidget.columnCount()
        print(q)
        for k in range(colCount):
            col = self.ui.tableWidget.item(q,k).text()
            a.append(col)
        print(a)

        #self.ui.tableWidget.setItem(self.ui.tableWidget.currentRow(),q,QWT(str(col))) #! Запись информации 
        #self.ui.tableWidget.setItem(self.ui.tableWidget.currentRow(),1,TWI(str(self.ui.lineEdit_2.text())))

        #cursor.execute('INSERT INTO sqlite_bd.db VALUES ("Иванов И.И.", "ПКС", 182.5, 12, 12, 12, 12)' )

global flag, q
flag = 0

q = 9

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
