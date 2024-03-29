# -*- coding: utf-8 -*-
import json
from datetime import datetime

# Form implementation generated from reading ui file 'temporary_student.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QMessageBox
import connect_database
import data_objects

message = ' '
is_empty = 0
teacher = ' '
time = ' '
date = ' '

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(379, 375)
        Dialog.setStyleSheet("background-color: rgb(0, 52, 77);")
        Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.Turkish, QtCore.QLocale.Turkey))
        Dialog.setWindowIcon(QtGui.QIcon("logo_hq.png"))
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(20, 70, 341, 231))
        self.frame.setStyleSheet("color: rgb(255, 230, 207);")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 70, 161, 20))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(40, 100, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(150, 40, 161, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 40, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 47, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_28 = QtWidgets.QLabel(self.frame)
        self.label_28.setGeometry(QtCore.QRect(40, 130, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.frame)
        self.label_29.setGeometry(QtCore.QRect(40, 160, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_29.setObjectName("label_29")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setGeometry(QtCore.QRect(150, 130, 161, 21))
        self.comboBox_2.setAutoFillBackground(False)
        self.comboBox_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.dateEdit = QtWidgets.QDateEdit(self.frame)
        self.dateEdit.setGeometry(QtCore.QRect(150, 100, 161, 22))
        self.dateEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setDate(QDate.currentDate())
        self.comboBox_3 = QtWidgets.QComboBox(self.frame)
        self.comboBox_3.setGeometry(QtCore.QRect(150, 160, 161, 21))
        self.comboBox_3.setAutoFillBackground(False)
        self.comboBox_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "color: rgb(0, 0, 0);")
        self.comboBox_3.setObjectName("comboBox_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(150, 190, 161, 20))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_30 = QtWidgets.QLabel(self.frame)
        self.label_30.setGeometry(QtCore.QRect(40, 190, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_30.setObjectName("label_30")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(40, 60, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color:  rgb(255, 230, 207);")
        self.label_14.setObjectName("label_14")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog, clicked = lambda : close_dialog_cancel())
        self.pushButton_3.setGeometry(QtCore.QRect(190, 320, 111, 31))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 246, 194);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog, clicked = lambda : close_dialog())
        self.pushButton_7.setGeometry(QtCore.QRect(70, 320, 111, 31))
        self.pushButton_7.setStyleSheet("background-color: rgb(255, 246, 194);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.comboBox_5 = QtWidgets.QComboBox(Dialog)
        self.comboBox_5.setGeometry(QtCore.QRect(40, 20, 301, 21))
        self.comboBox_5.setAutoFillBackground(False)
        self.comboBox_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.comboBox_5.setObjectName("comboBox_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.comboBox_5.currentTextChanged.connect(lambda : self.combo_changed())

        date_obj = QDate.fromString(date, 'yyyy-MM-dd')

        # Set the date in the QDateEdit widget

        def close_dialog():
            self.save_data()
            Dialog.close()
        def close_dialog_cancel():
            is_empty = 0
            Dialog.close()

        with open('temporary_student.txt', 'r', encoding="utf-8") as f:
            data_objects.temporary_students = json.load(f)

        hours = ['9:30-10:10', '10:30-11:10', '11:30-12:10', '12:30-13:10', '13:10-14:00', '14:00-14:40',
                 '15:00-15:40', '16:00-16:40', '17:00-17:40']
        for item in hours:
            self.comboBox_2.addItem(item)
        for employee in data_objects.employees:
            if employee['title'] == 'Ogretmen' or employee['title'] == 'Dil Konusmaci' or employee['title'] == 'Psikolog':
                self.comboBox_3.addItem(employee['name'] + ' ' + employee['surname'])
            else:
                pass
        self.comboBox_5.addItem('-')
        if len(data_objects.temporary_students) > 0:
            for student in data_objects.temporary_students:
                self.comboBox_5.addItem(student['name'] + ' ' + student['surname'])
        else:
            pass

        self.dateEdit.setDate(date_obj)
        self.comboBox_2.setCurrentText(time)
        self.comboBox_3.setCurrentText(teacher)

    def combo_changed(self):
        global message, is_empty
        if self.comboBox_5.currentText() == '-':
            self.pushButton_7.setText('Kaydet')
            self.lineEdit.setEnabled(True)
            self.lineEdit_2.setEnabled(True)
            self.lineEdit_4.setEnabled(True)
            self.dateEdit.setEnabled(True)
            self.comboBox_3.setEnabled(True)
            self.comboBox_2.setEnabled(True)
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_4.clear()
            self.dateEdit.clear()
            message = 'Deneme dersi sisteme kaydolacaktir ve istatistiklere katilacaktir. Onayliyor musunuz?'
            is_empty = 0
        else:
            for student in data_objects.temporary_students:
                if student['name'] + ' ' + student['surname'] == self.comboBox_5.currentText():
                    self.pushButton_7.setText('Sil')
                    self.lineEdit.setDisabled(True)
                    self.lineEdit_2.setDisabled(True)
                    self.lineEdit_4.setDisabled(True)
                    self.dateEdit.setDisabled(True)
                    self.comboBox_3.setDisabled(True)
                    self.comboBox_2.setDisabled(True)
                    self.lineEdit.setText(student['name'])
                    self.lineEdit_2.setText(student['surname'])
                    self.comboBox_2.setCurrentText(student['lesson_time'])
                    self.comboBox_3.setCurrentText(student['teacher'])
                    self.lineEdit_4.setText(student['contact'])
                    self.dateEdit.setDate(datetime.strptime(student['lesson_date'], '%Y-%m-%d').date())
                    message = 'Deneme dersi ve ogrenci bilgisi sistemden silinecektir. Onayliyor musunuz?'
                    is_empty = 1
                else:
                    pass

    def save_data(self):
        global message, is_empty
        # Process the data
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Deneme Dersi Ekle")
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setText(message)
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        yesButton = msgBox.button(QMessageBox.Yes)
        yesButton.setText("Evet")
        noButton = msgBox.button(QMessageBox.No)
        noButton.setText("Hayir")
        response = msgBox.exec_()
        # Perform an action based on the user's response
        days = ['PAZARTESI', 'SALI', 'CARSAMBA', 'PERSEMBE', 'CUMA', 'CUMARTESI', 'PAZAR']
        if response == QMessageBox.Yes:
            if is_empty == 0:
                date = self.dateEdit.date().toPyDate()
                formatted_date = date.strftime("%Y-%m-%d")
                date_obj = datetime.strptime(formatted_date, "%Y-%m-%d")
                day_of_week = date_obj.weekday()
                data_objects.temporary_one_student = {
                    'name': self.lineEdit.text().title(),
                    'surname': self.lineEdit_2.text().title(),
                    'lesson_date': formatted_date,
                    'lesson_time': self.comboBox_2.currentText(),
                    'teacher': self.comboBox_3.currentText(),
                    'contact': self.lineEdit_4.text()
                }
                data_objects.temporary_students.append(data_objects.temporary_one_student)
                for employee in data_objects.employees:
                    if (employee['name'] + ' ' + employee['surname']) == data_objects.temporary_one_student['teacher']:
                        employee['teacher_schedule'].append(('Deneme Dersi' + " ['" +
                                                             data_objects.temporary_one_student['name'] + ' ' +
                                                             data_objects.temporary_one_student['surname']
                                                             + "'] " + data_objects.temporary_one_student[
                                                                 'lesson_time'] + ' ' + days[day_of_week] +' '+
                                                             data_objects.temporary_one_student['lesson_date']))
                    else:
                        pass
                for item in data_objects.temporary_students:
                    name = item.get('name')
                    if name and ' ' in name:
                        item['name'] = name.replace(' ', '-')
                    if name.endswith('-'):
                        item['name'] = name.replace('-',
                                                    '')  # Remove the trailing '-' if it is not followed by a word character

                    for key, value in item.items():
                        if isinstance(value, str) and value.endswith('\n') or ('\n') in value:
                            item[key] = value.replace('\n', '')
            else:
                for student in data_objects.temporary_students:
                    if student['name'] + ' ' + student['surname'] == self.comboBox_5.currentText():
                        del data_objects.temporary_students[data_objects.temporary_students.index(student)]
                    else:
                        pass
        else:
            pass

        # Save the updated data back to the file
        with open("temporary_student.txt", "w", encoding="utf-8") as f:
            f.writelines(json.dumps(data_objects.temporary_students, default=str))
        with open("employee_data.txt", "w", encoding="utf-8") as f:
            f.writelines(json.dumps(data_objects.employees, default=str))

        connect_database.upload_files('temporary_student.txt')
        data_objects.temporary_one_student = {}



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "Ders Tarihi"))
        self.label.setText(_translate("Dialog", "Isim"))
        self.label_2.setText(_translate("Dialog", "Soyisim"))
        self.label_28.setText(_translate("Dialog", "Ders Saati"))
        self.label_29.setText(_translate("Dialog", "Ogretmen"))
        self.label_30.setText(_translate("Dialog", "Iletisim"))
        self.label_14.setText(_translate("Dialog", "  Ogrenci Bilgileri"))
        self.pushButton_3.setText(_translate("Dialog", "Vazgec"))
        self.pushButton_7.setText(_translate("Dialog", "Kaydet"))

def open_temporary_student():
    Dialog = QtWidgets.QDialog()
    Dialog.setStyle(QtWidgets.QStyleFactory.create("WindowsVista"))
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    Dialog.exec_()