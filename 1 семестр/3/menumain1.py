import sys
import os
from subprocess import Popen as Opn
# Импортируем наш интерфейс из файла
from menu import *
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QAction, QFileDialog, QApplication, QFontDialog)
from PyQt5.QtGui import QIcon
global a
a = 123

class MyWin(QtWidgets.QMainWindow):
    global a
    
    def __init__(self, parent=None):
        global a
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.actionExit.triggered.connect(self.close)

        self.ui.actionSave.triggered.connect(self.saveToFile)
        
        self.ui.actionOpen.triggered.connect(self.showDialog)
        
        self.ui.actionFont.triggered.connect(self.ChgFnt)

        self.ui.Open_test.triggered.connect(self.opnTst)
        
    def opnTst(self):
        self.ui.hide()
        os.system("Test\learnmain1.pyw")
        pass

    
    def closeEvent(self,e):
        pass

    def saveToFile(self):
        res = QtWidgets.QMessageBox.question(self,"Confirm Dialog",
        "Save text before quit?",QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No|QtWidgets.QMessageBox.Cancel,QtWidgets.QMessageBox.No)
        if res == QtWidgets.QMessageBox.Yes:
            options = QtWidgets.QFileDialog.Options()
            self.fileName, _= QtWidgets.QFileDialog.getSaveFileName(self,'Save To File','','Text Files(*.html)',options=options)
            if self.fileName:
                self.writeFile = open(self.fileName, 'w', encoding='utf-8')
            self.writeFile.write(self.ui.TextEdit.toHtml())  
            self.writeFile.close()
            self.ui.statusbar.showMessage('Save to %s' %self.fileName)
        else:
            e.ignore()

    def showDialog(self):
        fil = QFileDialog.getOpenFileName(self, 'Open', '/menul')[0]
        f = open(fil, 'r',encoding='utf-8')
        
        with f:
            data = f.read()
            self.ui.TextEdit.setText(data)


    def ChgFnt(self):
        b = QFontDialog.getFont()[0].toString().split(',')
        c = 'font: ' + b[4] + ' ' + b[1] + 'pt ' + '"' + b[0] + '";'
        #self.setStyleSheet(c)
        self.ui.TextEdit.setStyleSheet(c)
                


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())

    
