import sys
import time
# Импортируем наш интерфейс из файла
from guess import *
from PyQt5 import QtCore, QtGui, QtWidgets


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.comboBox.setCurrentIndex(0) 
        self.ui.comboBox.addItems('4 5'.split())
        
        self.ui.statusbar.showMessage ('Шабалин Дмитрий Алексеевич')
        

        # Здесь прописываем событие нажатия на кнопку        
        self.ui.pushButton.clicked.connect(self.start1)
        self.ui.pushButton2.clicked.connect(self.save)


    # функция которая выполняется
    # при нажатии на кнопку
    def start1(self):
        if self.ui.comboBox.currentIndex() == 0:
            self.wordFour(self.ui.lineEdit.text())
        elif self.ui.comboBox.currentIndex() == 1:
            self.wordFive(self.ui.lineEdit.text())
    
    def wordFour(self,letters):

        self.t1 = time.time()
        self.c = 0
        self.resArr = []
        self.initW = letters
        self.res = ["","","",""]
        self.r = open("dict.txt",'r')

        self.fileRead = self.r.read()
        self.fileSplit = self.fileRead.split()
        self.r.close()

        for self.i in range(0,len(self.initW)):
            self.res[0] = self.initW[self.i]

            for self.q in range(0, len(self.initW)):
                if (self.q != self.i):
                    self.res[1] = self.initW[self.q]

                    for self.p in range(0, len(self.initW)):
                        if (self.p != self.i) and (self.p != self.q):
                            self.res[2] = self.initW[self.p]

                            for self.pp in range(0, len(self.initW)):
                                if (self.pp != self.i) and (self.pp != self.q) and(self.pp != self.p):
                                    self.res[3] = self.initW[self.pp]
                                    self.wordFor = self.res[0]+self.res[1]+self.res[2]+self.res[3]
                                    if self.wordFor in self.fileSplit:
                                        if self.wordFor not in self.resArr:
                                            self.resArr.append(self.wordFor)

                                    self.c += 1
        self.str = "Найдено совпадений:" +str(len(self.resArr))+"\n"+self.arrOutput(self.resArr)+"\n"+str(self.c)+"комбинаций проверено \nВремя исполнения:" +str(time.time()-self.t1)+"c."
        self.ui.plainTextEdit.appendPlainText(self.str)
        self.ui.pushButton.setEnabled(True)                      
                                    
                        
        
   
    def wordFive(self,letters):

        self.t1 = time.time()
        self.c = 0
        self.resArr = []
        self.initW = letters
        self.res = ["","","","",""]
        self.r = open("dict.txt",'r')

        self.fileRead = self.r.read()
        self.fileSplit = self.fileRead.split()
        self.r.close()

        for self.i in range(0,len(self.initW)):
            self.res[0] = self.initW[self.i]

            for self.q in range(0, len(self.initW)):
                if (self.q != self.i):
                    self.res[1] = self.initW[self.q]

                    for self.p in range(0, len(self.initW)):
                        if (self.p != self.i) and (self.p != self.q):
                            self.res[2] = self.initW[self.p]


                            for self.pp in range(0, len(self.initW)):
                                if (self.pp != self.i) and (self.pp != self.q) and(self.pp != self.p):
                                    self.res[3] = self.initW[self.pp]

                                    for self.kp in range(0, len(self.initW)):
                                        if (self.kp != self.i) and (self.kp != self.q) and (self.kp != self.p) and (self.kp != self.pp):
                                            self.res[4] = self.initW[self.kp]
                                            self.wordFive = self.res[0]+self.res[1]+self.res[2]+self.res[3]+self.res[4]
                                            if self.wordFive in self.fileSplit:
                                                if self.wordFive not in self.resArr:
                                                    self.resArr.append(self.wordFive)
                                                                                       

                                    self.c += 1

        self.str = "Найдено совпадений:" +str(len(self.resArr))+"\n"+self.arrOutput(self.resArr)+"\n"+str(self.c)+"комбинаций проверено \nВремя исполнения:" +str(time.time()-self.t1)+"c."
        self.ui.plainTextEdit.appendPlainText(self.str)
        self.ui.pushButton.setEnabled(True)


    def arrOutput(self,arr):
        arr.sort()
        self.str = ''
        for i in range(0, len(arr)):
            if i != len(arr) -1:
                self.str += arr[i]+', '
            else:
                self.str += arr[i]+'. '
        return self.str

    def save(self):
        a = open("text.txt","w")
        a.write(self.str)
        a.close()  

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
