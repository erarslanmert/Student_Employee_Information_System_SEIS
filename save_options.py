# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'save_options.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import main_page
import data_objects

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(273, 333)
        Dialog.setStyleSheet("background-color: rgb(0, 49, 72);")
        Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.Turkish, QtCore.QLocale.Turkey))
        Dialog.setWindowIcon(QtGui.QIcon("logo_hq.png"))
        self.pushButton = QtWidgets.QPushButton(Dialog, clicked = lambda : dialog_close_ok())
        self.pushButton.setGeometry(QtCore.QRect(40, 260, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 254, 238);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog, clicked = lambda : dialog_close_cancel())
        self.pushButton_2.setGeometry(QtCore.QRect(140, 260, 91, 31))
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
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(60, 130, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_2.setObjectName("radioButton_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 40, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
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
        self.radioButton_4.setGeometry(QtCore.QRect(60, 210, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_4.setDisabled(True)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton.setDisabled(True)
        self.radioButton.toggled.connect(self.radio_activity)
        self.radioButton_2.toggled.connect(self.radio_activity)
        self.radioButton_3.toggled.connect(self.radio_activity)
        self.radioButton_4.toggled.connect(self.radio_activity)

        if data_objects.active_auth_level == 1:
            pass
        if data_objects.active_auth_level == 2:
            self.radioButton_2.setDisabled(True)
        if data_objects.active_auth_level == 3:
            self.radioButton_2.setDisabled(True)
            self.radioButton_4.setDisabled(True)
        if data_objects.active_auth_level == 4:
            self.radioButton_2.setDisabled(True)
            self.radioButton_4.setDisabled(True)
            self.radioButton.setDisabled(True)
            self.radioButton_3.setDisabled(True)

        def dialog_close_ok():
            self.select_save_type()
            Dialog.close()

        def dialog_close_cancel():
            main_page.saving_option = 0
            Dialog.close()

    def radio_activity(self):
        self.pushButton.setEnabled(True)

    def select_save_type(self):
        if self.radioButton.isChecked() == True:
            main_page.saving_option = 1
        if self.radioButton_2.isChecked() == True:
            main_page.saving_option = 2
        if self.radioButton_3.isChecked() == True:
            main_page.saving_option = 3
        if self.radioButton_4.isChecked() == True:
            main_page.saving_option = 4



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Kaydetme Secenekleri"))
        self.pushButton.setText(_translate("Dialog", "Tamam"))
        self.pushButton_2.setText(_translate("Dialog", "Iptal"))
        self.radioButton.setText(_translate("Dialog", "Ogrenci Verilerini Kaydet"))
        self.radioButton_2.setText(_translate("Dialog", "Calisan Verilerini Kaydet"))
        self.label.setText(_translate("Dialog", "Kaydetmek istediginiz veriyi secin"))
        self.radioButton_3.setText(_translate("Dialog", "Genel Cizelgeyi Kaydet"))
        self.radioButton_4.setText(_translate("Dialog", "Genel Istatistikleri Kaydet"))

def open_save_options():
    Dialog = QtWidgets.QDialog()
    Dialog.setStyle(QtWidgets.QStyleFactory.create("WindowsVista"))
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    Dialog.exec_()