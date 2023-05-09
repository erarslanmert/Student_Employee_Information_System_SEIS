# -- coding: utf-8 --
import ast
from datetime import datetime
import json


# Form implementation generated from reading ui file 'change_employee_data.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog

import connect_database
import data_objects

experience_list = []
salary_paid = []
salary_unpaid = []
new_state = ''
payment_date_options = []

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(738, 731)
        Dialog.setStyleSheet("background-color: rgb(0, 52, 77);")
        Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.Turkish, QtCore.QLocale.Turkey))
        Dialog.setWindowIcon(QtGui.QIcon("logo_hq.png"))
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(20, 90, 701, 571))
        self.frame.setStyleSheet("color: rgb(255, 230, 207);")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 100, 161, 20))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.lineEdit_2.setFont(font)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(40, 130, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(150, 70, 161, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit.setObjectName("lineEdit")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.lineEdit.setFont(font)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(150, 160, 161, 20))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.lineEdit_4.setFont(font)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 70, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 47, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(40, 160, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_16.setGeometry(QtCore.QRect(480, 100, 161, 61))
        self.lineEdit_16.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_16.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lineEdit_16.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit_16.setClearButtonEnabled(False)
        self.lineEdit_16.setObjectName("lineEdit_16")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.lineEdit_16.setFont(font)
        self.label_22 = QtWidgets.QLabel(self.frame)
        self.label_22.setGeometry(QtCore.QRect(370, 120, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_22.setObjectName("label_22")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_19.setGeometry(QtCore.QRect(150, 190, 161, 20))
        self.lineEdit_19.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_19.setObjectName("lineEdit_19")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.lineEdit_19.setFont(font)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(40, 180, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(370, 40, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(530, 280, 71, 71))
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_8.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("default-user-image.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.label_8.setFont(font)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(580, 330, 21, 21))
        self.pushButton_5.setAutoFillBackground(False)
        self.pushButton_5.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_5.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_5.setFlat(False)
        self.pushButton_5.setObjectName("pushButton_5")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.pushButton_5.setFont(font)
        self.label_27 = QtWidgets.QLabel(self.frame)
        self.label_27.setGeometry(QtCore.QRect(370, 310, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_27.setObjectName("label_27")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_23.setGeometry(QtCore.QRect(170, 260, 141, 20))
        self.lineEdit_23.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_23.setText("")
        self.lineEdit_23.setObjectName("lineEdit_23")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.lineEdit_23.setFont(font)
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(40, 270, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(40, 220, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame, clicked = lambda : self.add_item())
        self.pushButton_6.setGeometry(QtCore.QRect(290, 260, 21, 21))
        self.pushButton_6.setAutoFillBackground(False)
        self.pushButton_6.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_6.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_6.setFlat(False)
        self.pushButton_6.setObjectName("pushButton_6")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.pushButton_6.setFont(font)
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(40, 40, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.comboBox_5 = QtWidgets.QComboBox(self.frame)
        self.comboBox_5.setGeometry(QtCore.QRect(150, 40, 161, 21))
        self.comboBox_5.setAutoFillBackground(False)
        self.comboBox_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.comboBox_5.setObjectName("comboBox_5")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.comboBox_5.setFont(font)
        self.lineEdit_25 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_25.setGeometry(QtCore.QRect(480, 40, 161, 20))
        self.lineEdit_25.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_25.setText("")
        self.lineEdit_25.setObjectName("lineEdit_25")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.lineEdit_25.setFont(font)
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(370, 70, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_12.setObjectName("label_12")
        self.lineEdit_26 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_26.setGeometry(QtCore.QRect(480, 70, 161, 20))
        self.lineEdit_26.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_26.setText("")
        self.lineEdit_26.setObjectName("lineEdit_26")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.lineEdit_26.setFont(font)
        self.label_34 = QtWidgets.QLabel(self.frame)
        self.label_34.setGeometry(QtCore.QRect(370, 170, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_34.setObjectName("label_34")
        self.comboBox_6 = QtWidgets.QComboBox(self.frame)
        self.comboBox_6.setGeometry(QtCore.QRect(480, 170, 161, 21))
        self.comboBox_6.setAutoFillBackground(False)
        self.comboBox_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.comboBox_6.setObjectName("comboBox_6")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.comboBox_6.setFont(font)
        self.lineEdit_27 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_27.setGeometry(QtCore.QRect(480, 205, 161, 20))
        self.lineEdit_27.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_27.setText("")
        self.lineEdit_27.setObjectName("lineEdit_27")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.lineEdit_27.setFont(font)
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setGeometry(QtCore.QRect(370, 200, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_14.setWordWrap(True)
        self.label_14.setObjectName("label_14")
        self.dateEdit = QtWidgets.QDateEdit(self.frame)
        self.dateEdit.setGeometry(QtCore.QRect(150, 130, 161, 22))
        self.dateEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.dateEdit.setFont(font)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.frame)
        self.dateEdit_2.setGeometry(QtCore.QRect(150, 220, 161, 22))
        self.dateEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.dateEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setObjectName("dateEdit_2")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.dateEdit_2.setFont(font)
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setGeometry(QtCore.QRect(150, 280, 161, 81))
        self.listWidget.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"color: rgb(0, 0, 0);")
        self.listWidget.setObjectName("listWidget")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.listWidget.setFont(font)
        self.pushButton_8 = QtWidgets.QPushButton(self.frame, clicked = lambda : self.subtract_item())
        self.pushButton_8.setGeometry(QtCore.QRect(150, 260, 21, 21))
        self.pushButton_8.setAutoFillBackground(False)
        self.pushButton_8.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_8.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_8.setFlat(False)
        self.pushButton_8.setObjectName("pushButton_8")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.pushButton_8.setFont(font)
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(370, 230, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_15.setWordWrap(True)
        self.label_15.setObjectName("label_15")
        self.lineEdit_28 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_28.setGeometry(QtCore.QRect(480, 240, 161, 20))
        self.lineEdit_28.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_28.setText("")
        self.lineEdit_28.setObjectName("lineEdit_28")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.lineEdit_28.setFont(font)
        self.label_35 = QtWidgets.QLabel(self.frame)
        self.label_35.setGeometry(QtCore.QRect(40, 380, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_35.setObjectName("label_35")
        self.comboBox_7 = QtWidgets.QComboBox(self.frame)
        self.comboBox_7.setGeometry(QtCore.QRect(150, 380, 161, 21))
        self.comboBox_7.setAutoFillBackground(False)
        self.comboBox_7.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.setEditable(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.comboBox_7.setFont(font)
        self.label_36 = QtWidgets.QLabel(self.frame)
        self.label_36.setGeometry(QtCore.QRect(370, 370, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_36.setWordWrap(True)
        self.label_36.setObjectName("label_36")
        self.comboBox_8 = QtWidgets.QComboBox(self.frame)
        self.comboBox_8.setGeometry(QtCore.QRect(480, 380, 161, 21))
        self.comboBox_8.setAutoFillBackground(False)
        self.comboBox_8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.setEditable(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.comboBox_8.setFont(font)
        self.label_16 = QtWidgets.QLabel(self.frame)
        self.label_16.setGeometry(QtCore.QRect(250, 500, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setWordWrap(True)
        self.label_16.setObjectName("label_16")
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(80, 530, 70, 17))
        self.checkBox.setObjectName("checkBox")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.checkBox.setFont(font)
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_2.setGeometry(QtCore.QRect(170, 530, 41, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.checkBox_2.setFont(font)
        self.checkBox_3 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_3.setGeometry(QtCore.QRect(220, 530, 70, 17))
        self.checkBox_3.setObjectName("checkBox_3")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.checkBox_3.setFont(font)
        self.checkBox_4 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_4.setGeometry(QtCore.QRect(310, 530, 70, 17))
        self.checkBox_4.setObjectName("checkBox_4")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.checkBox_4.setFont(font)
        self.checkBox_5 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_5.setGeometry(QtCore.QRect(400, 530, 51, 17))
        self.checkBox_5.setObjectName("checkBox_5")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.checkBox_5.setFont(font)
        self.checkBox_6 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_6.setGeometry(QtCore.QRect(560, 530, 70, 17))
        self.checkBox_6.setObjectName("checkBox_6")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.checkBox_6.setFont(font)
        self.checkBox_7 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_7.setGeometry(QtCore.QRect(470, 530, 70, 17))
        self.checkBox_7.setObjectName("checkBox_7")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.checkBox_7.setFont(font)
        self.pushButton_9 = QtWidgets.QPushButton(self.frame, clicked = lambda : self.paid_to_unpaid())
        self.pushButton_9.setGeometry(QtCore.QRect(150, 420, 161, 21))
        self.pushButton_9.setAutoFillBackground(False)
        self.pushButton_9.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_9.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_9.setFlat(False)
        self.pushButton_9.setObjectName("pushButton_9")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.pushButton_9.setFont(font)
        self.pushButton_10 = QtWidgets.QPushButton(self.frame, clicked = lambda : self.unpaid_to_paid())
        self.pushButton_10.setGeometry(QtCore.QRect(480, 420, 161, 21))
        self.pushButton_10.setAutoFillBackground(False)
        self.pushButton_10.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_10.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_10.setFlat(False)
        self.pushButton_10.setObjectName("pushButton_10")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.pushButton_10.setFont(font)
        self.label_37 = QtWidgets.QLabel(self.frame)
        self.label_37.setGeometry(QtCore.QRect(370, 450, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_37.setFont(font)
        self.label_37.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_37.setWordWrap(True)
        self.label_37.setObjectName("label_37")
        self.comboBox_9 = QtWidgets.QComboBox(self.frame)
        self.comboBox_9.setGeometry(QtCore.QRect(480, 460, 161, 21))
        self.comboBox_9.setAutoFillBackground(False)
        self.comboBox_9.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.setEditable(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.comboBox_9.setFont(font)
        self.pushButton = QtWidgets.QPushButton(Dialog, clicked = lambda : self.data_save())
        self.pushButton.setGeometry(QtCore.QRect(310, 680, 75, 31))
        self.pushButton.setStyleSheet("background-color: rgb(255, 230, 207);")
        self.pushButton.setObjectName("pushButton")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.pushButton.setFont(font)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 680, 75, 31))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 230, 207);")
        self.pushButton_2.setObjectName("pushButton_2")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.pushButton_2.setFont(font)
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(40, 80, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(255, 230, 207);")
        self.label_13.setObjectName("label_13")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(240, 40, 251, 22))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.comboBox.setFont(font)
        self.pushButton_7 = QtWidgets.QPushButton(Dialog, clicked = lambda : self.set_deactive())
        self.pushButton_7.setGeometry(QtCore.QRect(550, 40, 151, 23))
        self.pushButton_7.setStyleSheet("background-color: rgb(255, 246, 194);")
        self.pushButton_7.setObjectName("pushButton_7")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.pushButton_7.setFont(font)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog, clicked = lambda : self.delete_employee())
        self.pushButton_3.setGeometry(QtCore.QRect(30, 40, 151, 23))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 246, 194);")
        self.pushButton_3.setObjectName("pushButton_3")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.pushButton_3.setFont(font)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        with open('employee_data.txt', 'r', encoding="utf-8") as f:
            data_objects.employees = json.load(f)


        self.comboBox_6.addItems(['Full-time', 'Part-time'])
        payment_date_options = []
        for i in range(1,29):
            payment_date_options.append(str(i))
        self.comboBox_9.addItems(payment_date_options)

        for employee in data_objects.employees:
            self.comboBox.addItem(employee['name'] + ' ' + employee['surname'])
            new_state = employee['status']



        self.comboBox.currentTextChanged.connect(self.combo_changed)
        self.comboBox.setCurrentIndex(1)
        self.comboBox.setCurrentIndex(0)

        if data_objects.active_auth_level == 1:
            self.comboBox_5.addItems(
                ['Ogretmen', 'Ust Yonetici', 'Mudur', 'Mudur Yardimcisi', 'Sekreter', 'Sofor', 'Temizlik Elemani',
                 'Mutfak Elemani', 'Guvenlik Gorevlisi', 'Psikolog', 'Dil Konusmaci', 'Stajyer'])
            pass
        else:
            self.comboBox_5.addItems(
                ['Ogretmen', 'Mudur', 'Mudur Yardimcisi', 'Sekreter', 'Sofor', 'Temizlik Elemani',
                 'Mutfak Elemani', 'Guvenlik Gorevlisi', 'Psikolog', 'Dil Konusmaci', 'Stajyer'])
            self.lineEdit_27.setDisabled(True)
            self.lineEdit_28.setDisabled(True)
            self.lineEdit_27.hide()
            self.lineEdit_28.hide()
            self.pushButton_3.setDisabled(True)
            self.pushButton_3.hide()
            self.pushButton_7.setDisabled(True)
            self.pushButton_7.hide()
            self.comboBox_9.setDisabled(True)
            self.comboBox_9.hide()
            self.comboBox_8.setDisabled(True)
            self.comboBox_8.hide()
            self.comboBox_7.setDisabled(True)
            self.comboBox_7.hide()
            self.pushButton_9.setDisabled(True)
            self.pushButton_9.hide()
            self.pushButton_10.setDisabled(True)
            self.pushButton_10.hide()
            self.label_14.hide()
            self.label_35.hide()
            self.label_36.hide()
            self.label_37.hide()

    def combo_changed(self):
        self.listWidget.clear()
        for employee in data_objects.employees:
            if self.comboBox.currentText() == employee['name'] + ' ' + employee['surname']:
                if 'Aktif' in employee['status']:
                    self.pushButton_7.setText('Deaktive Et')
                else:
                    self.pushButton_7.setText('Aktive Et')
                try:
                    self.comboBox_7.clear()
                    self.comboBox_8.clear()
                    #self.label_8.setPixmap(employee['photo'])
                    self.comboBox_5.setCurrentText(employee['title'])
                    self.lineEdit.setText(employee['name'])
                    self.lineEdit_2.setText(employee['surname'])
                    self.dateEdit.setDate(datetime.strptime(employee['date_of_birth'], '%Y-%m-%d').date())
                    self.lineEdit_4.setText(employee['identity_no'])
                    self.lineEdit_19.setText(employee['graduation_school'])
                    self.dateEdit_2.setDate(datetime.strptime(employee['graduation_date'], '%Y-%m-%d').date())
                    self.listWidget.addItems(employee['experience'])
                    str_paid = employee['paid_salary'][1:-1]
                    if len(str_paid) > 0:
                        paid_list = str_paid.split(',')
                    else:
                        paid_list = []
                    self.comboBox_7.addItems(paid_list)
                    self.lineEdit_25.setText(employee['phone'])
                    self.lineEdit_26.setText(employee['email'])
                    self.lineEdit_16.setText(employee['address'])
                    self.comboBox_6.setCurrentText(employee['type_employment'])
                    self.lineEdit_27.setText(employee['agreed_salary'])
                    str_unpaid = employee['unpaid_salary'][1:-1]
                    if len(str_unpaid) > 0:
                        unpaid_list = str_unpaid.split(',')
                    else:
                        unpaid_list = []
                    self.comboBox_8.addItems(unpaid_list)
                    self.comboBox_9.setCurrentText(employee['monthly_payment_date'])
                    for day in employee['working_days']:
                        if day == 'Pazartesi':
                            self.checkBox.setChecked(True)
                        if day == 'Sali':
                            self.checkBox_2.setChecked(True)
                        if day == 'Carsamba':
                            self.checkBox_3.setChecked(True)
                        if day == 'Persembe':
                            self.checkBox_4.setChecked(True)
                        if day == 'Cuma':
                            self.checkBox_5.setChecked(True)
                        if day == 'Cumartesi':
                            self.checkBox_6.setChecked(True)
                        if day == 'Pazar':
                            self.checkBox_7.setChecked(True)



                except IndexError:
                    pass
            else:
                pass


    def set_deactive(self):
        global new_state
        import datetime
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Calisani Inaktif Et")
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setText(
            "Calisan deaktive edilecektir. Kabul ediyor musunuz?")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        yesButton = msgBox.button(QMessageBox.Yes)
        yesButton.setText("Evet")
        noButton = msgBox.button(QMessageBox.No)
        noButton.setText("Hayir")
        response = msgBox.exec_()
        for employee in data_objects.employees:
            if self.comboBox.currentText() == employee['name'] + ' ' + employee['surname']:
        # Perform an action based on the user's response
                if response == QMessageBox.Yes and 'Aktif' in employee['status']:
                    current_date = datetime.date.today()
                    formatted_date = current_date.strftime("%d/%m/%Y")
                    new_state = 'Pasif' + '           ' + formatted_date
                elif response == QMessageBox.Yes and 'Pasif' in employee['status']:
                    current_date = datetime.date.today()
                    formatted_date = current_date.strftime("%d/%m/%Y")
                    new_state = 'Aktif' + '           ' + formatted_date
                else:
                    pass

    def delete_employee(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Calisani Sil")
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setText(
            "Calisan sistemden tamamen silinecektir. Kabul ediyor musunuz?")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        yesButton = msgBox.button(QMessageBox.Yes)
        yesButton.setText("Evet")
        noButton = msgBox.button(QMessageBox.No)
        noButton.setText("Hayir")
        response = msgBox.exec_()
        # Perform an action based on the user's response
        if response == QMessageBox.Yes:
            for employee in data_objects.employees:
                if employee['name'] + ' ' + employee['surname'] == self.comboBox.currentText():
                    data_objects.employees.remove(employee)
                    with open("employee_data.txt", "w", encoding="utf-8") as f:
                        f.writelines(json.dumps(data_objects.employees, default=str))
                    data_objects.one_employee = {}

                    with open('employee_data.txt', 'r', encoding="utf-8") as f:
                        data_objects.employees = json.load(f)
                    self.comboBox.removeItem(data_objects.employees.index(employee))
                    self.comboBox.setCurrentIndex(1)
                    self.comboBox.setCurrentIndex(0)

                else:
                    pass
        else:
            pass


    def paid_to_unpaid(self):
        item = self.comboBox_7.currentText()
        self.comboBox_7.removeItem(self.comboBox_7.currentIndex())
        self.comboBox_8.addItem(item)
        salary_unpaid.append(item)
    def unpaid_to_paid(self):
        item = self.comboBox_8.currentText()
        self.comboBox_8.removeItem(self.comboBox_8.currentIndex())
        self.comboBox_7.addItem(item)
        salary_paid.append(item)

    def data_save(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Calisan Verisi Duzenle")
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setText(
            "Girdiginiz bilgileri kontrol ettiyseniz, degisen veriler sisteme kaydedilecektir. Onayliyor musunuz?")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        yesButton = msgBox.button(QMessageBox.Yes)
        yesButton.setText("Evet")
        noButton = msgBox.button(QMessageBox.No)
        noButton.setText("Hayir")
        response = msgBox.exec_()
        # Perform an action based on the user's response
        if response == QMessageBox.Yes:
            self.get_items()
            import datetime
            current_date = datetime.date.today()
            formatted_date = current_date.strftime("%d/%m/%Y")
            formatted_date_2 = current_date.strftime("%Y-%m-%d")
            salary_changed = []
            day_of_work = []
            days = [self.checkBox,self.checkBox_2,self.checkBox_3,self.checkBox_4, self.checkBox_5,self.checkBox_6,self.checkBox_7]
            for day in days:
                if day.isChecked() == True:
                    day_of_work.append(day.text())
                else:
                    pass
            for employee in data_objects.employees:
                if self.comboBox.currentText() == employee['name'] + ' ' + employee['surname']:
                    if len(self.lineEdit_28.text()) > 1:
                        salary_changed.append(self.lineEdit_28.text() + 'TL' + ' / ' + formatted_date)
                    else:
                        salary_changed = employee['salary_change']
                    data_objects.employees[data_objects.employees.index(employee)] = {
                        "title": self.comboBox_5.currentText(),
                        "name": self.lineEdit.text().title(),
                        "surname": self.lineEdit_2.text().title(),
                        "date_of_birth": self.dateEdit.date().toPyDate(),
                        "identity_no": self.lineEdit_4.text().title(),
                        "graduation_school": self.lineEdit_19.text().title(),
                        "graduation_date": self.dateEdit_2.date().toPyDate(),
                        "experience": experience_list,
                        "phone": self.lineEdit_25.text().title(),
                        "email": self.lineEdit_26.text(),
                        "address": self.lineEdit_16.text().title(),
                        "type_employment": self.comboBox_6.currentText(),
                        "agreed_salary": self.lineEdit_27.text().title(),
                        "photo": '-',
                        "status": new_state,
                        "registration_date": employee['registration_date'],
                        "working_days": day_of_work,
                        "salary_change": salary_changed,
                        "teacher_schedule": employee['teacher_schedule'],
                        "teacher_attended": employee['teacher_attended'],
                        "teacher_skipped": employee['teacher_skipped'],
                        "schedule_changed": employee['schedule_changed'],
                        "schedule_cancelled": employee['schedule_cancelled'],
                        "monthly_payment_date": self.comboBox_9.currentText(),
                        "paid_salary": salary_paid,
                        "unpaid_salary": salary_unpaid
                    }
                    # write data to file
                    with open("employee_data.txt", "w", encoding="utf-8") as f:
                        f.writelines(json.dumps(data_objects.employees, default=str))
                    with open('employee_data.txt', 'r', encoding="utf-8") as f:
                        data_objects.employees = json.load(f)

                    connect_database.txt_to_csv('employee_data.txt', 'employee_data.csv')
                    connect_database.upload_files('employee_data.txt')
                    connect_database.upload_files('employee_data.csv')
                else:
                    pass

    def add_item(self):
        text = self.lineEdit_23.text()
        self.listWidget.addItem(text)
        self.lineEdit_23.clear()

    def subtract_item(self):
        current_row = self.listWidget.currentRow()
        if current_row != -1:
            self.listWidget.takeItem(current_row)

    def get_items(self):
        global experience_list
        items = []
        for index in range(self.listWidget.count()):
            items.append(self.listWidget.item(index).text())
        experience_list = items

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Calisan Verilerini Duzenle"))
        self.label_3.setText(_translate("Dialog", "Dogum Tarihi"))
        self.label.setText(_translate("Dialog", "Isim"))
        self.label_2.setText(_translate("Dialog", "Soyisim"))
        self.label_4.setText(_translate("Dialog", "TC Kimlik No"))
        self.label_22.setText(_translate("Dialog", "Adres"))
        self.label_5.setText(_translate("Dialog", "Mezun Oldugu Kurum"))
        self.label_7.setText(_translate("Dialog", "Telefon No"))
        self.pushButton_5.setToolTip(_translate("Dialog", "Fotograf Yukle"))
        self.pushButton_5.setText(_translate("Dialog", "+"))
        self.label_27.setText(_translate("Dialog", "Fotograf Ekle"))
        self.label_9.setText(_translate("Dialog", "Gecmis Kurum /Kurumlar"))
        self.label_10.setText(_translate("Dialog", "Mezuniyet Tarihi"))
        self.pushButton_6.setToolTip(_translate("Dialog", "Fotograf Yukle"))
        self.pushButton_6.setText(_translate("Dialog", "+"))
        self.label_11.setText(_translate("Dialog", "Unvan"))
        self.label_12.setText(_translate("Dialog", "E-mail Adresi"))
        self.label_34.setText(_translate("Dialog", "Calisma Tipi"))
        self.label_14.setText(_translate("Dialog", "Anlasilan Baslangic Ucreti"))
        self.pushButton_8.setToolTip(_translate("Dialog", "Fotograf Yukle"))
        self.pushButton_8.setText(_translate("Dialog", "-"))
        self.label_15.setText(_translate("Dialog", "Yeni Ucret Ekle"))
        self.label_35.setText(_translate("Dialog", "Yapilan Odemeler"))
        self.label_36.setText(_translate("Dialog", "Yapilmayan Odemeler"))
        self.label_16.setText(_translate("Dialog", "Calisma Gunleri:"))
        self.checkBox.setText(_translate("Dialog", "Pazartesi"))
        self.checkBox_2.setText(_translate("Dialog", "Sali"))
        self.checkBox_3.setText(_translate("Dialog", "Casrsamba"))
        self.checkBox_4.setText(_translate("Dialog", "Persembe"))
        self.checkBox_5.setText(_translate("Dialog", "Cuma"))
        self.checkBox_6.setText(_translate("Dialog", "Pazar"))
        self.checkBox_7.setText(_translate("Dialog", "Cumartesi"))
        self.pushButton_9.setToolTip(_translate("Dialog", "Fotograf Yukle"))
        self.pushButton_9.setText(_translate("Dialog", "Secili Odeme Yapilmadi"))
        self.pushButton_10.setToolTip(_translate("Dialog", "Fotograf Yukle"))
        self.pushButton_10.setText(_translate("Dialog", "Secili Odeme Yapildi"))
        self.label_37.setText(_translate("Dialog", "Aylik Odeme Gunu"))
        self.pushButton.setText(_translate("Dialog", "Kaydet"))
        self.pushButton_2.setText(_translate("Dialog", "Vazgec"))
        self.label_13.setText(_translate("Dialog", "   Calisan Bilgileri"))
        self.pushButton_7.setText(_translate("Dialog", "Deaktive Et"))
        self.pushButton_3.setText(_translate("Dialog", "Calisani Sil"))

def change_employee():
    Dialog = QtWidgets.QDialog()
    Dialog.setStyle(QtWidgets.QStyleFactory.create("WindowsVista"))
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    Dialog.exec_()