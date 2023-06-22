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
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(353, 670)
        Dialog.setStyleSheet("background-color: rgb(0, 94, 138);")
        Dialog.setWindowIcon(QtGui.QIcon("logo_hq.png"))
        Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.Turkish, QtCore.QLocale.Turkey))
        Dialog.setWindowIcon(QtGui.QIcon("logo_hq.png"))
        self.pushButton = QtWidgets.QPushButton(Dialog, clicked = lambda : close_dialog_ok())
        self.pushButton.setGeometry(QtCore.QRect(80, 608, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 254, 238);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog,clicked = lambda : close_dialog_cancel())
        self.pushButton_2.setGeometry(QtCore.QRect(180, 608, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 254, 238);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 248, 231, 31))
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
        self.listWidget.setGeometry(QtCore.QRect(50, 338, 251, 241))
        self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listWidget.setObjectName("listWidget")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.listWidget.setFont(font)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog, clicked = lambda : self.add_item())
        self.pushButton_3.setGeometry(QtCore.QRect(270, 298, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 254, 238);\n"
                                        "background-color: rgb(226, 226, 226);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog, clicked = lambda : self.subtract_item())
        self.pushButton_4.setGeometry(QtCore.QRect(50, 298, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 254, 238);\n"
                                        "background-color: rgb(226, 226, 226);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(90, 300, 171, 25))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.comboBox.setFont(font)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 18, 251, 31))
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
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(50, 70, 251, 25))
        self.comboBox_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_2.setObjectName("comboBox_2")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.comboBox_2.setFont(font)
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(50, 120, 271, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(50, 160, 271, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_3.setGeometry(QtCore.QRect(50, 200, 271, 20))
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
        self.pushButton.setDisabled(True)
        self.radioButton_4.setChecked(True)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        if data_objects.active_auth_level == 4:
            self.comboBox_2.clear()
            for attandence in main_page.attandence_list:
                if (data_objects.user_logged_in['name'] + ' ' + data_objects.user_logged_in['surname']) in attandence:
                    self.comboBox_2.addItem(attandence)
        else:
            self.comboBox_2.addItems(main_page.attandence_list)
        self.comboBox_2.currentTextChanged.connect(self.add_students)
        self.radioButton.toggled.connect(self.lock_widgets)
        self.radioButton_2.toggled.connect(self.lock_widgets)
        self.radioButton_3.toggled.connect(self.lock_widgets)
        self.comboBox_2.setCurrentIndex(1)
        self.comboBox_2.setCurrentIndex(0)



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
        self.radioButton_4.setChecked(True)
        self.pushButton_4.setEnabled(True)
        self.pushButton_3.setEnabled(True)
        self.comboBox.setEnabled(True)
        lesson_selected = self.comboBox_2.currentText()
        student_list = []
        for student in data_objects.students:
            for schedule in student['student_schedule']:
                if lesson_selected in schedule:
                    student_list.append(student['name'] + ' ' + student['surname'])
        self.comboBox.addItems(student_list)

    def press_cancel(self):
        self.listWidget.clear()
        self.comboBox.clear()
        self.comboBox_2.clear()
        self.radioButton_4.setChecked(True)

    def press_okay(self):
        global attended_class_list
        self.get_items()
        lesson_selected = self.comboBox_2.currentText()
        lesson_teacher = ''
        student_list = attended_class_list
        teacher = ''
        if self.radioButton.isChecked() == True:
            for student in data_objects.students:
                for schedule in student['student_schedule']:
                    if lesson_selected in schedule:
                        student['student_schedule'].remove(schedule)
                        student['schedule_cancelled'].append('Ogrenci Iptal Etti' + ' ' + schedule)
                        teacher_list = lesson_selected.split()
                        teacher = teacher_list[0] + ' ' + teacher_list[1]
                        lesson_teacher = lesson_selected.replace(teacher, '')
            for employee in data_objects.employees:
                for schedule in employee['teacher_schedule']:
                    if lesson_teacher in schedule:
                        employee['teacher_schedule'].remove(schedule)
                        employee['schedule_cancelled'].append('Ogrenci Iptal Etti' + ' ' + schedule)
        if self.radioButton_2.isChecked() == True:
            for student in data_objects.students:
                for schedule in student['student_schedule']:
                    if lesson_selected in schedule:
                        student['student_schedule'].remove(schedule)
                        student['schedule_cancelled'].append('Ogretmen Iptal Etti' + ' ' + schedule)
                        teacher_list = lesson_selected.split()
                        teacher = teacher_list[0] + ' ' + teacher_list[1]
                        lesson_teacher = lesson_selected.replace(teacher, '')
            for employee in data_objects.employees:
                for schedule in employee['teacher_schedule']:
                    if lesson_teacher in schedule:
                        employee['teacher_schedule'].remove(schedule)
                        employee['schedule_cancelled'].append('Ogretmen Iptal Etti' + ' ' + schedule)
        if self.radioButton_3.isChecked() == True:
            for student in data_objects.students:
                for schedule in student['student_schedule']:
                    if lesson_selected in schedule:
                        student['student_schedule'].remove(schedule)
                        student['schedule_cancelled'].append('Kurum Iptal Etti' + ' ' + schedule)
                        teacher_list = lesson_selected.split()
                        teacher = teacher_list[0] + ' ' + teacher_list[1]
                        lesson_teacher = lesson_selected.replace(teacher, '')
            for employee in data_objects.employees:
                for schedule in employee['teacher_schedule']:
                    if lesson_teacher in schedule:
                        employee['teacher_schedule'].remove(schedule)
                        employee['schedule_cancelled'].append('Kurum Iptal Etti' + ' ' + schedule)
        if self.radioButton_4.isChecked() == True:
            if len(attended_class_list) < len(student_list):
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
                    for student in data_objects.students:
                        for schedule in student['student_schedule']:
                            if lesson_selected in schedule:
                                if (student['name'] + ' ' + student['surname']) in student_list:
                                    student['student_schedule'].remove(schedule)
                                    student['student_attended'].append(schedule)
                                    teacher_list = lesson_selected.split()
                                    teacher = teacher_list[0] + ' ' + teacher_list[1]
                                    lesson_teacher = lesson_selected.replace(teacher,'')
                                else:
                                    teacher_list = lesson_selected.split()
                                    teacher = teacher_list[0] + ' ' + teacher_list[1]
                                    lesson_teacher = lesson_selected.replace(teacher, '')
                                    student['student_schedule'].remove(schedule)
                                    student['student_skipped'].append(schedule)

                    for employee in data_objects.employees:
                        for schedule in employee['teacher_schedule']:
                            if lesson_teacher in schedule:
                                employee['teacher_schedule'].remove(schedule)
                                employee['teacher_attended'].append(schedule)

                else:
                    pass
            else:
                for student in data_objects.students:
                    for schedule in student['student_schedule']:
                        if lesson_selected in schedule:
                            if (student['name'] + ' ' + student['surname']) in student_list:
                                student['student_schedule'].remove(schedule)
                                student['student_attended'].append(schedule)
                                teacher_list = lesson_selected.split()
                                teacher = teacher_list[0] + ' ' + teacher_list[1]
                                lesson_teacher = lesson_selected.replace(teacher, '')
                            else:
                                student['student_schedule'].remove(schedule)
                                student['student_skipped'].append(schedule)
                for employee in data_objects.employees:
                    for schedule in employee['teacher_schedule']:
                        if lesson_teacher in schedule:
                            employee['teacher_schedule'].remove(schedule)
                            employee['teacher_attended'].append(schedule)


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
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Ders Bilgisi Ekleme Sayfasi"))
        self.pushButton.setText(_translate("Dialog", "Tamam"))
        self.pushButton_2.setText(_translate("Dialog", "Iptal"))
        self.label.setText(_translate("Dialog", "Lutfen Derse Gelen Ogrencileri Listeye Ekleyin"))
        self.pushButton_3.setText(_translate("Dialog", "+"))
        self.pushButton_4.setText(_translate("Dialog", "-"))
        self.label_2.setText(_translate("Dialog", "Lutfen Yoklama Alinacak Dersi Secin"))
        self.radioButton.setText(_translate("Dialog", "Ders Iptal Edildi (Ogrenci Tarafindan)"))
        self.radioButton_2.setText(_translate("Dialog", "Ders Iptal Edildi (OgretmenTarafindan)"))
        self.radioButton_3.setText(_translate("Dialog", "Ders Iptal Edildi (Kurum Tarafindan)"))

def can():
    Dialog = QtWidgets.QDialog()
    Dialog.setStyle(QtWidgets.QStyleFactory.create("WindowsVista"))
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    Dialog.exec_()