# -*- coding: utf-8 -*-

import json
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QStyleFactory, QMessageBox

import connect_database
import data_objects
import smtplib

class Ui_Dialog(object):
        def setupUi(self, Dialog):
                Dialog.setObjectName("Dialog")
                Dialog.resize(620, 703)
                Dialog.setStyleSheet("background-color: rgb(0, 41, 61);\n"
                                         "selection-background-color: rgb(255, 255, 255);")
                Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.Turkish, QtCore.QLocale.Turkey))
                self.pushButton = QtWidgets.QPushButton(Dialog, clicked=lambda: close_dialog_ok())
                self.pushButton.setGeometry(QtCore.QRect(204, 630, 111, 41))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(11)
                self.pushButton.setFont(font)
                self.pushButton.setStyleSheet("background-color: rgb(255, 230, 207);")
                self.pushButton.setObjectName("pushButton")
                self.pushButton_2 = QtWidgets.QPushButton(Dialog, clicked=lambda: Dialog.close())
                self.pushButton_2.setGeometry(QtCore.QRect(320, 630, 101, 41))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(11)
                self.pushButton_2.setFont(font)
                self.pushButton_2.setStyleSheet("background-color: rgb(255, 230, 207);")
                self.pushButton_2.setObjectName("pushButton_2")
                self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)
                self.lineEdit_6.setGeometry(QtCore.QRect(211, 150, 350, 31))
                self.lineEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.lineEdit_6.setObjectName("lineEdit_6")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(9)
                font.setItalic(False)
                self.lineEdit_6.setFont(font)
                self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
                self.lineEdit_4.setGeometry(QtCore.QRect(211, 210, 350, 31))
                self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.lineEdit_4.setObjectName("lineEdit_4")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(9)
                font.setItalic(False)
                self.lineEdit_4.setFont(font)
                self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
                self.lineEdit_5.setGeometry(QtCore.QRect(211, 270, 350, 31))
                self.lineEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.lineEdit_5.setObjectName("lineEdit_5")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(9)
                font.setItalic(False)
                self.lineEdit_5.setFont(font)
                self.lineEdit_7 = QtWidgets.QLineEdit(Dialog)
                self.lineEdit_7.setGeometry(QtCore.QRect(211, 330, 350, 31))
                self.lineEdit_7.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.lineEdit_7.setObjectName("lineEdit_7")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(9)
                font.setItalic(False)
                self.lineEdit_7.setFont(font)
                self.lineEdit = QtWidgets.QLineEdit(Dialog)
                self.lineEdit.setGeometry(QtCore.QRect(211, 390, 350, 31))
                self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.lineEdit.setObjectName("lineEdit")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(9)
                font.setItalic(False)
                self.lineEdit.setFont(font)
                self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
                self.lineEdit_2.setGeometry(QtCore.QRect(211, 450, 350, 31))
                self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.lineEdit_2.setObjectName("lineEdit_2")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(9)
                font.setItalic(False)
                self.lineEdit_2.setFont(font)
                self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
                self.lineEdit_3.setGeometry(QtCore.QRect(211, 510, 350, 31))
                self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.lineEdit_3.setObjectName("lineEdit_3")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(9)
                font.setItalic(False)
                self.lineEdit_3.setFont(font)
                self.label = QtWidgets.QLabel(Dialog)
                self.label.setGeometry(QtCore.QRect(60, 390, 150, 31))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(12)
                font.setStyleStrategy(QtGui.QFont.PreferDefault)
                self.label.setFont(font)
                self.label.setMouseTracking(False)
                self.label.setStyleSheet("color:  rgb(255, 230, 207);\n"
                                         "")
                self.label.setAlignment(QtCore.Qt.AlignLeft)
                self.label.setObjectName("label")
                self.label_2 = QtWidgets.QLabel(Dialog)
                self.label_2.setGeometry(QtCore.QRect(60, 450, 150, 31))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(12)
                font.setStyleStrategy(QtGui.QFont.PreferDefault)
                self.label_2.setFont(font)
                self.label_2.setMouseTracking(False)
                self.label_2.setStyleSheet("color:  rgb(255, 230, 207);")
                self.label_2.setAlignment(QtCore.Qt.AlignLeft)
                self.label_2.setObjectName("label_2")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(9)
                font.setItalic(False)
                self.label_2.setFont(font)
                self.label_4 = QtWidgets.QLabel(Dialog)
                self.label_4.setGeometry(QtCore.QRect(270, 20, 91, 91))
                self.label_4.setText("")
                self.label_4.setPixmap(QtGui.QPixmap("logo_hq.png"))
                self.label_4.setScaledContents(True)
                self.label_4.setObjectName("label_4")
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(9)
                font.setItalic(False)
                self.label_4.setFont(font)
                self.label_3 = QtWidgets.QLabel(Dialog)
                self.label_3.setGeometry(QtCore.QRect(60, 510, 150, 31))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(12)
                font.setStyleStrategy(QtGui.QFont.PreferDefault)
                self.label_3.setFont(font)
                self.label_3.setMouseTracking(False)
                self.label_3.setStyleSheet("color:  rgb(255, 230, 207);")
                self.label_3.setAlignment(QtCore.Qt.AlignLeft)
                self.label_3.setObjectName("label_3")

                self.label_5 = QtWidgets.QLabel(Dialog)
                self.label_5.setGeometry(QtCore.QRect(60, 270, 150, 31))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(12)
                font.setStyleStrategy(QtGui.QFont.PreferDefault)
                self.label_5.setFont(font)
                self.label_5.setMouseTracking(False)
                self.label_5.setStyleSheet("color:  rgb(255, 230, 207);")
                self.label_5.setAlignment(QtCore.Qt.AlignLeft)
                self.label_5.setObjectName("label_5")

                self.label_6 = QtWidgets.QLabel(Dialog)
                self.label_6.setGeometry(QtCore.QRect(60, 150, 150, 31))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(12)
                font.setStyleStrategy(QtGui.QFont.PreferDefault)
                self.label_6.setFont(font)
                self.label_6.setMouseTracking(False)
                self.label_6.setStyleSheet("color:  rgb(255, 230, 207);\n"
                                           "")
                self.label_6.setAlignment(QtCore.Qt.AlignLeft)
                self.label_6.setObjectName("label_6")
                self.label_7 = QtWidgets.QLabel(Dialog)
                self.label_7.setGeometry(QtCore.QRect(60, 210, 150, 31))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(12)
                font.setStyleStrategy(QtGui.QFont.PreferDefault)
                self.label_7.setFont(font)
                self.label_7.setMouseTracking(False)
                self.label_7.setStyleSheet("color:  rgb(255, 230, 207);")
                self.label_7.setAlignment(QtCore.Qt.AlignLeft)
                self.label_7.setObjectName("label_7")
                self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)
                self.lineEdit_6.setGeometry(QtCore.QRect(211, 150, 350, 31))
                self.lineEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.lineEdit_6.setObjectName("lineEdit_6")

                self.label_8 = QtWidgets.QLabel(Dialog)
                self.label_8.setGeometry(QtCore.QRect(60, 330, 150, 31))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(12)
                font.setStyleStrategy(QtGui.QFont.PreferDefault)
                self.label_8.setFont(font)
                self.label_8.setMouseTracking(False)
                self.label_8.setStyleSheet("color:  rgb(255, 230, 207);")
                self.label_8.setAlignment(QtCore.Qt.AlignLeft)
                self.label_8.setObjectName("label_8")
                self.label_9 = QtWidgets.QLabel(Dialog)
                self.label_9.setGeometry(QtCore.QRect(100, 560, 431, 51))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(10)
                font.setStyleStrategy(QtGui.QFont.PreferDefault)
                self.label_9.setFont(font)
                self.label_9.setMouseTracking(False)
                self.label_9.setStyleSheet("color:  rgb(255, 230, 207);")
                self.label_9.setAlignment(QtCore.Qt.AlignCenter)
                self.label_9.setWordWrap(True)
                self.label_9.setObjectName("label_9")
                self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
                self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
                self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
                self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
                self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
                self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
                self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
                self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
                self.lineEdit_7.setAlignment(QtCore.Qt.AlignCenter)
                self.pushButton.setDisabled(True)

                self.retranslateUi(Dialog)
                QtCore.QMetaObject.connectSlotsByName(Dialog)

                self.lineEdit.textEdited.connect(self.enable_okay_button)
                self.lineEdit_2.textEdited.connect(self.enable_okay_button)
                self.lineEdit_3.textEdited.connect(self.enable_okay_button)
                self.lineEdit_4.textEdited.connect(self.enable_okay_button)
                self.lineEdit_5.textEdited.connect(self.enable_okay_button)
                self.lineEdit_6.textEdited.connect(self.enable_okay_button)
                self.lineEdit_7.textEdited.connect(self.enable_okay_button)

                self.ready_to_close = False

                def close_dialog_ok():
                        self.insert_user_db()
                        if self.ready_to_close == True:
                                Dialog.close()
                        else:
                                pass

        def enable_okay_button(self):
                if self.lineEdit.text() and self.lineEdit_2.text() and self.lineEdit_3.text() and self.lineEdit_4.text() and self.lineEdit_5.text() and self.lineEdit_6.text() and self.lineEdit_7.text():
                        self.pushButton.setEnabled(True)
                else:
                        self.pushButton.setDisabled(True)

        def insert_user_db(self):
                with open('employee_data.txt', 'r', encoding="utf-8") as f:
                        data_objects.employees = json.load(f)
                with open('user_list.txt', 'r', encoding="utf-8") as f:
                        data_objects.users = json.load(f)
                employee_found = False
                employee_matched = {}
                user_found = False
                for user in data_objects.users:
                        if self.lineEdit_6.text().title() == user['name'] and self.lineEdit_4.text().title() == \
                                user['surname']:
                                error_box = QMessageBox()
                                error_box.setIcon(QMessageBox.Critical)
                                error_box.setWindowTitle("Error")
                                error_box.setText("Calisan icin bir hesap mevcut!")
                                error_box.setInformativeText(
                                        "Sisteme kayitli calisan icin kullanici hesabi mevcut!")
                                error_box.exec_()
                                self.lineEdit_6.clear()
                                self.lineEdit_4.clear()
                                user_found = True
                                break
                        else:
                                pass

                if user_found == False:
                        for employee in data_objects.employees:
                                if self.lineEdit_6.text().title() == employee[
                                        'name'] and self.lineEdit_4.text().title() == employee['surname'] and employee['title'] in ['Ogretmen', 'Ust Yonetici', 'Mudur', 'Mudur Yardimcisi', 'Sekreter', 'Psikolog', 'Dil Konusmaci']:
                                        employee_found = True
                                        employee_matched = employee
                                        break
                                else:
                                        pass
                if employee_found == False:
                        error_box = QMessageBox()
                        error_box.setIcon(QMessageBox.Critical)
                        error_box.setWindowTitle("Error")
                        error_box.setText("Calisan kayitli degil!")
                        error_box.setInformativeText(
                                "Lutfen sisteme kayitli ve erisime uygun bir calisan ismi girin. Birden fazla isminiz var ise tum isimlerinizi arada bir adet bosluk birakarak yazin. Turkce karakterler kullanmayin. Eger sisteme kayitli oldugunuzu dusunuyorsaniz ust yoneticiniz ile iletisime gecin.")
                        error_box.setStandardButtons(QMessageBox.Ok)
                        error_box.exec_()
                        self.lineEdit_6.clear()
                        self.lineEdit_4.clear()
                else:
                        if employee_matched['title'] == 'Ust Yonetici':
                                auth_level = 1
                        elif employee_matched['title'] == 'Mudur' or employee_matched[
                                'title'] == 'Mudur Yardimcisi':
                                auth_level = 2
                        elif employee_matched['title'] == 'Sekreter':
                                auth_level = 3
                        elif employee_matched['title'] == 'Ogretmen' or employee_matched[
                                'title'] == 'Psikolog' or employee_matched[
                                'title'] == 'Dil Konusmaci':
                                auth_level = 4
                        else:
                                auth_level = 0
                        if self.lineEdit_2.text() != self.lineEdit_3.text():
                                error_box = QMessageBox()
                                error_box.setIcon(QMessageBox.Critical)
                                error_box.setWindowTitle("Error")
                                error_box.setText("Sifre tekrari ile uyusmuyor!")
                                error_box.setInformativeText(
                                        "Sifreniz sifre tekrari ile uyusmamaktadir. Lutfen tekrar sifrenizi ve tekrarini giriniz!")
                                error_box.setStandardButtons(QMessageBox.Ok)
                                error_box.exec_()
                                self.lineEdit_2.clear()
                                self.lineEdit_3.clear()
                                self.pushButton.setDisabled(True)
                        else:
                                msgBox = QMessageBox()
                                msgBox.setWindowTitle("Kullanici Olusturuluyor")
                                msgBox.setIcon(QMessageBox.Question)
                                msgBox.setText(
                                        "Girdiginiz bilgileri kontrol ettiyseniz, yeni kullanici hesabi olusturulacaktir, onayliyor musunuz?")
                                msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                                yesButton = msgBox.button(QMessageBox.Yes)
                                yesButton.setText("Evet")
                                noButton = msgBox.button(QMessageBox.No)
                                noButton.setText("Hayir")
                                response = msgBox.exec_()
                                # Perform an action based on the user's response
                                if response == QMessageBox.Yes:
                                        data_objects.one_user = {
                                                "name": self.lineEdit_6.text().title(),
                                                "surname": self.lineEdit_4.text().title(),
                                                "email": self.lineEdit_5.text(),
                                                "phone": self.lineEdit_7.text(),
                                                "user_name": self.lineEdit.text(),
                                                "password": self.lineEdit_2.text(),
                                                "auth_level": auth_level
                                        }
                                        data_objects.users.append(data_objects.one_user)
                                        with open("user_list.txt", "w", encoding="utf-8") as f:
                                                f.writelines(json.dumps(data_objects.users, default=str))
                                        info_box = QMessageBox()
                                        info_box.setIcon(QMessageBox.Information)
                                        info_box.setWindowTitle("Info")
                                        info_box.setText("Kullanici Eklendi.")
                                        info_box.setInformativeText("Kullanici basariyla eklenmistir!.")
                                        info_box.setStandardButtons(QMessageBox.Ok)
                                        info_box.exec_()
                                        self.ready_to_close = True
                                        '''connect_database.upload_files('user_list.txt')
                                        connect_database.txt_to_csv('user_list.txt','user_list.csv')
                                        connect_database.upload_files('user_list.csv')'''
                                else:
                                        pass

        def retranslateUi(self, Dialog):
                _translate = QtCore.QCoreApplication.translate
                Dialog.setWindowTitle(_translate("Dialog", "Giris Ekrani"))
                self.pushButton.setText(_translate("Dialog", "Kayit Ol"))
                self.pushButton_2.setText(_translate("Dialog", "Iptal"))
                self.label.setText(_translate("Dialog", "Kullanici Ismi"))
                self.label_2.setText(_translate("Dialog", "Sifre"))
                self.label_3.setText(_translate("Dialog", "Sifre Tekrar"))
                self.label_5.setText(_translate("Dialog", "Email Adresi"))
                self.label_6.setText(_translate("Dialog", "Isim"))
                self.label_7.setText(_translate("Dialog", "Soyisim"))
                self.label_8.setText(_translate("Dialog", "Telefon No"))
                self.label_9.setText(_translate("Dialog",
                                                "Bu ekranda girilen verilerin, veritabani ile eslesmesi halinde kaydiniz otomatik olarak onaylanacaktir"))

def open_new_user():
        Dialog = QtWidgets.QDialog()
        Dialog.setStyle(QtWidgets.QStyleFactory.create("WindowsVista"))
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()
