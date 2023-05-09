# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change_data_options.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import connect_database
import data_objects
import delete_lesson
import delete_user
import general_statistics_dashboard
import change_employee_data
import change_student_data

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(324, 345)
        Dialog.setStyleSheet("background-color: rgb(0, 49, 72);")
        Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.Turkish, QtCore.QLocale.Turkey))
        Dialog.setWindowIcon(QtGui.QIcon("logo_hq.png"))
        self.pushButton = QtWidgets.QPushButton(Dialog, clicked = lambda : dialog_close_ok())
        self.pushButton.setGeometry(QtCore.QRect(70, 290, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 254, 238);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog, clicked = lambda : dialog_close_cancel())
        self.pushButton_2.setGeometry(QtCore.QRect(170, 290, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 254, 238);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(60, 90, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(60, 130, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_2.setObjectName("radioButton_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 20, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
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
        self.radioButton_4 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_4.setGeometry(QtCore.QRect(60, 210, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_5.setGeometry(QtCore.QRect(60, 250, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_5.setObjectName("radioButton_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton.setDisabled(True)
        self.radioButton.toggled.connect(self.radio_activity)
        self.radioButton_2.toggled.connect(self.radio_activity)
        self.radioButton_3.toggled.connect(self.radio_activity)
        self.radioButton_4.toggled.connect(self.radio_activity)
        self.radioButton_5.toggled.connect(self.radio_activity)

        def dialog_close_ok():
            self.press_okay()
            Dialog.close()

        def dialog_close_cancel():
            Dialog.close()

        if data_objects.active_auth_level == 2:
            self.radioButton_4.setDisabled(True)
        elif data_objects.active_auth_level == 3:
            self.radioButton.setDisabled(True)
            self.radioButton_3.setDisabled(True)
            self.radioButton_4.setDisabled(True)
        else:
            pass

    def radio_activity(self):
        self.pushButton.setEnabled(True)

    def press_okay(self):
        if self.radioButton.isChecked() == True:
            general_statistics_dashboard.barchart_general()
        if self.radioButton_2.isChecked() == True:
            change_student_data.change_student()
        if self.radioButton_3.isChecked() == True:
            change_employee_data.change_employee()
        if self.radioButton_4.isChecked() == True:
            delete_user.open_delete_user()
        if self.radioButton_5.isChecked() == True:
            delete_lesson.open_delete_lesson()


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Goruntuleme Secenekleri"))
        self.pushButton.setText(_translate("Dialog", "Tamam"))
        self.pushButton_2.setText(_translate("Dialog", "Iptal"))
        self.radioButton.setText(_translate("Dialog", "Kurum Istatistiklerini Goruntule"))
        self.radioButton_2.setText(_translate("Dialog", "Ogrenci Verilerini Duzenle"))
        self.label.setText(_translate("Dialog", "Bu veriler sadece ozel erisimi olan yoneticiler tarafindan tarafindan gorulebilirve duzenlenebilir!"))
        self.radioButton_3.setText(_translate("Dialog", "Calisan Verilerini Duzenle"))
        self.radioButton_4.setText(_translate("Dialog", "Kullanici Hesabi Sil"))
        self.radioButton_5.setText(_translate("Dialog", "Genel Cizelgeden Ders Sil"))

def open_change_options():
    Dialog = QtWidgets.QDialog()
    Dialog.setStyle(QtWidgets.QStyleFactory.create("WindowsVista"))
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    Dialog.exec_()