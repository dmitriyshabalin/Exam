# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 240)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.TextEdit.setGeometry(QtCore.QRect(10, 0, 301, 191))
        self.TextEdit.setObjectName("TextEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionFont = QtWidgets.QAction(MainWindow)
        self.actionFont.setObjectName("actionFont")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.Open_test = QtWidgets.QAction(MainWindow)
        self.Open_test.setObjectName("Open_test")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuOptions.addAction(self.actionFont)
        self.menuOptions.addAction(self.Open_test)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionFont.setText(_translate("MainWindow", "Font..."))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.Open_test.setText(_translate("MainWindow", "Open test"))
