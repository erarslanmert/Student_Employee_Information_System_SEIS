# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'attandence.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import json
import connect_database
from PyQt5 import QtCore, QtGui, QtWidgets
import main_page, data_objects


attended_class_list = []
lesson_selected = " "
lesson_selected_2 = " "
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(353, 300)
        Dialog.setStyleSheet("background-color: rgb(0, 94, 138);")
        Dialog.setWindowIcon(QtGui.QIcon("logo_hq.png"))
        Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.Turkish, QtCore.QLocale.Turkey))
        Dialog.setWindowIcon(QtGui.QIcon("logo_hq.png"))
        self.pushButton = QtWidgets.QPushButton(Dialog, clicked = lambda : close_dialog_ok())
        self.pushButton.setGeometry(QtCore.QRect(80, 170, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 254, 238);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog,clicked = lambda : close_dialog_cancel())
        self.pushButton_2.setGeometry(QtCore.QRect(180, 170, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 254, 238);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(50, 50, 271, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(50, 90, 271, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_3.setGeometry(QtCore.QRect(50, 130, 271, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_4.setGeometry(QtCore.QRect(50, 200, 271, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_4.hide()
        self.radioButton_4.setChecked(True)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


        def close_dialog_cancel():
            self.press_cancel()
            Dialog.close()

        def close_dialog_ok():
            self.press_okay()
            Dialog.close()


    def press_cancel(self):
        self.radioButton_4.setChecked(True)

    def press_okay(self):
        global attended_class_list, lesson_selected, lesson_selected_2
        lesson_teacher = ''
        if self.radioButton.isChecked() == True:
            for student in data_objects.students:
                for schedule in student['student_schedule']:
                    if lesson_selected_2 == schedule:
                        student['student_schedule'].remove(schedule)
                        student['schedule_cancelled'].append('Ogrenci Iptal Etti' + ' ' + schedule)
            for employee in data_objects.employees:
                for schedule in employee['teacher_schedule']:
                    if lesson_selected == schedule:
                        employee['teacher_schedule'].remove(schedule)
                        employee['schedule_cancelled'].append('Ogrenci Iptal Etti' + ' ' + schedule)
        if self.radioButton_2.isChecked() == True:
            for student in data_objects.students:
                for schedule in student['student_schedule']:
                    if lesson_selected_2 == schedule:
                        student['student_schedule'].remove(schedule)
                        student['schedule_cancelled'].append('Ogretmen Iptal Etti' + ' ' + schedule)
            for employee in data_objects.employees:
                for schedule in employee['teacher_schedule']:
                    if lesson_selected == schedule:
                        employee['teacher_schedule'].remove(schedule)
                        employee['schedule_cancelled'].append('Ogretmen Iptal Etti' + ' ' + schedule)
        if self.radioButton_3.isChecked() == True:
            for student in data_objects.students:
                for schedule in student['student_schedule']:
                    if lesson_selected_2 == schedule:
                        student['student_schedule'].remove(schedule)
                        student['schedule_cancelled'].append('Kurum Iptal Etti' + ' ' + schedule)
            for employee in data_objects.employees:
                for schedule in employee['teacher_schedule']:
                    if lesson_selected == schedule:
                        employee['teacher_schedule'].remove(schedule)
                        employee['schedule_cancelled'].append('Kurum Iptal Etti' + ' ' + schedule)
        if self.radioButton_4.isChecked() == True:
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


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Ders Iptali Giris Sayfasi"))
        self.pushButton.setText(_translate("Dialog", "Tamam"))
        self.pushButton_2.setText(_translate("Dialog", "Iptal"))
        self.radioButton.setText(_translate("Dialog", "Ders Iptal Edildi (Ogrenci Tarafindan)"))
        self.radioButton_2.setText(_translate("Dialog", "Ders Iptal Edildi (OgretmenTarafindan)"))
        self.radioButton_3.setText(_translate("Dialog", "Ders Iptal Edildi (Kurum Tarafindan)"))

def class_cancel():
    Dialog = QtWidgets.QDialog()
    Dialog.setStyle(QtWidgets.QStyleFactory.create("WindowsVista"))
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    Dialog.exec_()