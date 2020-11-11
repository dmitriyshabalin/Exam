import sys
import random
import os
import xml.dom.minidom
import time

from sh import *
from PyQt5 import QtCore, QtGui, QtWidgets


DEFAULT_STYLE = """
QProgressBar{
    
    
    text-align: center
}

QProgressBar::chunk {
    background-color: grey;
    width: 10px;
    margin: 1px;
}
"""


class MyWin(QtWidgets.QMainWindow):

    lbs = []
    rbs = [['']*10]*15
    bgrs = []
    labels = []
    variants = []
    correct = []

    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        

        self.timer = QtCore.QTimer(self)
        self.mixXml()
        self.readToDom()
        self.verticalLayout = QtWidgets.QVBoxLayout(self.ui.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.addWidgetsToInterface()
        self.timer.timeout.connect(lambda:self.updater(self.timeSeconds))

        self.timer.start(1000)
        
        
        self.progress = QtWidgets.QProgressBar(self)
        self.progress.setGeometry(10, 480, 780, 25)
        self.progress.setMaximum(100)
        self.progress.setStyleSheet(DEFAULT_STYLE)
      
        self.show()
       
        self.ui.pushButton.clicked.connect(self.check)
        

    def mixXml(self):
        self.linesMixed = []
        self.r = open('bd1.xml','r',encoding = 'utf-8')
        self.fileRead = self.r.readlines()
        for line in range(2, len(self.fileRead)-1):
            self.linesMixed.append(self.fileRead[line])
        random.shuffle(self.linesMixed)
        self.r.close()

        self.w = open('temp.xml','w', encoding= 'utf-8')
        self.w.write('''<?xml version= "1.0" encoding="utf-8"?>\n<content>\n''')
        for line in self.linesMixed:
            self.w.write('%s' % line)
        self.w.write('</content>')
        self.w.close()
        

    def readToDom(self):
        self.dom = xml.dom.minidom.parse('temp.xml')
        self.collection = self.dom.documentElement
        self.timeSeconds = int(self.collection.getElementsByTagName("time")[0].childNodes[0].data)
        self.linesArr = self.collection.getElementsByTagName("q")
        for line in range(0, len(self.linesArr)):
            self.labels.append(self.linesArr[line].childNodes[0].data)
            self.variants.append(self.linesArr[line].getAttribute('ans').split('**?**'))
            self.correct.append(self.linesArr[line].getAttribute('cor'))
        for variant in self.variants:

            random.shuffle(variant)

        os.remove('temp.xml')
        

    def addWidgetsToInterface(self):
        for line in range (0, len(self.labels)):
            self.lbs.append(QtWidgets.QLabel(self.ui.scrollAreaWidgetContents))
            self.lbs[line].setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
            self.lbs[line].setText('<b>%s</b>'%self.labels[line])
            self.verticalLayout.addWidget(self.lbs[line])
            self.bgrs.append(QtWidgets.QButtonGroup(self.ui.centralwidget))
            for v in range(0, len(self.variants[line])):
                
                self.rbs[line][v] = QtWidgets.QRadioButton(self.ui.scrollAreaWidgetContents)
                self.bgrs[line].addButton(self.rbs[line][v])
                self.rbs[line][v].setText(self.variants[line][v])
                self.verticalLayout.addWidget(self.rbs[line][v])
        

    def check(self):
        counter = 0
        for group in range (0, len(self.bgrs)):
            for rb in self.bgrs[group].buttons():
                if rb.isChecked():
                    if rb.text() == self.correct[group]:
                        counter +=1
        
        message = "Ваш результат "+"%.2f" %float(counter/len(self.bgrs)*100)+ "%"
        gg = counter/len(self.bgrs)*100
        
        if gg <= 50:
            self.ui.statusbar.setStyleSheet('color: red;font-weight: bold;')
            self.ui.statusbar.showMessage(message)
        elif gg > 50 and gg <= 75:
            self.ui.statusbar.setStyleSheet('color: navy;font-weight: bold;')
            self.ui.statusbar.showMessage(message)
        else:
            self.ui.statusbar.setStyleSheet('color: green;font-weight: bold;')
            self.ui.statusbar.showMessage(message)
            
        
        #self.progress.setValue(gg)
      
     
    def updater(self, val):
        
        val = self.timeSeconds
        if val == 0:
            self.timer.stop()
            self.check()
            self.ui.scrollArea.setEnabled(False)
            self.ui.scrollArea.setEnabled(False)
        self.ui.label.setText(self.intToTime(val))
        self.timeSeconds -= 1

        self.progress.setValue(val*3.3)

    def intToTime(self, num):
        h = 0
        m = 0
        if num >= 3600:
            h = num // 3600
            num = num % 3600
        if num >= 60:
            m = num //60
            num = num % 60

        s = num
        strl = "%d." % h
        if m < 10:
            strl += "0%d:" %m
        else:
            strl += "%d:" %m

        if s < 10:
            strl += "0%d" %s
        else:
            strl += "%d" %s

        return strl

        
    


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())


