# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design/des.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(445, 180)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(445, 180))
        MainWindow.setMaximumSize(QtCore.QSize(445, 180))
        MainWindow.setMouseTracking(True)
        MainWindow.setTabletTracking(True)
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setGeometry(QtCore.QRect(370, 93, 75, 32))
        self.button.setFocusPolicy(QtCore.Qt.TabFocus)
        self.button.setObjectName("button")

        self.admission = QtWidgets.QLabel(self.centralwidget)
        self.admission.setGeometry(QtCore.QRect(10, 10, 65, 16))
        self.admission.setObjectName("admission")
        self.admission_line = QtWidgets.QLineEdit(self.centralwidget)
        self.admission_line.setGeometry(QtCore.QRect(77, 8, 35, 20))
        self.admission_line.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.admission_line.setAlignment(QtCore.Qt.AlignCenter)
        self.admission_line.setObjectName("admission_line")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 32, 121, 16))
        self.label.setObjectName("label")

        self.percentage_line = QtWidgets.QLineEdit(self.centralwidget)
        self.percentage_line.setGeometry(QtCore.QRect(130, 30, 30, 20))
        self.percentage_line.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.percentage_line.setAlignment(QtCore.Qt.AlignCenter)
        self.percentage_line.setObjectName("percentage_line")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 73, 130, 16))
        self.label_2.setObjectName("label_2")

        self.way = QtWidgets.QLineEdit(self.centralwidget)
        self.way.setEnabled(False)
        self.way.setGeometry(QtCore.QRect(10, 98, 361, 20))
        self.way.setMouseTracking(False)
        self.way.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.way.setObjectName("way")

        self.findFolder = QtWidgets.QPushButton(self.centralwidget)
        self.findFolder.setGeometry(QtCore.QRect(150, 68, 100, 32))
        self.findFolder.setObjectName("findFolder")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 445, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tester"))
        self.button.setText(_translate("MainWindow", "Test"))
        self.admission.setText(_translate("MainWindow", "Tolerance:"))
        self.admission_line.setText(_translate("MainWindow", "0.2"))
        self.label.setText(_translate("MainWindow", "Target percentage:"))
        self.percentage_line.setText(_translate("MainWindow", "75"))
        self.label_2.setText(_translate("MainWindow", "The path to the folder:"))
        self.way.setText(_translate("MainWindow", "Your folder"))
        self.findFolder.setText(_translate("MainWindow", "Find Folder"))
