# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'learn1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(466, 322)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 451, 281))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.scrollArea = QtWidgets.QScrollArea(self.tab)
        self.scrollArea.setGeometry(QtCore.QRect(10, 10, 441, 241))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 439, 239))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setGeometry(QtCore.QRect(10, 100, 421, 131))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 401, 16))
        self.label.setText("")
        self.label.setObjectName("label")
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setGeometry(QtCore.QRect(10, 40, 401, 17))
        self.radioButton.setText("")
        self.radioButton.setObjectName("radioButton")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 60, 401, 17))
        self.radioButton_2.setText("")
        self.radioButton_2.setObjectName("radioButton_2")
        self.buttonGroup.addButton(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 80, 401, 17))
        self.radioButton_3.setText("")
        self.radioButton_3.setObjectName("radioButton_3")
        self.buttonGroup.addButton(self.radioButton_3)
        self.textEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 421, 81))
        self.textEdit.setObjectName("textEdit")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.tab_2)
        self.scrollArea_2.setGeometry(QtCore.QRect(10, 10, 441, 241))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 439, 239))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.frame_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.frame_2.setGeometry(QtCore.QRect(10, 100, 421, 131))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 401, 16))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.radioButton_4 = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_4.setGeometry(QtCore.QRect(10, 40, 401, 17))
        self.radioButton_4.setText("")
        self.radioButton_4.setObjectName("radioButton_4")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.radioButton_4)
        self.radioButton_5 = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_5.setGeometry(QtCore.QRect(10, 60, 401, 17))
        self.radioButton_5.setText("")
        self.radioButton_5.setObjectName("radioButton_5")
        self.buttonGroup_2.addButton(self.radioButton_5)
        self.radioButton_6 = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_6.setGeometry(QtCore.QRect(10, 80, 401, 17))
        self.radioButton_6.setText("")
        self.radioButton_6.setObjectName("radioButton_6")
        self.buttonGroup_2.addButton(self.radioButton_6)
        self.textEdit_2 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 10, 421, 81))
        self.textEdit_2.setObjectName("textEdit_2")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.tab_3)
        self.scrollArea_3.setGeometry(QtCore.QRect(10, 10, 441, 241))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 439, 239))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.frame_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.frame_3.setGeometry(QtCore.QRect(10, 100, 421, 131))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 401, 16))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.radioButton_7 = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton_7.setGeometry(QtCore.QRect(10, 40, 401, 17))
        self.radioButton_7.setText("")
        self.radioButton_7.setObjectName("radioButton_7")
        self.buttonGroup_3 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_3.setObjectName("buttonGroup_3")
        self.buttonGroup_3.addButton(self.radioButton_7)
        self.radioButton_8 = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton_8.setGeometry(QtCore.QRect(10, 60, 401, 17))
        self.radioButton_8.setText("")
        self.radioButton_8.setObjectName("radioButton_8")
        self.buttonGroup_3.addButton(self.radioButton_8)
        self.radioButton_9 = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton_9.setGeometry(QtCore.QRect(10, 80, 401, 17))
        self.radioButton_9.setText("")
        self.radioButton_9.setObjectName("radioButton_9")
        self.buttonGroup_3.addButton(self.radioButton_9)
        self.textEdit_3 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_3)
        self.textEdit_3.setGeometry(QtCore.QRect(10, 10, 421, 81))
        self.textEdit_3.setObjectName("textEdit_3")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.scrollArea_7 = QtWidgets.QScrollArea(self.tab_7)
        self.scrollArea_7.setGeometry(QtCore.QRect(10, 10, 441, 241))
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollArea_7.setObjectName("scrollArea_7")
        self.scrollAreaWidgetContents_7 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_7.setGeometry(QtCore.QRect(0, 0, 439, 239))
        self.scrollAreaWidgetContents_7.setObjectName("scrollAreaWidgetContents_7")
        self.frame_7 = QtWidgets.QFrame(self.scrollAreaWidgetContents_7)
        self.frame_7.setGeometry(QtCore.QRect(10, 100, 431, 131))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_7 = QtWidgets.QLabel(self.frame_7)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 421, 16))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.radioButton_19 = QtWidgets.QRadioButton(self.frame_7)
        self.radioButton_19.setGeometry(QtCore.QRect(10, 40, 401, 17))
        self.radioButton_19.setText("")
        self.radioButton_19.setObjectName("radioButton_19")
        self.buttonGroup_4 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_4.setObjectName("buttonGroup_4")
        self.buttonGroup_4.addButton(self.radioButton_19)
        self.radioButton_20 = QtWidgets.QRadioButton(self.frame_7)
        self.radioButton_20.setGeometry(QtCore.QRect(10, 60, 401, 17))
        self.radioButton_20.setText("")
        self.radioButton_20.setObjectName("radioButton_20")
        self.buttonGroup_4.addButton(self.radioButton_20)
        self.radioButton_21 = QtWidgets.QRadioButton(self.frame_7)
        self.radioButton_21.setGeometry(QtCore.QRect(10, 80, 401, 17))
        self.radioButton_21.setText("")
        self.radioButton_21.setObjectName("radioButton_21")
        self.buttonGroup_4.addButton(self.radioButton_21)
        self.textEdit_7 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_7)
        self.textEdit_7.setGeometry(QtCore.QRect(10, 10, 421, 81))
        self.textEdit_7.setObjectName("textEdit_7")
        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_7)
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.scrollArea_8 = QtWidgets.QScrollArea(self.tab_8)
        self.scrollArea_8.setGeometry(QtCore.QRect(10, 10, 441, 241))
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollArea_8.setObjectName("scrollArea_8")
        self.scrollAreaWidgetContents_8 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_8.setGeometry(QtCore.QRect(0, 0, 439, 239))
        self.scrollAreaWidgetContents_8.setObjectName("scrollAreaWidgetContents_8")
        self.frame_8 = QtWidgets.QFrame(self.scrollAreaWidgetContents_8)
        self.frame_8.setGeometry(QtCore.QRect(10, 100, 421, 131))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.label_8 = QtWidgets.QLabel(self.frame_8)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 401, 16))
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.radioButton_22 = QtWidgets.QRadioButton(self.frame_8)
        self.radioButton_22.setGeometry(QtCore.QRect(10, 40, 401, 17))
        self.radioButton_22.setText("")
        self.radioButton_22.setObjectName("radioButton_22")
        self.buttonGroup_5 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_5.setObjectName("buttonGroup_5")
        self.buttonGroup_5.addButton(self.radioButton_22)
        self.radioButton_23 = QtWidgets.QRadioButton(self.frame_8)
        self.radioButton_23.setGeometry(QtCore.QRect(10, 60, 401, 17))
        self.radioButton_23.setText("")
        self.radioButton_23.setObjectName("radioButton_23")
        self.buttonGroup_5.addButton(self.radioButton_23)
        self.radioButton_24 = QtWidgets.QRadioButton(self.frame_8)
        self.radioButton_24.setGeometry(QtCore.QRect(10, 80, 401, 17))
        self.radioButton_24.setText("")
        self.radioButton_24.setObjectName("radioButton_24")
        self.buttonGroup_5.addButton(self.radioButton_24)
        self.textEdit_8 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_8)
        self.textEdit_8.setGeometry(QtCore.QRect(10, 10, 421, 81))
        self.textEdit_8.setObjectName("textEdit_8")
        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_8)
        self.tabWidget.addTab(self.tab_8, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.scrollArea_24 = QtWidgets.QScrollArea(self.tab_9)
        self.scrollArea_24.setGeometry(QtCore.QRect(10, 10, 441, 241))
        self.scrollArea_24.setWidgetResizable(True)
        self.scrollArea_24.setObjectName("scrollArea_24")
        self.scrollAreaWidgetContents_24 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_24.setGeometry(QtCore.QRect(0, 0, 439, 239))
        self.scrollAreaWidgetContents_24.setObjectName("scrollAreaWidgetContents_24")
        self.frame_24 = QtWidgets.QFrame(self.scrollAreaWidgetContents_24)
        self.frame_24.setGeometry(QtCore.QRect(10, 100, 421, 131))
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.label_24 = QtWidgets.QLabel(self.frame_24)
        self.label_24.setGeometry(QtCore.QRect(10, 10, 401, 16))
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.radioButton_70 = QtWidgets.QRadioButton(self.frame_24)
        self.radioButton_70.setGeometry(QtCore.QRect(10, 40, 401, 17))
        self.radioButton_70.setText("")
        self.radioButton_70.setObjectName("radioButton_70")
        self.buttonGroup_6 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_6.setObjectName("buttonGroup_6")
        self.buttonGroup_6.addButton(self.radioButton_70)
        self.radioButton_71 = QtWidgets.QRadioButton(self.frame_24)
        self.radioButton_71.setGeometry(QtCore.QRect(10, 60, 401, 17))
        self.radioButton_71.setText("")
        self.radioButton_71.setObjectName("radioButton_71")
        self.buttonGroup_6.addButton(self.radioButton_71)
        self.radioButton_72 = QtWidgets.QRadioButton(self.frame_24)
        self.radioButton_72.setGeometry(QtCore.QRect(10, 80, 401, 17))
        self.radioButton_72.setText("")
        self.radioButton_72.setObjectName("radioButton_72")
        self.buttonGroup_6.addButton(self.radioButton_72)
        self.textEdit_24 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_24)
        self.textEdit_24.setGeometry(QtCore.QRect(10, 10, 421, 81))
        self.textEdit_24.setObjectName("textEdit_24")
        self.scrollArea_24.setWidget(self.scrollAreaWidgetContents_24)
        self.tabWidget.addTab(self.tab_9, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.scrollArea_25 = QtWidgets.QScrollArea(self.tab_10)
        self.scrollArea_25.setGeometry(QtCore.QRect(10, 10, 441, 241))
        self.scrollArea_25.setWidgetResizable(True)
        self.scrollArea_25.setObjectName("scrollArea_25")
        self.scrollAreaWidgetContents_25 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_25.setGeometry(QtCore.QRect(0, 0, 439, 239))
        self.scrollAreaWidgetContents_25.setObjectName("scrollAreaWidgetContents_25")
        self.frame_25 = QtWidgets.QFrame(self.scrollAreaWidgetContents_25)
        self.frame_25.setGeometry(QtCore.QRect(10, 100, 421, 131))
        self.frame_25.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.label_25 = QtWidgets.QLabel(self.frame_25)
        self.label_25.setGeometry(QtCore.QRect(10, 10, 401, 16))
        self.label_25.setText("")
        self.label_25.setObjectName("label_25")
        self.radioButton_73 = QtWidgets.QRadioButton(self.frame_25)
        self.radioButton_73.setGeometry(QtCore.QRect(10, 40, 401, 17))
        self.radioButton_73.setText("")
        self.radioButton_73.setObjectName("radioButton_73")
        self.buttonGroup_7 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_7.setObjectName("buttonGroup_7")
        self.buttonGroup_7.addButton(self.radioButton_73)
        self.radioButton_74 = QtWidgets.QRadioButton(self.frame_25)
        self.radioButton_74.setGeometry(QtCore.QRect(10, 60, 401, 17))
        self.radioButton_74.setText("")
        self.radioButton_74.setObjectName("radioButton_74")
        self.buttonGroup_7.addButton(self.radioButton_74)
        self.radioButton_75 = QtWidgets.QRadioButton(self.frame_25)
        self.radioButton_75.setGeometry(QtCore.QRect(10, 80, 401, 17))
        self.radioButton_75.setText("")
        self.radioButton_75.setObjectName("radioButton_75")
        self.buttonGroup_7.addButton(self.radioButton_75)
        self.textEdit_25 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_25)
        self.textEdit_25.setGeometry(QtCore.QRect(10, 10, 421, 81))
        self.textEdit_25.setObjectName("textEdit_25")
        self.scrollArea_25.setWidget(self.scrollAreaWidgetContents_25)
        self.tabWidget.addTab(self.tab_10, "")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.scrollArea_26 = QtWidgets.QScrollArea(self.tab_11)
        self.scrollArea_26.setGeometry(QtCore.QRect(10, 10, 441, 241))
        self.scrollArea_26.setWidgetResizable(True)
        self.scrollArea_26.setObjectName("scrollArea_26")
        self.scrollAreaWidgetContents_26 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_26.setGeometry(QtCore.QRect(0, 0, 439, 239))
        self.scrollAreaWidgetContents_26.setObjectName("scrollAreaWidgetContents_26")
        self.frame_26 = QtWidgets.QFrame(self.scrollAreaWidgetContents_26)
        self.frame_26.setGeometry(QtCore.QRect(10, 100, 421, 131))
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.label_26 = QtWidgets.QLabel(self.frame_26)
        self.label_26.setGeometry(QtCore.QRect(10, 10, 401, 16))
        self.label_26.setText("")
        self.label_26.setObjectName("label_26")
        self.radioButton_76 = QtWidgets.QRadioButton(self.frame_26)
        self.radioButton_76.setGeometry(QtCore.QRect(10, 40, 401, 17))
        self.radioButton_76.setText("")
        self.radioButton_76.setObjectName("radioButton_76")
        self.buttonGroup_8 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_8.setObjectName("buttonGroup_8")
        self.buttonGroup_8.addButton(self.radioButton_76)
        self.radioButton_77 = QtWidgets.QRadioButton(self.frame_26)
        self.radioButton_77.setGeometry(QtCore.QRect(10, 60, 401, 17))
        self.radioButton_77.setText("")
        self.radioButton_77.setObjectName("radioButton_77")
        self.buttonGroup_8.addButton(self.radioButton_77)
        self.radioButton_78 = QtWidgets.QRadioButton(self.frame_26)
        self.radioButton_78.setGeometry(QtCore.QRect(10, 80, 401, 17))
        self.radioButton_78.setText("")
        self.radioButton_78.setObjectName("radioButton_78")
        self.buttonGroup_8.addButton(self.radioButton_78)
        self.textEdit_26 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_26)
        self.textEdit_26.setGeometry(QtCore.QRect(10, 10, 421, 81))
        self.textEdit_26.setObjectName("textEdit_26")
        self.scrollArea_26.setWidget(self.scrollAreaWidgetContents_26)
        self.tabWidget.addTab(self.tab_11, "")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.scrollArea_27 = QtWidgets.QScrollArea(self.tab_12)
        self.scrollArea_27.setGeometry(QtCore.QRect(10, 10, 441, 241))
        self.scrollArea_27.setWidgetResizable(True)
        self.scrollArea_27.setObjectName("scrollArea_27")
        self.scrollAreaWidgetContents_27 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_27.setGeometry(QtCore.QRect(0, 0, 439, 239))
        self.scrollAreaWidgetContents_27.setObjectName("scrollAreaWidgetContents_27")
        self.frame_27 = QtWidgets.QFrame(self.scrollAreaWidgetContents_27)
        self.frame_27.setGeometry(QtCore.QRect(10, 100, 421, 131))
        self.frame_27.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.label_27 = QtWidgets.QLabel(self.frame_27)
        self.label_27.setGeometry(QtCore.QRect(10, 10, 401, 16))
        self.label_27.setText("")
        self.label_27.setObjectName("label_27")
        self.radioButton_79 = QtWidgets.QRadioButton(self.frame_27)
        self.radioButton_79.setGeometry(QtCore.QRect(10, 40, 401, 17))
        self.radioButton_79.setText("")
        self.radioButton_79.setObjectName("radioButton_79")
        self.buttonGroup_9 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_9.setObjectName("buttonGroup_9")
        self.buttonGroup_9.addButton(self.radioButton_79)
        self.radioButton_80 = QtWidgets.QRadioButton(self.frame_27)
        self.radioButton_80.setGeometry(QtCore.QRect(10, 60, 401, 17))
        self.radioButton_80.setText("")
        self.radioButton_80.setObjectName("radioButton_80")
        self.buttonGroup_9.addButton(self.radioButton_80)
        self.radioButton_81 = QtWidgets.QRadioButton(self.frame_27)
        self.radioButton_81.setGeometry(QtCore.QRect(10, 80, 401, 17))
        self.radioButton_81.setText("")
        self.radioButton_81.setObjectName("radioButton_81")
        self.buttonGroup_9.addButton(self.radioButton_81)
        self.textEdit_27 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_27)
        self.textEdit_27.setGeometry(QtCore.QRect(10, 10, 421, 81))
        self.textEdit_27.setObjectName("textEdit_27")
        self.scrollArea_27.setWidget(self.scrollAreaWidgetContents_27)
        self.tabWidget.addTab(self.tab_12, "")
        self.tab_13 = QtWidgets.QWidget()
        self.tab_13.setObjectName("tab_13")
        self.scrollArea_28 = QtWidgets.QScrollArea(self.tab_13)
        self.scrollArea_28.setGeometry(QtCore.QRect(10, 10, 441, 241))
        self.scrollArea_28.setWidgetResizable(True)
        self.scrollArea_28.setObjectName("scrollArea_28")
        self.scrollAreaWidgetContents_28 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_28.setGeometry(QtCore.QRect(0, 0, 439, 239))
        self.scrollAreaWidgetContents_28.setObjectName("scrollAreaWidgetContents_28")
        self.frame_28 = QtWidgets.QFrame(self.scrollAreaWidgetContents_28)
        self.frame_28.setGeometry(QtCore.QRect(10, 100, 421, 131))
        self.frame_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.label_28 = QtWidgets.QLabel(self.frame_28)
        self.label_28.setGeometry(QtCore.QRect(10, 10, 401, 16))
        self.label_28.setText("")
        self.label_28.setObjectName("label_28")
        self.radioButton_82 = QtWidgets.QRadioButton(self.frame_28)
        self.radioButton_82.setGeometry(QtCore.QRect(10, 40, 401, 17))
        self.radioButton_82.setText("")
        self.radioButton_82.setObjectName("radioButton_82")
        self.buttonGroup_10 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_10.setObjectName("buttonGroup_10")
        self.buttonGroup_10.addButton(self.radioButton_82)
        self.radioButton_83 = QtWidgets.QRadioButton(self.frame_28)
        self.radioButton_83.setGeometry(QtCore.QRect(10, 60, 401, 17))
        self.radioButton_83.setText("")
        self.radioButton_83.setObjectName("radioButton_83")
        self.buttonGroup_10.addButton(self.radioButton_83)
        self.radioButton_84 = QtWidgets.QRadioButton(self.frame_28)
        self.radioButton_84.setGeometry(QtCore.QRect(10, 80, 401, 17))
        self.radioButton_84.setText("")
        self.radioButton_84.setObjectName("radioButton_84")
        self.buttonGroup_10.addButton(self.radioButton_84)
        self.textEdit_28 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_28)
        self.textEdit_28.setGeometry(QtCore.QRect(10, 10, 421, 81))
        self.textEdit_28.setObjectName("textEdit_28")
        self.scrollArea_28.setWidget(self.scrollAreaWidgetContents_28)
        self.tabWidget.addTab(self.tab_13, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 466, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(9)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Тест"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Вопрос 1"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Вопрос 2"))
        self.textEdit_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Вопрос 3"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "Вопрос 4"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("MainWindow", "Вопрос 5"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), _translate("MainWindow", "Вопрос 6"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), _translate("MainWindow", "Вопрос 7"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_11), _translate("MainWindow", "Вопрос 8"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_12), _translate("MainWindow", "Вопрос 9"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_13), _translate("MainWindow", "Вопрос 10"))
