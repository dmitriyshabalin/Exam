import sys
import random
import xml.dom.minidom
from learn1 import *
from PyQt5 import QtCore, QtGui, QtWidgets

class MyWin(QtWidgets.QMainWindow):
    
    text = []
    questions = []
    variants = []
    correct = []
    
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.dom = xml.dom.minidom.parse('learn.xml')
        self.collection = self.dom.documentElement
        self.linesArr = self.collection.getElementsByTagName("text")

        for line in self.linesArr:
            self.text.append(line.childNodes[0].data)
            self.questions.append(line.getAttribute('question'))
            self.variants.append(line.getAttribute('answers').split('**?**'))
            self.correct.append(line.getAttribute('correct'))

        random.shuffle(self.variants[0])
        random.shuffle(self.variants[1])
        random.shuffle(self.variants[2])
        
        random.shuffle(self.variants[3])
        random.shuffle(self.variants[4])
        random.shuffle(self.variants[5])
        random.shuffle(self.variants[6])
        random.shuffle(self.variants[7])
        random.shuffle(self.variants[8])
        random.shuffle(self.variants[9])

        self.ui.textEdit.setText(self.questions[0])
        self.ui.textEdit_2.setText(self.questions[1])
        self.ui.textEdit_3.setText(self.questions[2])
        
        self.ui.textEdit_7.setText(self.questions[3])
        self.ui.textEdit_8.setText(self.questions[4])
        self.ui.textEdit_24.setText(self.questions[5])
        self.ui.textEdit_25.setText(self.questions[6])
        self.ui.textEdit_26.setText(self.questions[7])
        self.ui.textEdit_27.setText(self.questions[8])
        self.ui.textEdit_28.setText(self.questions[9])
        
        
        self.ui.label.setText(self.text[0])
        self.ui.label_2.setText(self.text[1])
        self.ui.label_3.setText(self.text[2])

        self.ui.label_7.setText(self.text[2])
        self.ui.label_8.setText(self.text[2])
        self.ui.label_24.setText(self.text[2])
        self.ui.label_25.setText(self.text[2])
        self.ui.label_26.setText(self.text[2])
        self.ui.label_27.setText(self.text[2])
        self.ui.label_28.setText(self.text[2])

        self.ui.radioButton.setText(self.variants[0][0])
        self.ui.radioButton_2.setText(self.variants[0][1])
        self.ui.radioButton_3.setText(self.variants[0][2])

        self.ui.radioButton_4.setText(self.variants[1][0])
        self.ui.radioButton_5.setText(self.variants[1][1])
        self.ui.radioButton_6.setText(self.variants[1][2])

        self.ui.radioButton_7.setText(self.variants[2][0])
        self.ui.radioButton_8.setText(self.variants[2][1])
        self.ui.radioButton_9.setText(self.variants[2][2])

        

        self.ui.radioButton_19.setText(self.variants[3][0])
        self.ui.radioButton_20.setText(self.variants[3][1])
        self.ui.radioButton_21.setText(self.variants[3][2])

        self.ui.radioButton_22.setText(self.variants[4][0])
        self.ui.radioButton_23.setText(self.variants[4][1])
        self.ui.radioButton_24.setText(self.variants[4][2])

        self.ui.radioButton_70.setText(self.variants[5][0])
        self.ui.radioButton_71.setText(self.variants[5][1])
        self.ui.radioButton_72.setText(self.variants[5][2])

        self.ui.radioButton_73.setText(self.variants[6][0])
        self.ui.radioButton_74.setText(self.variants[6][1])
        self.ui.radioButton_75.setText(self.variants[6][2])

        self.ui.radioButton_76.setText(self.variants[7][0])
        self.ui.radioButton_77.setText(self.variants[7][1])
        self.ui.radioButton_78.setText(self.variants[7][2])

        self.ui.radioButton_79.setText(self.variants[8][0])
        self.ui.radioButton_80.setText(self.variants[8][1])
        self.ui.radioButton_81.setText(self.variants[8][2])

        self.ui.radioButton_82.setText(self.variants[9][0])
        self.ui.radioButton_83.setText(self.variants[9][1])
        self.ui.radioButton_84.setText(self.variants[9][2])
        

        self.ui.tabWidget.setTabEnabled(1, False)
        self.ui.tabWidget.setTabEnabled(2, False)
        
        self.ui.tabWidget.setTabEnabled(3, False)
        self.ui.tabWidget.setTabEnabled(4, False)
        self.ui.tabWidget.setTabEnabled(5, False)
        self.ui.tabWidget.setTabEnabled(6, False)
        self.ui.tabWidget.setTabEnabled(7, False)
        self.ui.tabWidget.setTabEnabled(8, False)
        self.ui.tabWidget.setTabEnabled(9, False)

        self.ui.buttonGroup.buttonClicked.connect(self.correctAnsl)
        self.ui.buttonGroup_2.buttonClicked.connect(self.correctAnsl2)
        self.ui.buttonGroup_3.buttonClicked.connect(self.correctAnsl3)

        self.ui.buttonGroup_4.buttonClicked.connect(self.correctAnsl4)
        self.ui.buttonGroup_5.buttonClicked.connect(self.correctAnsl5)
        self.ui.buttonGroup_6.buttonClicked.connect(self.correctAnsl6)
        self.ui.buttonGroup_7.buttonClicked.connect(self.correctAnsl7)
        self.ui.buttonGroup_8.buttonClicked.connect(self.correctAnsl8)
        self.ui.buttonGroup_9.buttonClicked.connect(self.correctAnsl9)
        self.ui.buttonGroup_10.buttonClicked.connect(self.correctAnsl10)



    def correctAnsl(self):
        for rb in self.ui.buttonGroup.buttons():
            if rb.isChecked():
                if rb.text() == self.correct[0]:
                    self.ui.statusbar.showMessage("Верно!",2000)
                    self.ui.tab.setEnabled(False)
                    self.ui.tabWidget.setTabEnabled(1, True)

    def correctAnsl2(self):
        for rb in self.ui.buttonGroup_2.buttons():
            if rb.isChecked():
                if rb.text() == self.correct[1]:
                    self.ui.statusbar.showMessage("Верно!",2000)
                    self.ui.tab_2.setEnabled(False)
                    self.ui.tabWidget.setTabEnabled(2, True)

    def correctAnsl3(self):
        for rb in self.ui.buttonGroup_3.buttons():
            if rb.isChecked():
                if rb.text() == self.correct[2]:
                    self.ui.statusbar.showMessage("Верно!",2000)
                    self.ui.tab_3.setEnabled(False)
                    self.ui.tabWidget.setTabEnabled(3, True)

    def correctAnsl4(self):
        for rb in self.ui.buttonGroup_4.buttons():
            if rb.isChecked():
                if rb.text() == self.correct[3]:
                    self.ui.statusbar.showMessage("Верно!",2000)
                    self.ui.tab_7.setEnabled(False)
                    self.ui.tabWidget.setTabEnabled(4, True)

    def correctAnsl5(self):
        for rb in self.ui.buttonGroup_5.buttons():
            if rb.isChecked():
                if rb.text() == self.correct[4]:
                    self.ui.statusbar.showMessage("Верно!",2000)
                    self.ui.tab_8.setEnabled(False)
                    self.ui.tabWidget.setTabEnabled(5, True)

    def correctAnsl6(self):
        for rb in self.ui.buttonGroup_6.buttons():
            if rb.isChecked():
                if rb.text() == self.correct[5]:
                    self.ui.statusbar.showMessage("Верно!",2000)
                    self.ui.tab_9.setEnabled(False)
                    self.ui.tabWidget.setTabEnabled(6, True)
        
    def correctAnsl7(self):
        for rb in self.ui.buttonGroup_7.buttons():
            if rb.isChecked():
                if rb.text() == self.correct[6]:
                    self.ui.statusbar.showMessage("Верно!",2000)
                    self.ui.tab_10.setEnabled(False)
                    self.ui.tabWidget.setTabEnabled(7, True)

    def correctAnsl8(self):
        for rb in self.ui.buttonGroup_8.buttons():
            if rb.isChecked():
                if rb.text() == self.correct[7]:
                    self.ui.statusbar.showMessage("Верно!",2000)
                    self.ui.tab_11.setEnabled(False)
                    self.ui.tabWidget.setTabEnabled(8, True)

    def correctAnsl9(self):
        for rb in self.ui.buttonGroup_9.buttons():
            if rb.isChecked():
                if rb.text() == self.correct[8]:
                    self.ui.statusbar.showMessage("Верно!",2000)
                    self.ui.tab_12.setEnabled(False)
                    self.ui.tabWidget.setTabEnabled(9, True)

    def correctAnsl10(self):
        for rb in self.ui.buttonGroup_10.buttons():
            if rb.isChecked():
                if rb.text() == self.correct[9]:
                    self.ui.statusbar.showMessage("Верно! Тест пройден!!!",5000)
                    self.ui.tab_13.setEnabled(False)
        

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())


    
