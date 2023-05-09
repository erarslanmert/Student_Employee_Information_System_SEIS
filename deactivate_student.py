# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deactivate_student.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import change_student_data


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(264, 283)
        Dialog.setStyleSheet("background-color: rgb(0, 49, 72);")
        Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.Turkish, QtCore.QLocale.Turkey))
        Dialog.setWindowIcon(QtGui.QIcon("logo_hq.png"))
        self.pushButton = QtWidgets.QPushButton(Dialog, clicked = lambda : dialog_close_ok())
        self.pushButton.setGeometry(QtCore.QRect(40, 220, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 254, 238);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 220, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 254, 238);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(60, 90, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog, clicked = lambda : Dialog.close)
        self.radioButton_2.setGeometry(QtCore.QRect(60, 130, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_2.setObjectName("radioButton_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 30, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.radioButton_3 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_3.setGeometry(QtCore.QRect(60, 170, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_3.setObjectName("radioButton_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        def dialog_close_ok():
            self.select_mode()
            Dialog.close()

    def select_mode(self):
        if self.radioButton.isChecked() == True:
            change_student_data.deactivation_mode = 'Kurumdan Ayrildi'
        elif self.radioButton_2.isChecked() == True:
            change_student_data.deactivation_mode = 'Dersleri Tamamladi'
        elif self.radioButton_3.isChecked() == True:
            change_student_data.deactivation_mode = 'Dondurdu'
        else:
            change_student_data.deactivation_mode = ''

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Tamam"))
        self.pushButton_2.setText(_translate("Dialog", "Iptal"))
        self.radioButton.setText(_translate("Dialog", "Kurumdan Ayrildi"))
        self.radioButton_2.setText(_translate("Dialog", "Dersleri Tamamladi"))
        self.label.setText(_translate("Dialog", "Ogrencinin deaktivasyon sebebhini seciniz"))
        self.radioButton_3.setText(_translate("Dialog", "Dondurdu"))

def open_deactivate_student():
    Dialog = QtWidgets.QDialog()
    Dialog.setStyle(QtWidgets.QStyleFactory.create("WindowsVista"))
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    Dialog.exec_()