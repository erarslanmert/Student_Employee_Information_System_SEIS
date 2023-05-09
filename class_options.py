# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_attendence.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import json

from PyQt5 import QtCore, QtGui, QtWidgets
import connect_database
import data_objects
import main_page




class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(353, 600)
        Dialog.setStyleSheet("background-color: rgb(0, 49, 72);")
        Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.Turkish, QtCore.QLocale.Turkey))
        Dialog.setWindowIcon(QtGui.QIcon("logo_hq.png"))

        self.pushButton = QtWidgets.QPushButton(Dialog, clicked = lambda : close_dialog_ok())
        self.pushButton.setGeometry(QtCore.QRect(80, 540, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 254, 238);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog, clicked = lambda : close_dialog_cancel())
        self.pushButton_2.setGeometry(QtCore.QRect(180, 540, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 254, 238);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(100, 70, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_2.setObjectName("radioButton_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 20, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.radioButton_3 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_3.setGeometry(QtCore.QRect(100, 110, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_5 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_5.setGeometry(QtCore.QRect(100, 150, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_5.setObjectName("radioButton_5")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(50, 240, 251, 271))
        self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listWidget.setObjectName("listWidget")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.listWidget.setFont(font)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog, clicked = lambda : self.add_item())
        self.pushButton_3.setGeometry(QtCore.QRect(270, 190, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 254, 238);\n"
                                        "background-color: rgb(226, 226, 226);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog, clicked = lambda : self.subtract_item())
        self.pushButton_4.setGeometry(QtCore.QRect(50, 190, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 254, 238);\n"
                                        "background-color: rgb(226, 226, 226);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(90, 192, 171, 25))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.comboBox.setFont(font)

        self.comboBox.setDisabled(True)
        self.pushButton_3.setDisabled(True)
        self.pushButton_4.setDisabled(True)
        self.pushButton.setDisabled(True)

        self.radioButton_2.toggled.connect(self.normal_class_availablity)
        self.radioButton_5.toggled.connect(self.normal_class_availablity)
        self.radioButton_3.toggled.connect(self.group_class_availablity)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        def close_dialog_cancel():
            self.press_cancel()
            Dialog.close()

        def close_dialog_ok():
            self.press_okay()
            Dialog.close()


    def group_class_availablity(self):
        self.comboBox.setEnabled(True)
        self.pushButton_3.setEnabled(True)
        self.pushButton_4.setEnabled(True)
        self.pushButton.setEnabled(True)
        for student in data_objects.students:
            self.comboBox.addItem((student['name']) + ' ' + (student['surname']))

    def normal_class_availablity(self):
        self.comboBox.setEnabled(True)
        self.pushButton_3.setDisabled(True)
        self.pushButton_4.setDisabled(True)
        self.pushButton.setEnabled(True)
        for student in data_objects.students:
            self.comboBox.addItem((student['name']) + ' ' + (student['surname']))

    def pushbutton_unavailablity(self):
        self.comboBox.setDisabled(True)
        self.pushButton_3.setDisabled(True)
        self.pushButton_4.setDisabled(True)
        self.pushButton.setEnabled(True)
        self.comboBox.clear()
        self.listWidget.clear()


    def press_okay(self):

        if self.radioButton_2.isChecked() == True:
            main_page.radio_button_selected = 2
            main_page.group_class_list.append(self.comboBox.currentText())
        if self.radioButton_3.isChecked() == True:
            self.get_items()
            main_page.radio_button_selected = 3
        if self.radioButton_5.isChecked() == True:
            main_page.radio_button_selected = 5
            main_page.group_class_list.append(self.comboBox.currentText())

        self.radioButton_2.setChecked(False)
        self.radioButton_3.setChecked(False)
        self.radioButton_5.setChecked(False)



    def press_cancel(self):
        self.comboBox.clear()
        self.listWidget.clear()
        self.radioButton_2.setChecked(False)
        self.radioButton_3.setChecked(False)
        self.radioButton_5.setChecked(False)
        main_page.radio_button_selected = 0

    def add_item(self):
        text = self.comboBox.currentText()
        self.listWidget.addItem(text)
        self.comboBox.removeItem(self.comboBox.currentIndex())

    def subtract_item(self):
        current_row = self.listWidget.currentRow()
        if current_row != -1:
            current_item = self.listWidget.currentItem()
            self.comboBox.addItem(current_item.text())
            self.listWidget.takeItem(current_row)

    def get_items(self):
        items = []
        for index in range(self.listWidget.count()):
            items.append(self.listWidget.item(index).text())
        main_page.group_class_list = items

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Ders Bilgisi Ekleme Sayfasi"))
        self.pushButton.setText(_translate("Dialog", "Tamam"))
        self.pushButton_2.setText(_translate("Dialog", "Iptal"))
        self.radioButton_2.setText(_translate("Dialog", "Akademik Ders Ekle"))
        self.label.setText(_translate("Dialog", "Eklemek istediginiz veriyi secin"))
        self.radioButton_3.setText(_translate("Dialog", "Grup Dersi Ekle"))
        self.radioButton_5.setText(_translate("Dialog", "Attentioner Ders Ekle"))
        self.pushButton_3.setText(_translate("Dialog", "+"))
        self.pushButton_4.setText(_translate("Dialog", "-"))

def open_class_options():
    Dialog = QtWidgets.QDialog()
    Dialog.setStyle(QtWidgets.QStyleFactory.create("WindowsVista"))
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    Dialog.exec_()