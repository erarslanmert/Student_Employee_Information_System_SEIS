# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'employee_addition.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import json
from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
from PyQt5.QtWidgets import QMessageBox
import connect_database
from PyQt5.QtCore import QDate
import data_objects
import date_consistency
import main_page

experience_list = []
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(393, 755)
        Dialog.setStyleSheet("background-color: rgb(0, 102, 150);")
        Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.Turkish, QtCore.QLocale.Turkey))
        Dialog.setWindowIcon(QtGui.QIcon("logo_hq.png"))
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(20, 30, 351, 641))
        self.frame.setStyleSheet("color: rgb(255, 230, 207);")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 100, 161, 20))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "color: rgb(0, 0, 0);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.lineEdit_2.setFont(font)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(40, 130, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(150, 70, 161, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "color: rgb(0, 0, 0);")
        self.lineEdit.setObjectName("lineEdit")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.lineEdit.setFont(font)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(150, 160, 161, 20))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "color: rgb(0, 0, 0);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.lineEdit_4.setFont(font)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 70, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 47, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(40, 160, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_16.setGeometry(QtCore.QRect(150, 410, 161, 61))
        self.lineEdit_16.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "color: rgb(0, 0, 0);")
        self.lineEdit_16.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.lineEdit_16.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit_16.setClearButtonEnabled(False)
        self.lineEdit_16.setObjectName("lineEdit_16")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.lineEdit_16.setFont(font)
        self.label_22 = QtWidgets.QLabel(self.frame)
        self.label_22.setGeometry(QtCore.QRect(40, 430, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_22.setObjectName("label_22")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_19.setGeometry(QtCore.QRect(150, 190, 161, 20))
        self.lineEdit_19.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "color: rgb(0, 0, 0);")
        self.lineEdit_19.setObjectName("lineEdit_19")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.lineEdit_19.setFont(font)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(40, 180, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(40, 350, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(190, 540, 71, 71))
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_8.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("default-user-image.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.label_8.setFont(font)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(239, 589, 21, 21))
        self.pushButton_5.setAutoFillBackground(False)
        self.pushButton_5.setStyleSheet("background-color: rgb(209, 209, 209);\n"
                                        "color: rgb(0, 0, 0);")
        self.pushButton_5.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_5.setFlat(False)
        self.pushButton_5.setObjectName("pushButton_5")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.pushButton_5.setFont(font)
        self.label_27 = QtWidgets.QLabel(self.frame)
        self.label_27.setGeometry(QtCore.QRect(40, 570, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_27.setObjectName("label_27")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(40, 260, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(40, 220, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(40, 40, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.comboBox_5 = QtWidgets.QComboBox(self.frame)
        self.comboBox_5.setGeometry(QtCore.QRect(150, 40, 161, 21))
        self.comboBox_5.setAutoFillBackground(False)
        self.comboBox_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "color: rgb(0, 0, 0);")
        self.comboBox_5.setObjectName("comboBox_5")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.comboBox_5.setFont(font)
        self.lineEdit_25 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_25.setGeometry(QtCore.QRect(150, 350, 161, 20))
        self.lineEdit_25.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "color: rgb(0, 0, 0);")
        self.lineEdit_25.setText("")
        self.lineEdit_25.setObjectName("lineEdit_25")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.lineEdit_25.setFont(font)
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(40, 380, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_12.setObjectName("label_12")
        self.lineEdit_26 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_26.setGeometry(QtCore.QRect(150, 380, 161, 20))
        self.lineEdit_26.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "color: rgb(0, 0, 0);")
        self.lineEdit_26.setText("")
        self.lineEdit_26.setObjectName("lineEdit_26")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.lineEdit_26.setFont(font)
        self.label_34 = QtWidgets.QLabel(self.frame)
        self.label_34.setGeometry(QtCore.QRect(40, 480, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_34.setObjectName("label_34")
        self.comboBox_6 = QtWidgets.QComboBox(self.frame)
        self.comboBox_6.setGeometry(QtCore.QRect(150, 480, 161, 21))
        self.comboBox_6.setAutoFillBackground(False)
        self.comboBox_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "color: rgb(0, 0, 0);")
        self.comboBox_6.setObjectName("comboBox_6")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.comboBox_6.setFont(font)
        self.lineEdit_27 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_27.setGeometry(QtCore.QRect(150, 510, 161, 20))
        self.lineEdit_27.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "color: rgb(0, 0, 0);")
        self.lineEdit_27.setText("")
        self.lineEdit_27.setObjectName("lineEdit_27")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.lineEdit_27.setFont(font)
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setGeometry(QtCore.QRect(40, 500, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_14.setWordWrap(True)
        self.label_14.setObjectName("label_14")
        self.dateEdit = QtWidgets.QDateEdit(self.frame)
        self.dateEdit.setGeometry(QtCore.QRect(150, 130, 161, 22))
        self.dateEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "color: rgb(0, 0, 0);")
        self.dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.dateEdit.setFont(font)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.frame)
        self.dateEdit_2.setGeometry(QtCore.QRect(150, 220, 161, 22))
        self.dateEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "color: rgb(0, 0, 0);")
        self.dateEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setObjectName("dateEdit_2")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.dateEdit_2.setFont(font)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame, clicked = lambda : self.add_item())
        self.pushButton_6.setGeometry(QtCore.QRect(290, 260, 21, 21))
        self.pushButton_6.setAutoFillBackground(False)
        self.pushButton_6.setStyleSheet("background-color: rgb(209, 209, 209);\n"
                                        "color: rgb(0, 0, 0);")
        self.pushButton_6.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_6.setFlat(False)
        self.pushButton_6.setObjectName("pushButton_6")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.pushButton_6.setFont(font)
        self.pushButton_8 = QtWidgets.QPushButton(self.frame, clicked = lambda : self.subtract_item())
        self.pushButton_8.setGeometry(QtCore.QRect(150, 260, 21, 21))
        self.pushButton_8.setAutoFillBackground(False)
        self.pushButton_8.setStyleSheet("background-color: rgb(209, 209, 209);\n"
                                        "color: rgb(0, 0, 0);")
        self.pushButton_8.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_8.setFlat(False)
        self.pushButton_8.setObjectName("pushButton_8")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.pushButton_8.setFont(font)
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setGeometry(QtCore.QRect(150, 280, 161, 61))
        self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "color: rgb(0, 0, 0);")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.listWidget.setFont(font)
        self.lineEdit_23 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_23.setGeometry(QtCore.QRect(169, 260, 122, 20))
        self.lineEdit_23.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "color: rgb(0, 0, 0);")
        self.lineEdit_23.setText("")
        self.lineEdit_23.setObjectName("lineEdit_23")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.lineEdit_23.setFont(font)
        self.pushButton = QtWidgets.QPushButton(Dialog, clicked = lambda: close_dialog())
        self.pushButton.setGeometry(QtCore.QRect(120, 700, 75, 31))
        self.pushButton.setStyleSheet("background-color: rgb(255, 230, 207);")
        self.pushButton.setObjectName("pushButton")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.pushButton.setFont(font)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog, clicked = lambda : Dialog.close())
        self.pushButton_2.setGeometry(QtCore.QRect(200, 700, 75, 31))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 230, 207);")
        self.pushButton_2.setObjectName("pushButton_2")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.pushButton_2.setFont(font)
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(40, 20, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(255, 230, 207);")
        self.label_13.setObjectName("label_13")
        self.comboBox_5.setEditable(True)
        self.comboBox_5.addItems(['Ogretmen', 'Ust Yonetici', 'Mudur', 'Mudur Yardimcisi', 'Sekreter', 'Sofor', 'Temizlik Elemani',
                                  'Mutfak Elemani', 'Guvenlik Gorevlisi', 'Psikolog', 'Dil Konusmaci', 'Stajyer'])
        self.comboBox_6.setEditable(True)
        self.comboBox_6.addItems(['Full-time', 'Part-time'])

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        def close_dialog():
            self.save_employee()
            Dialog.close()

        if data_objects.active_auth_level == 1:
            pass
        else:
            self.lineEdit_27.setDisabled(True)
            self.lineEdit_27.hide()
            self.label_14.hide()


    def add_item(self):
        text = self.lineEdit_23.text()
        self.listWidget.addItem(text)
        self.lineEdit_23.clear()

    def subtract_item(self):
        current_row = self.listWidget.currentRow()
        if current_row != -1:
            self.listWidget.takeItem(current_row)

    def get_items(self):
        global experience_list
        items = []
        for index in range(self.listWidget.count()):
            items.append(self.listWidget.item(index).text())
        experience_list = items

    def save_employee(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Calisan Olusturuluyor")
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setText(
            "Girdiginiz bilgileri kontrol ettiyseniz, yeni calisan sisteme eklenecektir. Onayliyor musunuz?")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        yesButton = msgBox.button(QMessageBox.Yes)
        yesButton.setText("Evet")
        noButton = msgBox.button(QMessageBox.No)
        noButton.setText("Hayir")
        response = msgBox.exec_()
        # Perform an action based on the user's response
        if response == QMessageBox.Yes:
            self.get_items()
            current_date = datetime.date.today()
            formatted_date = current_date.strftime("%d-%m-%Y")
            data_objects.one_employee = {
                        "title": self.comboBox_5.currentText(),
                        "name": self.lineEdit.text().title(),
                        "surname": self.lineEdit_2.text().title(),
                        "date_of_birth": self.dateEdit.date().toPyDate(),
                        "identity_no": self.lineEdit_4.text().title(),
                        "graduation_school": self.lineEdit_19.text().title(),
                        "graduation_date": self.dateEdit_2.date().toPyDate(),
                        "experience": experience_list,
                        "phone": self.lineEdit_25.text().title(),
                        "email": self.lineEdit_26.text(),
                        "address": self.lineEdit_16.text().title(),
                        "type_employment": self.comboBox_6.currentText(),
                        "agreed_salary": self.lineEdit_27.text().title(),
                        "photo": '-',
                        "status": 'Aktif' + '           ' + formatted_date,
                        "registration_date": formatted_date,
                        "working_days": [],
                        "salary_change": [],
                        "teacher_schedule": [],
                        "teacher_attended": [],
                        "teacher_skipped": [],
                        "schedule_changed": [],
                        "schedule_cancelled": [],
                        "monthly_payment_date": '1',
                        "paid_salary": [],
                        "unpaid_salary": []
                }
            data_objects.employees.append(data_objects.one_employee)
            # write data to file
            date_consistency.convert_dates_in_list(data_objects.employees)

            with open("employee_data.txt", "w", encoding="utf-8") as f:
                    f.writelines(json.dumps(data_objects.employees,default=str))
            data_objects.one_employee = {}
            with open('employee_data.txt', 'r', encoding="utf-8") as f:
                data_objects.employees = json.load(f)
            connect_database.txt_to_csv('employee_data.txt', 'employee_data.csv')
            connect_database.upload_files('employee_data.txt')
            connect_database.upload_files('employee_data.csv')

        else:
            pass

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "Dogum Tarihi"))
        self.label.setText(_translate("Dialog", "Isim"))
        self.label_2.setText(_translate("Dialog", "Soyisim"))
        self.label_4.setText(_translate("Dialog", "TC Kimlik No"))
        self.label_22.setText(_translate("Dialog", "Adres"))
        self.label_5.setText(_translate("Dialog", "Mezun Oldugu Kurum"))
        self.label_7.setText(_translate("Dialog", "Telefon No"))
        self.pushButton_5.setToolTip(_translate("Dialog", "Fotograf Yukle"))
        self.pushButton_5.setText(_translate("Dialog", "+"))
        self.label_27.setText(_translate("Dialog", "Fotograf Ekle"))
        self.label_9.setText(_translate("Dialog", "Gecmis Kurum /Kurumlar"))
        self.label_10.setText(_translate("Dialog", "Mezuniyet Tarihi"))
        self.label_11.setText(_translate("Dialog", "Unvan"))
        self.label_12.setText(_translate("Dialog", "E-mail Adresi"))
        self.label_34.setText(_translate("Dialog", "Calisma Tipi"))
        self.label_14.setText(_translate("Dialog", "Anlasilan Baslangic Ucreti"))
        self.pushButton_6.setText(_translate("Dialog", "+"))
        self.pushButton_8.setToolTip(_translate("Dialog", "Fotograf Yukle"))
        self.pushButton_8.setText(_translate("Dialog", "-"))
        self.pushButton.setText(_translate("Dialog", "Ekle"))
        self.pushButton_2.setText(_translate("Dialog", "Vazgec"))
        self.label_13.setText(_translate("Dialog", "   Calisan Bilgileri"))

def open_employee_addition():
    Dialog = QtWidgets.QDialog()
    Dialog.setStyle(QtWidgets.QStyleFactory.create("Fusion"))
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    Dialog.exec_()