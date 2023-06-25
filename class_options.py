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


class_type = 0
if_cancelled = 0

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(353, 415)
        Dialog.setStyleSheet("background-color: rgb(0, 49, 72);")
        Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.Turkish, QtCore.QLocale.Turkey))
        Dialog.setWindowIcon(QtGui.QIcon("logo_hq.png"))

        self.pushButton = QtWidgets.QPushButton(Dialog, clicked = lambda : close_dialog_ok())
        self.pushButton.setGeometry(QtCore.QRect(80, 360, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 254, 238);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog, clicked = lambda : close_dialog_cancel())
        self.pushButton_2.setGeometry(QtCore.QRect(180, 360, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 254, 238);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(50, 70, 251, 271))
        self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listWidget.setObjectName("listWidget")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.listWidget.setFont(font)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog, clicked = lambda : self.add_item())
        self.pushButton_3.setGeometry(QtCore.QRect(270, 30, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 254, 238);\n"
                                        "background-color: rgb(226, 226, 226);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog, clicked = lambda : self.subtract_item())
        self.pushButton_4.setGeometry(QtCore.QRect(50, 30, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 254, 238);\n"
                                        "background-color: rgb(226, 226, 226);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(90, 32, 171, 25))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.comboBox.setFont(font)
        self.pushButton.setDisabled(True)

        for student in data_objects.students:
            self.comboBox.addItem((student['name']) + ' ' + (student['surname']))


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        def close_dialog_cancel():
            self.press_cancel()
            Dialog.close()

        def close_dialog_ok():
            self.press_okay()
            Dialog.close()

        for student in data_objects.students:
            self.comboBox.addItem((student['name']) + ' ' + (student['surname']))


    def press_okay(self):
        global if_cancelled
        self.get_items()
        if_cancelled = 0

    def press_cancel(self):
        global if_cancelled
        self.comboBox.clear()
        self.listWidget.clear()
        if_cancelled = 1

    def add_item(self):
        text = self.comboBox.currentText()
        self.listWidget.addItem(text)
        self.comboBox.removeItem(self.comboBox.currentIndex())
        if class_type == 1 or class_type == 2:
            self.pushButton_3.setDisabled(True)
            self.pushButton_4.setDisabled(True)
            self.comboBox.clear()
            self.comboBox.setDisabled(True)
            self.pushButton.setEnabled(True)
        elif class_type == 3:
            self.pushButton.setEnabled(True)
        else:
            pass

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
        self.pushButton_3.setText(_translate("Dialog", "+"))
        self.pushButton_4.setText(_translate("Dialog", "-"))

def open_class_options():
    Dialog = QtWidgets.QDialog()
    Dialog.setStyle(QtWidgets.QStyleFactory.create("WindowsVista"))
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    Dialog.exec_()