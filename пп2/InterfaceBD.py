# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InterfaceBD.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(784, 482)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 761, 431))
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.tabWidget = QtWidgets.QTabWidget(self.page)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 621, 361))
        self.tabWidget.setStyleSheet("QTabBar::tab {\n"
"color:white; /* цвет букв таблицы */\n"
"background:#424242; /* цвет заднего фона букв таблицы */\n"
"border: 1px solid black;\n"
"font:8pt \"Myriad Pro\";\n"
"height:12px;\n"
"padding:5px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"background: #424270;  /* цвет заднего фона букв таблицы выбранной вкладки  */\n"
"margin-bottom: -1px;\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget_1 = QtWidgets.QTableWidget(self.tab)
        self.tableWidget_1.setGeometry(QtCore.QRect(0, 0, 611, 331))
        self.tableWidget_1.setStyleSheet("QTableWidget {\n"
"     background-color: #d2bcab;\n"
" }")
        self.tableWidget_1.setObjectName("tableWidget_1")
        self.tableWidget_1.setColumnCount(4)
        self.tableWidget_1.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_1.setHorizontalHeaderItem(3, item)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 0, 611, 331))
        self.tableWidget_2.setStyleSheet("QTableWidget {\n"
"     background-color: #d2bcab;\n"
" }")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_3.setGeometry(QtCore.QRect(0, 0, 611, 331))
        self.tableWidget_3.setStyleSheet("QTableWidget {\n"
"     background-color: #d2bcab;\n"
" }")
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(3)
        self.tableWidget_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget_4.setGeometry(QtCore.QRect(0, 0, 611, 331))
        self.tableWidget_4.setStyleSheet("QTableWidget {\n"
"     background-color: #d2bcab;\n"
" }")
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(5)
        self.tableWidget_4.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, item)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tableWidget_5 = QtWidgets.QTableWidget(self.tab_5)
        self.tableWidget_5.setGeometry(QtCore.QRect(0, 0, 611, 331))
        self.tableWidget_5.setStyleSheet("QTableWidget {\n"
"     background-color: #d2bcab;\n"
" }")
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(0)
        self.tableWidget_5.setRowCount(0)
        self.tabWidget.addTab(self.tab_5, "")
        self.pushButton_3 = QtWidgets.QPushButton(self.page)
        self.pushButton_3.setGeometry(QtCore.QRect(640, 90, 111, 23))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"     background-color: grey;\n"
"    color: white;\n"
" }")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton = QtWidgets.QPushButton(self.page)
        self.pushButton.setGeometry(QtCore.QRect(640, 30, 111, 23))
        self.pushButton.setStyleSheet("QPushButton {\n"
"     background-color: grey;\n"
"    color: white;\n"
" }")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.page)
        self.pushButton_2.setGeometry(QtCore.QRect(640, 60, 111, 23))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"     background-color: grey;\n"
"    color: white;\n"
" }")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.page)
        self.pushButton_5.setGeometry(QtCore.QRect(660, 400, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"     background-color: #800000;\n"
"    color: white;\n"
" }")
        self.pushButton_5.setIconSize(QtCore.QSize(82, 32))
        self.pushButton_5.setAutoRepeat(False)
        self.pushButton_5.setAutoExclusive(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.frame = QtWidgets.QFrame(self.page)
        self.frame.setGeometry(QtCore.QRect(0, 0, 761, 431))
        self.frame.setStyleSheet("QFrame{\n"
"    background: #8a3324;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget_2.setGeometry(QtCore.QRect(649, 140, 111, 211))
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.frame_7 = QtWidgets.QFrame(self.page_6)
        self.frame_7.setGeometry(QtCore.QRect(0, 0, 111, 211))
        self.frame_7.setStyleSheet("QFrame{\n"
"    background: #8a3324;\n"
"}")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.listWidget = QtWidgets.QListWidget(self.frame_7)
        self.listWidget.setGeometry(QtCore.QRect(0, 60, 101, 91))
        self.listWidget.setStyleSheet("QListWidget{\n"
"    background-color: #424242;\n"
"    color:white;\n"
"\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"    color: red;\n"
"}")
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.stackedWidget_2.addWidget(self.page_6)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.frame_8 = QtWidgets.QFrame(self.page_7)
        self.frame_8.setGeometry(QtCore.QRect(0, 0, 111, 211))
        self.frame_8.setStyleSheet("QFrame{\n"
"    background: #8a3324;\n"
"}")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.stackedWidget_2.addWidget(self.page_7)
        self.label_24 = QtWidgets.QLabel(self.frame)
        self.label_24.setGeometry(QtCore.QRect(10, 380, 121, 16))
        self.label_24.setStyleSheet("QLabel{\n"
"    color: black;\n"
"}")
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.frame)
        self.label_25.setGeometry(QtCore.QRect(120, 380, 131, 16))
        self.label_25.setStyleSheet("QLabel{\n"
"    color: black;\n"
"}")
        self.label_25.setText("")
        self.label_25.setObjectName("label_25")
        self.frame.raise_()
        self.tabWidget.raise_()
        self.pushButton_3.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_5.raise_()
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label = QtWidgets.QLabel(self.page_2)
        self.label.setGeometry(QtCore.QRect(340, 0, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"    color: white;\n"
"}")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 71, 16))
        self.label_2.setStyleSheet("QLabel{\n"
"    color: white;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setGeometry(QtCore.QRect(130, 50, 41, 16))
        self.label_3.setStyleSheet("QLabel{\n"
"    color: white;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit.setGeometry(QtCore.QRect(10, 70, 113, 20))
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 70, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(250, 70, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(370, 70, 113, 20))
        self.lineEdit_4.setAutoFillBackground(False)
        self.lineEdit_4.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_4.setInputMask("")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setGeometry(QtCore.QRect(250, 50, 51, 16))
        self.label_4.setStyleSheet("QLabel{\n"
"    color: white;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.page_2)
        self.label_5.setGeometry(QtCore.QRect(370, 50, 51, 16))
        self.label_5.setStyleSheet("QLabel{\n"
"    color: white;\n"
"}")
        self.label_5.setObjectName("label_5")
        self.spinBox = QtWidgets.QSpinBox(self.page_2)
        self.spinBox.setGeometry(QtCore.QRect(150, 200, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.label_6 = QtWidgets.QLabel(self.page_2)
        self.label_6.setGeometry(QtCore.QRect(20, 200, 131, 16))
        self.label_6.setStyleSheet("QLabel{\n"
"    color: white;\n"
"}")
        self.label_6.setObjectName("label_6")
        self.pushButton_6 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_6.setGeometry(QtCore.QRect(230, 200, 75, 23))
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"     background-color: grey;\n"
"    color: white;\n"
" }")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_7.setGeometry(QtCore.QRect(320, 200, 75, 23))
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0.5, y2: 0.5,\n"
"                                 stop: 0 red, stop: 1 rgb(255, 191, 191));\n"
" }")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_14 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_14.setGeometry(QtCore.QRect(420, 200, 75, 23))
        self.pushButton_14.setStyleSheet("QPushButton {\n"
"     background-color: grey;\n"
"    color: white;\n"
" }")
        self.pushButton_14.setObjectName("pushButton_14")
        self.frame_3 = QtWidgets.QFrame(self.page_2)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 761, 431))
        self.frame_3.setStyleSheet("QFrame{\n"
"    background: #8a3324;\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_3.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_4.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.spinBox.raise_()
        self.label_6.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.pushButton_14.raise_()
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_7 = QtWidgets.QLabel(self.page_3)
        self.label_7.setGeometry(QtCore.QRect(330, 10, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("QLabel{\n"
"    color: white;\n"
"}")
        self.label_7.setObjectName("label_7")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.page_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(10, 80, 113, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.page_3)
        self.lineEdit_6.setGeometry(QtCore.QRect(130, 80, 113, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.page_3)
        self.lineEdit_7.setGeometry(QtCore.QRect(250, 80, 113, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_8 = QtWidgets.QLabel(self.page_3)
        self.label_8.setGeometry(QtCore.QRect(10, 60, 71, 16))
        self.label_8.setStyleSheet("QLabel{\n"
"    color: white;\n"
"}")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.page_3)
        self.label_9.setGeometry(QtCore.QRect(130, 60, 51, 16))
        self.label_9.setStyleSheet("QLabel{\n"
"    color: white;\n"
"}")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.page_3)
        self.label_10.setGeometry(QtCore.QRect(250, 60, 91, 16))
        self.label_10.setStyleSheet("QLabel{\n"
"    color: white;\n"
"}")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.page_3)
        self.label_11.setGeometry(QtCore.QRect(20, 180, 131, 16))
        self.label_11.setStyleSheet("QLabel{\n"
"    color: white;\n"
"}")
        self.label_11.setObjectName("label_11")
        self.spinBox_2 = QtWidgets.QSpinBox(self.page_3)
        self.spinBox_2.setGeometry(QtCore.QRect(160, 180, 42, 22))
        self.spinBox_2.setObjectName("spinBox_2")
        self.pushButton_8 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_8.setGeometry(QtCore.QRect(230, 180, 75, 23))
        self.pushButton_8.setStyleSheet("QPushButton {\n"
"     background-color: grey;\n"
"    color: white;\n"
" }")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_9.setGeometry(QtCore.QRect(320, 180, 75, 23))
        self.pushButton_9.setStyleSheet("QPushButton {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0.5, y2: 0.5,\n"
"                                 stop: 0 red, stop: 1 rgb(255, 191, 191));\n"
" }")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_15 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_15.setGeometry(QtCore.QRect(410, 180, 75, 23))
        self.pushButton_15.setStyleSheet("QPushButton {\n"
"     background-color: grey;\n"
"    color: white;\n"
" }")
        self.pushButton_15.setObjectName("pushButton_15")
        self.frame_4 = QtWidgets.QFrame(self.page_3)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 761, 431))
        self.frame_4.setStyleSheet("QFrame{\n"
"    background: #8a3324;\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_4.raise_()
        self.label_7.raise_()
        self.lineEdit_5.raise_()
        self.lineEdit_6.raise_()
        self.lineEdit_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.spinBox_2.raise_()
        self.pushButton_8.raise_()
        self.pushButton_9.raise_()
        self.pushButton_15.raise_()
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_12 = QtWidgets.QLabel(self.page_4)
        self.label_12.setGeometry(QtCore.QRect(360, 10, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("QLabel{\n"
"    color: white;\n"
"}")
        self.label_12.setObjectName("label_12")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.page_4)
        self.lineEdit_8.setGeometry(QtCore.QRect(10, 70, 113, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.page_4)
        self.lineEdit_9.setGeometry(QtCore.QRect(130, 70, 113, 20))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.page_4)
        self.lineEdit_10.setGeometry(QtCore.QRect(250, 70, 113, 20))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_13 = QtWidgets.QLabel(self.page_4)
        self.label_13.setGeometry(QtCore.QRect(10, 50, 61, 16))
        self.label_13.setStyleSheet("QLabel{\n"
"    color: white;\n"
"}")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.page_4)
        self.label_14.setGeometry(QtCore.QRect(130, 50, 81, 16))
        self.label_14.setStyleSheet("QLabel{\n"
"    color: white;\n"
"}")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.page_4)
        self.label_15.setGeometry(QtCore.QRect(260, 50, 61, 16))
        self.label_15.setStyleSheet("QLabel{\n"
"    color: white;\n"
"}")
        self.label_15.setObjectName("label_15")
        self.spinBox_3 = QtWidgets.QSpinBox(self.page_4)
        self.spinBox_3.setGeometry(QtCore.QRect(160, 190, 42, 22))
        self.spinBox_3.setObjectName("spinBox_3")
        self.pushButton_10 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_10.setGeometry(QtCore.QRect(230, 190, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("QPushButton {\n"
"     background-color: grey;\n"
"    color: white;\n"
" }")
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_16 = QtWidgets.QLabel(self.page_4)
        self.label_16.setGeometry(QtCore.QRect(20, 190, 131, 16))
        self.label_16.setStyleSheet("QLabel{\n"
"    color: white;\n"
"}")
        self.label_16.setObjectName("label_16")
        self.pushButton_11 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_11.setGeometry(QtCore.QRect(320, 190, 75, 23))
        self.pushButton_11.setStyleSheet("QPushButton {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0.5, y2: 0.5,\n"
"                                 stop: 0 red, stop: 1 rgb(255, 191, 191));\n"
" }")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_16 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_16.setGeometry(QtCore.QRect(410, 190, 75, 23))
        self.pushButton_16.setStyleSheet("QPushButton {\n"
"     background-color: grey;\n"
"    color: white;\n"
" }")
        self.pushButton_16.setObjectName("pushButton_16")
        self.frame_5 = QtWidgets.QFrame(self.page_4)
        self.frame_5.setGeometry(QtCore.QRect(0, 0, 761, 431))
        self.frame_5.setStyleSheet("QFrame{\n"
"    background: #8a3324;\n"
"}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.frame_5.raise_()
        self.label_12.raise_()
        self.lineEdit_8.raise_()
        self.lineEdit_9.raise_()
        self.lineEdit_10.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.spinBox_3.raise_()
        self.pushButton_10.raise_()
        self.label_16.raise_()
        self.pushButton_11.raise_()
        self.pushButton_16.raise_()
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.label_17 = QtWidgets.QLabel(self.page_5)
        self.label_17.setGeometry(QtCore.QRect(290, 10, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("QLabel{\n"
"    color: white;\n"
"}")
        self.label_17.setObjectName("label_17")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.page_5)
        self.lineEdit_11.setGeometry(QtCore.QRect(10, 80, 113, 20))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.page_5)
        self.lineEdit_15.setGeometry(QtCore.QRect(490, 80, 113, 20))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.label_18 = QtWidgets.QLabel(self.page_5)
        self.label_18.setGeometry(QtCore.QRect(10, 60, 91, 16))
        self.label_18.setStyleSheet("QLabel{\n"
"    color: white;\n"
"}")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.page_5)
        self.label_19.setGeometry(QtCore.QRect(130, 60, 71, 16))
        self.label_19.setStyleSheet("QLabel{\n"
"    color: white;\n"
"}")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.page_5)
        self.label_20.setGeometry(QtCore.QRect(250, 60, 71, 16))
        self.label_20.setStyleSheet("QLabel{\n"
"    color: white;\n"
"}")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.page_5)
        self.label_21.setGeometry(QtCore.QRect(370, 60, 61, 16))
        self.label_21.setStyleSheet("QLabel{\n"
"    color: white;\n"
"}")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.page_5)
        self.label_22.setGeometry(QtCore.QRect(490, 60, 51, 16))
        self.label_22.setStyleSheet("QLabel{\n"
"    color: white;\n"
"}")
        self.label_22.setObjectName("label_22")
        self.pushButton_12 = QtWidgets.QPushButton(self.page_5)
        self.pushButton_12.setGeometry(QtCore.QRect(230, 190, 75, 23))
        self.pushButton_12.setStyleSheet("QPushButton {\n"
"     background-color: grey;\n"
"    color: white;\n"
" }")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.page_5)
        self.pushButton_13.setGeometry(QtCore.QRect(320, 190, 75, 23))
        self.pushButton_13.setStyleSheet("QPushButton {\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0.5, y2: 0.5,\n"
"                                 stop: 0 red, stop: 1 rgb(255, 191, 191));\n"
" }")
        self.pushButton_13.setObjectName("pushButton_13")
        self.spinBox_4 = QtWidgets.QSpinBox(self.page_5)
        self.spinBox_4.setGeometry(QtCore.QRect(160, 190, 42, 22))
        self.spinBox_4.setObjectName("spinBox_4")
        self.label_23 = QtWidgets.QLabel(self.page_5)
        self.label_23.setGeometry(QtCore.QRect(20, 190, 131, 16))
        self.label_23.setStyleSheet("QLabel{\n"
"    color: white;\n"
"}")
        self.label_23.setObjectName("label_23")
        self.pushButton_17 = QtWidgets.QPushButton(self.page_5)
        self.pushButton_17.setGeometry(QtCore.QRect(410, 190, 75, 23))
        self.pushButton_17.setStyleSheet("QPushButton {\n"
"     background-color: grey;\n"
"    color: white;\n"
" }")
        self.pushButton_17.setObjectName("pushButton_17")
        self.frame_6 = QtWidgets.QFrame(self.page_5)
        self.frame_6.setGeometry(QtCore.QRect(0, 0, 761, 431))
        self.frame_6.setStyleSheet("QFrame{\n"
"    background: #8a3324;\n"
"}")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.comboBox = QtWidgets.QComboBox(self.frame_6)
        self.comboBox.setGeometry(QtCore.QRect(130, 80, 111, 22))
        self.comboBox.setStyleSheet("QComboBox{\n"
"    background: grey;\n"
"    color:white;\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_6)
        self.comboBox_2.setGeometry(QtCore.QRect(250, 80, 111, 22))
        self.comboBox_2.setStyleSheet("QComboBox{\n"
"    background: grey;\n"
"    color:white;\n"
"}")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.frame_6)
        self.comboBox_3.setGeometry(QtCore.QRect(370, 80, 111, 22))
        self.comboBox_3.setStyleSheet("QComboBox{\n"
"    background: grey;\n"
"    color:white;\n"
"}")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_26 = QtWidgets.QLabel(self.frame_6)
        self.label_26.setGeometry(QtCore.QRect(600, 50, 141, 21))
        self.label_26.setText("")
        self.label_26.setObjectName("label_26")
        self.frame_6.raise_()
        self.label_17.raise_()
        self.lineEdit_11.raise_()
        self.lineEdit_15.raise_()
        self.label_18.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.label_21.raise_()
        self.label_22.raise_()
        self.pushButton_12.raise_()
        self.pushButton_13.raise_()
        self.spinBox_4.raise_()
        self.label_23.raise_()
        self.pushButton_17.raise_()
        self.stackedWidget.addWidget(self.page_5)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 791, 451))
        self.frame_2.setStyleSheet("QFrame{\n"
"    background: #424242;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.raise_()
        self.stackedWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 784, 21))
        self.menubar.setStyleSheet("QMenuBar{\n"
"    background: #800000;\n"
"    color: white;\n"
"}\n"
"\n"
"QMenuBar::item:selected{\n"
"    background: #8a3324;\n"
"    color: white;\n"
"}")
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setStyleSheet("QMenu{\n"
"    background: white;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QMenu::item:selected{\n"
"    background: #8a3324;\n"
"    color: white;\n"
"}\n"
"")
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setStyleSheet("QMenu{\n"
"    background: white;\n"
"    border: 1px solid black;\n"
"}\n"
"\n"
"QMenu::item:selected{\n"
"    background: #8a3324;\n"
"    color: white;\n"
"}\n"
"")
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menu_2)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("QStatusBar{\n"
"    background: #424242;\n"
"    color: white;\n"
"}")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_6 = QtWidgets.QAction(MainWindow)
        self.action_6.setObjectName("action_6")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.actionWord = QtWidgets.QAction(MainWindow)
        self.actionWord.setObjectName("actionWord")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.actionExcel = QtWidgets.QAction(MainWindow)
        self.actionExcel.setObjectName("actionExcel")
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_4)
        self.menu_3.addAction(self.actionWord)
        self.menu_3.addAction(self.action_3)
        self.menu_3.addAction(self.actionExcel)
        self.menu_2.addAction(self.menu_3.menuAction())
        self.menu_2.addAction(self.action_6)
        self.menu_2.addAction(self.action)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Работа с базой данных"))
        item = self.tableWidget_1.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id_клиента"))
        item = self.tableWidget_1.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ФИО"))
        item = self.tableWidget_1.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "адрес"))
        item = self.tableWidget_1.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "телефон"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Клиенты"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id_рабочего"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ФИО"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "квалификация"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Работники"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id_услуги"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "наименование"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "стоимость"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Услуги"))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id_регистрации"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "id_клиента"))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "id_рабочего"))
        item = self.tableWidget_4.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "id_услуги"))
        item = self.tableWidget_4.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "дата"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Регистрация_работ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Запросы"))
        self.pushButton_3.setText(_translate("MainWindow", "Удалить"))
        self.pushButton.setText(_translate("MainWindow", "Обновить"))
        self.pushButton_2.setText(_translate("MainWindow", "Добавить/Изменить"))
        self.pushButton_5.setText(_translate("MainWindow", "Выход"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Запрос 1"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "Запрос 2"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "Запрос 3"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "Запрос 4"))
        item = self.listWidget.item(4)
        item.setText(_translate("MainWindow", "Запрос 5"))
        item = self.listWidget.item(5)
        item.setText(_translate("MainWindow", "Запрос 6"))
        item = self.listWidget.item(6)
        item.setText(_translate("MainWindow", "Запрос 7"))
        item = self.listWidget.item(7)
        item.setText(_translate("MainWindow", "Запрос 8"))
        item = self.listWidget.item(8)
        item.setText(_translate("MainWindow", "Запрос 9"))
        item = self.listWidget.item(9)
        item.setText(_translate("MainWindow", "Запрос 10"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "Клиенты"))
        self.label_2.setText(_translate("MainWindow", "id_клиента"))
        self.label_3.setText(_translate("MainWindow", "ФИО"))
        self.label_4.setText(_translate("MainWindow", "адрес"))
        self.label_5.setText(_translate("MainWindow", "телефон"))
        self.label_6.setText(_translate("MainWindow", "Выбирите номер записи:"))
        self.pushButton_6.setText(_translate("MainWindow", "Изменить"))
        self.pushButton_7.setText(_translate("MainWindow", "Отмена"))
        self.pushButton_14.setText(_translate("MainWindow", "Добавить"))
        self.label_7.setText(_translate("MainWindow", "Работники"))
        self.label_8.setText(_translate("MainWindow", "id_рабочего"))
        self.label_9.setText(_translate("MainWindow", "ФИО"))
        self.label_10.setText(_translate("MainWindow", "квалификация"))
        self.label_11.setText(_translate("MainWindow", "Выбирите номер записи:"))
        self.pushButton_8.setText(_translate("MainWindow", "Изменить"))
        self.pushButton_9.setText(_translate("MainWindow", "Отмена"))
        self.pushButton_15.setText(_translate("MainWindow", "Добавить"))
        self.label_12.setText(_translate("MainWindow", "Услуги"))
        self.label_13.setText(_translate("MainWindow", "id_услуги"))
        self.label_14.setText(_translate("MainWindow", "наименование"))
        self.label_15.setText(_translate("MainWindow", "стоимость"))
        self.pushButton_10.setText(_translate("MainWindow", "Изменить"))
        self.label_16.setText(_translate("MainWindow", "Выбирите номер записи:"))
        self.pushButton_11.setText(_translate("MainWindow", "Отмена"))
        self.pushButton_16.setText(_translate("MainWindow", "Добавить"))
        self.label_17.setText(_translate("MainWindow", "Регистрация_работ"))
        self.label_18.setText(_translate("MainWindow", "id_регистрации"))
        self.label_19.setText(_translate("MainWindow", "id_клиента"))
        self.label_20.setText(_translate("MainWindow", "id_рабочего"))
        self.label_21.setText(_translate("MainWindow", "id_услуги"))
        self.label_22.setText(_translate("MainWindow", "дата"))
        self.pushButton_12.setText(_translate("MainWindow", "Изменить"))
        self.pushButton_13.setText(_translate("MainWindow", "Отмена"))
        self.label_23.setText(_translate("MainWindow", "Выбирите номер записи:"))
        self.pushButton_17.setText(_translate("MainWindow", "Добавить"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "4"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "4"))
        self.menu.setTitle(_translate("MainWindow", "Режим"))
        self.menu_2.setTitle(_translate("MainWindow", "Опции"))
        self.menu_3.setTitle(_translate("MainWindow", "Сохранить в файл"))
        self.action_2.setText(_translate("MainWindow", "Администратор"))
        self.action_4.setText(_translate("MainWindow", "Пользователь"))
        self.action_6.setText(_translate("MainWindow", "О программе"))
        self.action.setText(_translate("MainWindow", "Инструкция"))
        self.actionWord.setText(_translate("MainWindow", "Word"))
        self.action_3.setText(_translate("MainWindow", "Блокнот"))
        self.actionExcel.setText(_translate("MainWindow", "Excel"))
