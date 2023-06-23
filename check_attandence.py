# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'attandence.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import json

from PyQt5.QtWidgets import QMessageBox

import connect_database
from PyQt5 import QtCore, QtGui, QtWidgets
import main_page, data_objects


attended_class_list = []
attandence_class = ' '
check_group = ' '
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(353, 495)
        Dialog.setStyleSheet("background-color: rgb(0, 94, 138);")
        Dialog.setWindowIcon(QtGui.QIcon("logo_hq.png"))
        Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.Turkish, QtCore.QLocale.Turkey))
        Dialog.setWindowIcon(QtGui.QIcon("logo_hq.png"))
        self.pushButton = QtWidgets.QPushButton(Dialog, clicked = lambda : close_dialog_ok())
        self.pushButton.setGeometry(QtCore.QRect(80, 428, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 254, 238);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog,clicked = lambda : close_dialog_cancel())
        self.pushButton_2.setGeometry(QtCore.QRect(180, 428, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 254, 238);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 70, 231, 31))
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
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(50, 158, 251, 241))
        self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listWidget.setObjectName("listWidget")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.listWidget.setFont(font)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog, clicked = lambda : self.add_item())
        self.pushButton_3.setGeometry(QtCore.QRect(270, 118, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 254, 238);\n"
                                        "background-color: rgb(226, 226, 226);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog, clicked = lambda : self.subtract_item())
        self.pushButton_4.setGeometry(QtCore.QRect(50, 118, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 254, 238);\n"
                                        "background-color: rgb(226, 226, 226);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(90, 120, 171, 25))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.comboBox.setFont(font)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 18, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")

        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setDisabled(True)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.add_students()

        def close_dialog_cancel():
            self.press_cancel()
            Dialog.close()

        def close_dialog_ok():
            self.press_okay()
            Dialog.close()

    def lock_widgets(self):
        self.pushButton.setEnabled(True)
        self.pushButton_3.setDisabled(True)
        self.pushButton_4.setDisabled(True)
        self.comboBox.setDisabled(True)

    def add_students(self):
        self.comboBox.clear()
        self.pushButton.setEnabled(True)
        self.comboBox.setEnabled(True)
        student_list = []
        for student in data_objects.students:
            for schedule in student['student_schedule']:
                if attandence_class in schedule:
                    student_list.append(student['name'] + ' ' + student['surname'])
        self.comboBox.addItems(student_list)
        self.comboBox.model().sort(0)

    def press_cancel(self):
        self.listWidget.clear()
        self.comboBox.clear()

    def press_okay(self):
        global attended_class_list, check_group
        self.get_items()
        lesson_teacher = ''
        student_list = attended_class_list
        teacher = ''
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Yoklama Sayfasi")
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setText(
            "Yoklama listesine herhangi bir ogrenci eklemediniz. Listeye eklenmeyen ogrenciler yoklamada devamsizlik yapmis sayilacaktir. Onayliyor musunuz?")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        yesButton = msgBox.button(QMessageBox.Yes)
        yesButton.setText("Evet")
        noButton = msgBox.button(QMessageBox.No)
        noButton.setText("Hayir")
        response = msgBox.exec_()
        # Perform an action based on the user's response
        if response == QMessageBox.Yes:
            if "Grup" in check_group and len(student_list)>1:
                for student in data_objects.students:
                    for schedule in student['student_schedule']:
                        if attandence_class in schedule:
                            if (student['name'] + ' ' + student['surname']) in student_list:
                                student['student_schedule'].remove(schedule)
                                student['student_attended'].append(schedule)
                                teacher_list = attandence_class.split()
                                teacher = teacher_list[0] + ' ' + teacher_list[1]
                                lesson_teacher = attandence_class.replace(teacher,'')
                            else:
                                teacher_list = attandence_class.split()
                                teacher = teacher_list[0] + ' ' + teacher_list[1]
                                lesson_teacher = attandence_class.replace(teacher, '')
                                student['student_schedule'].remove(schedule)
                                student['student_skipped'].append(schedule)

                for employee in data_objects.employees:
                    for schedule in employee['teacher_schedule']:
                        if lesson_teacher in schedule:
                            employee['teacher_schedule'].remove(schedule)
                            employee['teacher_attended'].append(schedule)

            else:
                for student in data_objects.students:
                    for schedule in student['student_schedule']:
                        if attandence_class in schedule:
                            if (student['name'] + ' ' + student['surname']) in student_list:
                                student['student_schedule'].remove(schedule)
                                student['student_attended'].append(schedule)
                                teacher_list = attandence_class.split()
                                teacher = teacher_list[0] + ' ' + teacher_list[1]
                                lesson_teacher = attandence_class.replace(teacher, '')
                            else:
                                student['student_schedule'].remove(schedule)
                                student['student_skipped'].append(schedule)
                for employee in data_objects.employees:
                    for schedule in employee['teacher_schedule']:
                        if lesson_teacher in schedule:
                            employee['teacher_schedule'].remove(schedule)
                            employee['teacher_attended'].append(schedule)
        else:
            pass


        with open("student_data.txt", "w", encoding="utf-8") as f:
            f.writelines(json.dumps(data_objects.students, default=str))
        with open('student_data.txt', 'r', encoding="utf-8") as f:
            data_objects.students = json.load(f)
        with open("employee_data.txt", "w", encoding="utf-8") as f:
            f.writelines(json.dumps(data_objects.employees, default=str))
        with open('employee_data.txt', 'r', encoding="utf-8") as f:
            data_objects.employees = json.load(f)
        '''connect_database.txt_to_csv('employee_data.txt', 'employee_data.csv')
        connect_database.txt_to_csv('student_data.txt', 'student_data.csv')
        connect_database.upload_files('student_data.txt')
        connect_database.upload_files('employee_data.txt')
        connect_database.upload_files('student_data.csv')
        connect_database.upload_files('employee_data.csv')'''


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
        global attended_class_list
        items = []
        for index in range(self.listWidget.count()):
            items.append(self.listWidget.item(index).text())
        attended_class_list = items

    def retranslateUi(self, Dialog):
        global attandence_class
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Ders Bilgisi Ekleme Sayfasi"))
        self.pushButton.setText(_translate("Dialog", "Tamam"))
        self.pushButton_2.setText(_translate("Dialog", "Iptal"))
        self.label.setText(_translate("Dialog", "Lutfen Derse Gelen Ogrencileri Listeye Ekleyin"))
        self.pushButton_3.setText(_translate("Dialog", "+"))
        self.pushButton_4.setText(_translate("Dialog", "-"))
        self.label_2.setText(_translate("Dialog", "{}".format(str(attandence_class))))


def open_attandence():
    Dialog = QtWidgets.QDialog()
    Dialog.setStyle(QtWidgets.QStyleFactory.create("WindowsVista"))
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    Dialog.exec_()