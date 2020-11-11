import sys
from inter import *
from PyQt5 import QtCore, QtGui, QtWidgets
import random 


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
       
        self.ui.pushButton.clicked.connect(self.filling)

        self.ui.tableWidget.verticalHeader().hide()
        self.ui.tableWidget.horizontalHeader().hide()

        self.ui.tableWidget.resizeRowsToContents()

    def filling(self):
        self.ui.listWidget.clear()
        array = sorted([random.randint(0, 6000) for i in range(100)]) 
        for i in array:
            self.ui.listWidget.addItem(str(i))

        interval = array[-1]//10
        print(interval)
        
        '''spis = []
        for i in array:
            if i < 601:
                spis.append(i)
                
        lenspis = len(spis)'''

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
