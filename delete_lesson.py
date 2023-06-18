# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete_lesson.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import json

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QMessageBox

import connect_database
import data_objects
import main_page


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(324, 377)
        Dialog.setStyleSheet("background-color: rgb(0, 85, 127);")
        Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.Turkish, QtCore.QLocale.Turkey))
        Dialog.setWindowIcon(QtGui.QIcon("logo_hq.png"))
        self.pushButton = QtWidgets.QPushButton(Dialog, clicked = lambda : dialog_close_ok())
        self.pushButton.setGeometry(QtCore.QRect(70, 310, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 254, 238);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog, clicked = lambda : Dialog.close())
        self.pushButton_2.setGeometry(QtCore.QRect(170, 310, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 254, 238);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(30, 80, 261, 31))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.comboBox.setFont(font)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 40, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(60, 210, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.comboBox_3 = QtWidgets.QComboBox(Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(30, 250, 261, 31))
        self.comboBox_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_3.setObjectName("comboBox_3")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.comboBox_3.setFont(font)
        self.dateEdit = QtWidgets.QDateEdit(Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(30, 160, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateEdit.setFont(font)
        self.dateEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit.setObjectName("dateEdit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 130, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.dateEdit.setDate(QDate.currentDate())

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


        self.comboBox_3.addItems(['9:30-10:10', '10:30-11:10', '11:30-12:10', '12:30-13:10', '13:10-14:00', '14:00-14:40',
         '15:00-15:40', '16:00-16:40', '17:00-17:40'])

        for employee in data_objects.employees:
            if employee['title'] == 'Ogretmen' or  employee['title'] == 'Dil Konusmaci' or  employee['title'] == 'Psikolog':
                self.comboBox.addItem((employee['name']) + ' ' + (employee['surname']))

        def dialog_close_ok():
            self.delete_selected()
            Dialog.close()

    def delete_selected(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Cizelgeden Ders Sil")
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setText(
            "Secili ders (planlanan ders / yoklamasi alinan ders / iptal olan ders) tum sistemden silinecektir. Onayliyor musunuz?")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        yesButton = msgBox.button(QMessageBox.Yes)
        yesButton.setText("Evet")
        noButton = msgBox.button(QMessageBox.No)
        noButton.setText("Hayir")
        response = msgBox.exec_()
        # Perform an action based on the user's response
        if response == QMessageBox.Yes:
            selected_lesson = []
            selected_lesson.append(str(self.dateEdit.date().toPyDate()))
            selected_lesson.append(self.comboBox.currentText())
            selected_lesson.append(self.comboBox_3.currentText())
            print(selected_lesson)
            for student in data_objects.students:
                for day in student['student_schedule']:
                    if selected_lesson[0] in day and selected_lesson[1] in day and selected_lesson[2] in day:
                        student['student_schedule'].remove(day)
                        data_objects.students[data_objects.students.index(student)] = student
                for day in student['student_attended']:
                    if selected_lesson[0] in day and selected_lesson[1] in day and selected_lesson[2] in day:
                        student['student_attended'].remove(day)
                        data_objects.students[data_objects.students.index(student)] = student
                for day in student['student_skipped']:
                    if selected_lesson[0] in day and selected_lesson[1] in day and selected_lesson[2] in day:
                        student['student_skipped'].remove(day)
                        data_objects.students[data_objects.students.index(student)] = student
                for day in student['schedule_cancelled']:
                    if selected_lesson[0] in day and selected_lesson[1] in day and selected_lesson[2] in day:
                        student['schedule_cancelled'].remove(day)
                        data_objects.students[data_objects.students.index(student)] = student
            for employee in data_objects.employees:
                for day in employee['teacher_schedule']:
                    if selected_lesson[0] in day and selected_lesson[2] in day:
                        employee['teacher_schedule'].remove(day)
                        data_objects.employees[data_objects.employees.index(employee)] = employee
                for day in employee['teacher_attended']:
                    if selected_lesson[0] in day and selected_lesson[2] in day:
                        employee['teacher_attended'].remove(day)
                        data_objects.employees[data_objects.employees.index(employee)] = employee
                for day in employee['teacher_skipped']:
                    if selected_lesson[0] in day and day and selected_lesson[2] in day:
                        employee['teacher_skipped'].remove(day)
                        data_objects.employees[data_objects.employees.index(employee)] = employee
                for day in employee['schedule_cancelled']:
                    if selected_lesson[0] in day and selected_lesson[2] in day:
                        employee['schedule_cancelled'].remove(day)
                        data_objects.employees[data_objects.employees.index(employee)] = employee

            with open("employee_data.txt", "w", encoding="utf-8") as f:
                f.writelines(json.dumps(data_objects.employees, default=str))
            with open('employee_data.txt', 'r', encoding="utf-8") as f:
                data_objects.employees = json.load(f)
            with open("student_data.txt", "w", encoding="utf-8") as f:
                f.writelines(json.dumps(data_objects.students, default=str))
            with open('student_data.txt', 'r', encoding="utf-8") as f:
                data_objects.students = json.load(f)
            '''connect_database.txt_to_csv('employee_data.txt', 'employee_data.csv')
            connect_database.txt_to_csv('student_data.txt', 'student_data.csv')
            connect_database.upload_files('student_data.txt')
            connect_database.upload_files('employee_data.txt')
            connect_database.upload_files('student_data.csv')
            connect_database.upload_files('employee_data.csv')'''
        else:
            pass


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Kullanici Sil"))
        self.pushButton.setText(_translate("Dialog", "Sil"))
        self.pushButton_2.setText(_translate("Dialog", "Iptal"))
        self.label.setText(_translate("Dialog", "Ogretmen Seciniz"))
        self.label_3.setText(_translate("Dialog", "Saat Seciniz"))
        self.label_2.setText(_translate("Dialog", "Tarih Seciniz"))

def open_delete_lesson():
    Dialog = QtWidgets.QDialog()
    Dialog.setStyle(QtWidgets.QStyleFactory.create("WindowsVista"))
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    Dialog.exec_()

