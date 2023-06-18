# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete_user.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import json

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import connect_database
import data_objects


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(324, 190)
        Dialog.setStyleSheet("background-color: rgb(0, 85, 127);")
        Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.Turkish, QtCore.QLocale.Turkey))
        Dialog.setWindowIcon(QtGui.QIcon("logo_hq.png"))
        self.pushButton = QtWidgets.QPushButton(Dialog, clicked = lambda : close_dialog_ok())
        self.pushButton.setGeometry(QtCore.QRect(70, 120, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 254, 238);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog, clicked = lambda : Dialog.close())
        self.pushButton_2.setGeometry(QtCore.QRect(170, 120, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 254, 238);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(30, 60, 261, 31))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.comboBox.setFont(font)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 20, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton.setDisabled(True)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        for user in data_objects.users:
            self.comboBox.addItem(user['name'] + ' ' + user['surname'] + ' ' + '(' + user['user_name'] + ')')

        self.comboBox.currentTextChanged.connect(self.combo_activity)

        def close_dialog_ok():
            self.remove_user()
            Dialog.close()

    def combo_activity(self):
        self.pushButton.setEnabled(True)

    def remove_user(self):
        selected_user = {}
        selected = False
        for user in data_objects.users:
            if user['name'] in self.comboBox.currentText() and user['surname'] in self.comboBox.currentText() and user['user_name'] in self.comboBox.currentText():
                selected = True
                selected_user = user
            else:
                pass
        if selected == True:
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Kullanici Siliniyor")
            msgBox.setIcon(QMessageBox.Question)
            msgBox.setText(
                "Secili kullanici hesabi kalici olarak silinecektir. Sistemi kullanabilmek icin, calisanin yeni bir hesap olusturmasi gerekecektir. Onayliyor musunuz?")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            yesButton = msgBox.button(QMessageBox.Yes)
            yesButton.setText("Evet")
            noButton = msgBox.button(QMessageBox.No)
            noButton.setText("Hayir")
            response = msgBox.exec_()
            # Perform an action based on the user's response
            if response == QMessageBox.Yes:
                data_objects.users.remove(selected_user)
                with open("user_list.txt", "w", encoding="utf-8") as f:
                    f.writelines(json.dumps(data_objects.users, default=str))
                '''connect_database.upload_files('user_list.txt')
                connect_database.txt_to_csv('user_list.txt', 'user_list.csv')
                connect_database.upload_files('user_list.csv')'''
            else:
                pass

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Kullanici Sil"))
        self.pushButton.setText(_translate("Dialog", "Sil"))
        self.pushButton_2.setText(_translate("Dialog", "Iptal"))
        self.label.setText(_translate("Dialog", "Silinecek Kullaniciyi Seciniz!"))

def open_delete_user():
    Dialog = QtWidgets.QDialog()
    Dialog.setStyle(QtWidgets.QStyleFactory.create("WindowsVista"))
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    Dialog.exec_()