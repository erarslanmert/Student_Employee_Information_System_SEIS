# -*- coding: utf-8 -*-


import json
import textwrap

import numpy as np
from PyQt5 import QtWidgets,QtCore,QtGui
import matplotlib.pyplot as plt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import data_objects

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(730, 960)
        Dialog.setStyleSheet("background-color: #FCFBE1;")
        Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.Turkish, QtCore.QLocale.Turkey))
        Dialog.setWindowIcon(QtGui.QIcon("logo_hq.png"))
        self.rendered_dialog = Dialog
        self.comboBox_5 = QtWidgets.QComboBox(Dialog)
        self.comboBox_5.setGeometry(QtCore.QRect(250, 710, 131, 22))
        self.comboBox_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_5.setObjectName("comboBox_5")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.comboBox_5.setFont(font)
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(390, 710, 111, 22))
        self.spinBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox.setMinimum(2020)
        self.spinBox.setMaximum(2100)
        self.spinBox.setObjectName("spinBox")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.spinBox.setFont(font)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 750, 191, 16))
        self.label.setObjectName("label")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.label.setFont(font)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 780, 191, 16))
        self.label_2.setObjectName("label_2")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 840, 191, 16))
        self.label_3.setObjectName("label_3")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 870, 191, 16))
        self.label_4.setObjectName("label_4")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.label_4.setFont(font)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 900, 191, 16))
        self.label_5.setObjectName("label_5")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.label_5.setFont(font)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(250, 750, 211, 16))
        self.label_6.setObjectName("label_6")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.label_6.setFont(font)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(20, 810, 191, 16))
        self.label_7.setObjectName("label_7")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.label_7.setFont(font)
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(250, 780, 211, 16))
        self.label_8.setObjectName("label_8")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.label_8.setFont(font)
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(250, 810, 211, 16))
        self.label_9.setObjectName("label_9")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.label_9.setFont(font)
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(280, 680, 211, 16))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.label_10.setFont(font)
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(250, 840, 251, 16))
        self.label_11.setObjectName("label_11")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.label_11.setFont(font)
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(250, 870, 251, 16))
        self.label_12.setObjectName("label_12")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.label_12.setFont(font)
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(250, 900, 251, 16))
        self.label_13.setObjectName("label_13")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.label_13.setFont(font)
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(550, 750, 191, 16))
        self.label_14.setObjectName("label_14")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.label_14.setFont(font)
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(550, 780, 191, 16))
        self.label_15.setObjectName("label_15")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.label_15.setFont(font)
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(550, 810, 191, 16))
        self.label_16.setObjectName("label_16")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.label_16.setFont(font)
        self.label_17 = QtWidgets.QLabel(Dialog)
        self.label_17.setGeometry(QtCore.QRect(550, 840, 191, 16))
        self.label_17.setObjectName("label_17")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.label_17.setFont(font)
        self.label_18 = QtWidgets.QLabel(Dialog)
        self.label_18.setGeometry(QtCore.QRect(550, 870, 191, 16))
        self.label_18.setObjectName("label_18")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.label_18.setFont(font)
        self.label_19 = QtWidgets.QLabel(Dialog)
        self.label_19.setGeometry(QtCore.QRect(550, 900, 191, 16))
        self.label_19.setObjectName("label_19")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setItalic(False)
        self.label_19.setFont(font)

        self.comboBox_5.addItems(['Ocak','Subat','Mart','Nisan','Mayis','Haziran','Temmuz','Agustos','Eylul',
                                  'Ekim','Kasim','Aralik'])

        # Create a Matplotlib Figure and add a subplot for the bar chart
        self.figure = plt.Figure()
        self.barChart = self.figure.add_subplot(211)
        self.barChart2 = self.figure.add_subplot(212)
        self.barChart.set_title("Genel Ogrenci & Calisan Istatistikleri", fontsize=8, pad = 30)



        # Add the bars to the subplot
        x = ['Aktif Ogrenci', 'Pasif Ogrenci', 'Ayrilan Ogrenci', 'Dersleri Bitiren Ogrenci', 'Toplam Ogrenci',
                'Attentioner Ogrenci', 'Akademik Ogrenci', 'Ozel Ogrenci', 'Raporlu Ogrenci', 'Karma Ogrenci']
        total_student = len(data_objects.students)
        attentioner_student = []
        academic_student = []
        paid_student = []
        unpaid_student = []
        mixed_paid_student = []
        active_students = []
        passive_students = []
        student_left_self = []
        student_left_finished = []

        with open('student_data.txt', 'r', encoding="utf-8") as f:
            data_objects.students = json.load(f)
        with open('employee_data.txt', 'r', encoding="utf-8") as f:
            data_objects.employees = json.load(f)

        for student in data_objects.students:
            if student['module'] == 'Attentioner':
                attentioner_student.append(student['name']+' '+student['surname'])
            if student['module'] == 'Akademik':
                academic_student.append(student['name']+' '+student['surname'])
            if student['registeration_type'] == 'Ozel':
                paid_student.append(student['name']+' '+student['surname'])
            if student['registeration_type'] == 'Raporlu':
                unpaid_student.append(student['name']+' '+student['surname'])
            if student['registeration_type'] == 'Karma':
                mixed_paid_student.append(student['name']+' '+student['surname'])
            if 'Aktif' in student['status']:
                active_students.append(student['name']+' '+student['surname'])
            if 'Pasif' in student['status']:
                passive_students.append(student['name'] + ' ' + student['surname'])
            if student['student_left'] == 'Ogrenci kendi istegi ile ayrilmistir':
                student_left_self.append(student['name']+' '+student['surname'])
            if student['student_left'] == 'Ogrenci dersleri bitirdigi icin ayrilmistir':
                student_left_finished.append(student['name']+' '+student['surname'])

        x_1 = ['Ogretmen', 'Ust Yonetici', 'Mudur', 'Mudur Yardimcisi', 'Sekreter', 
               'Sofor', 'Temizlik Elemani', 'Mutfak Elemani', 'Guvenlik Gorevlisi', 'Psikolog', 'Dil Konusmaci', 'Stajyer',
               'Toplam Aktif Calisan', 'Toplam Ayrilan Calisan']
        
        teacher = []
        master_manager = []
        manager = []
        assistant_manager = []
        secretary = []
        driver = []
        cleaner = []
        cooker = []
        security = []
        psychologist = []
        speaker = []
        intern = []
        total_active = []
        total_passive = []
        
        for employee in data_objects.employees:
            if employee['title'] == x_1[0]:
                teacher.append(employee['name']+' '+employee['surname'])
            if employee['title'] == x_1[1]:
                master_manager.append(employee['name']+' '+employee['surname'])
            if employee['title'] == x_1[2]:
                manager.append(employee['name']+' '+employee['surname'])
            if employee['title'] == x_1[3]:
                assistant_manager.append(employee['name']+' '+employee['surname'])
            if employee['title'] == x_1[4]:
                secretary.append(employee['name']+' '+employee['surname'])
            if employee['title'] == x_1[5]:
                driver.append(employee['name']+' '+employee['surname'])
            if employee['title'] == x_1[6]:
                cleaner.append(employee['name'] + ' ' + employee['surname'])
            if employee['title'] == x_1[7]:
                cooker.append(employee['name']+' '+employee['surname'])
            if employee['title'] == x_1[8]:
                security.append(employee['name']+' '+employee['surname'])
            if employee['title'] == x_1[9]:
                psychologist.append(employee['name']+' '+employee['surname'])
            if employee['title'] == x_1[10]:
                speaker.append(employee['name']+' '+employee['surname'])
            if employee['title'] == x_1[11]:
                intern.append(employee['name']+' '+employee['surname'])
            if 'Aktif' in employee['status']:
                total_active.append(employee['name']+' '+employee['surname'])
            if 'Pasif' in employee['status']:
                total_passive.append(employee['name']+' '+employee['surname'])

        
        y = [len(active_students), len(passive_students), len(student_left_self),
             len(student_left_finished), len(data_objects.students), len(attentioner_student),
             len(academic_student), len(paid_student), len(unpaid_student),len(mixed_paid_student)]
        
        y_1 = [len(teacher), len(master_manager), len(manager),
             len(assistant_manager), len(secretary), len(driver),
             len(cleaner), len(cooker), len(security),len(psychologist),len(speaker),len(intern),
             len(total_active),len(total_passive)]
        #
        colors = ['#FFBEBE', '#FFE2AD', '#DEFBBE', '#BEFBD9', '#D5F7FF', '#E1D5FF', '#F9D5FF','#ECECEC', '#FFBEBE', '#FFE2AD', '#DEFBBE', '#BEFBD9', '#D5F7FF', '#E1D5FF', '#F9D5FF','#ECECEC']
        wrapped_labels = ['\n'.join(textwrap.wrap(label, width=11)) for label in x]
        wrapped_labels_2 = ['\n'.join(textwrap.wrap(label, width=15
                                                    )) for label in x_1]

        # Set the x-axis labels on the bar chart
        x_positions = np.arange(len(wrapped_labels))
        self.barChart.set_xticks(x_positions)
        self.barChart.set_xticklabels(wrapped_labels)
        x_positions_2 = np.arange(len(wrapped_labels_2))
        self.barChart2.set_xticks(x_positions_2)
        self.barChart2.set_xticklabels(wrapped_labels_2)
        bars = self.barChart.bar(x_positions, y, color=colors)
        bars2 = self.barChart2.bar(x_positions_2, y_1, color=colors)

        # Set the axes labels and add the FigureCanvas to the dialog
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setGeometry(QtCore.QRect(0, 0, 700, 650))
        self.canvas.setParent(Dialog)
        self.canvas.show()

        # Hide the rectangle around the graph
        self.barChart.spines['top'].set_visible(False)
        self.barChart.spines['right'].set_visible(False)
        self.barChart.spines['left'].set_visible(False)

        self.barChart2.spines['top'].set_visible(False)
        self.barChart2.spines['right'].set_visible(False)
        self.barChart2.spines['left'].set_visible(False)


        # Hide the y-axis labels
        self.barChart.tick_params(axis='y', labelcolor='white')
        self.barChart.tick_params(axis='x', labelrotation=45, labelsize=6, pad=1)
        self.barChart.set_yticks([])
        self.barChart.set_yticklabels([])
        self.figure.patch.set_facecolor('#FCFBE1')
        self.barChart.set_facecolor('#FCFBE1')
        self.barChart2.tick_params(axis='y', labelcolor='white')
        self.barChart2.tick_params(axis='x', labelrotation=45, labelsize=6, pad=1)
        self.barChart2.set_yticks([])
        self.barChart2.set_yticklabels([])
        self.barChart2.set_facecolor('#FCFBE1')
        self.figure.subplots_adjust(bottom=0.1)
        # Set the x-axis label rotation angle and label position


        # Add the value labels to the plot
        for bar in bars:
            height = bar.get_height()
            self.barChart.text(bar.get_x() + bar.get_width() / 2., height,
                               '%d' % int(height), ha='center', va='bottom')

        for bar in bars2:
            height = bar.get_height()
            self.barChart2.text(bar.get_x() + bar.get_width() / 2., height,
                               '%d' % int(height), ha='center', va='bottom')

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


        self.spinBox.setValue(2023)
        self.comboBox_5.currentTextChanged.connect(self.update_labels)
        self.spinBox.valueChanged.connect(self.update_labels)

    def save_pdf(self):
        from PyQt5.QtGui import QPainter
        from PyQt5.QtPrintSupport import QPrinter
        import tkinter as tk
        from tkinter import filedialog
        printer = QPrinter()
        printer.setOutputFormat(QPrinter.PdfFormat)
        dialog_title = 'Save PNG'
        default_filename = 'genel_istatistikler.png'
        root = tk.Tk()
        root.withdraw()  # hide the main window
        file_path = filedialog.asksaveasfilename(defaultextension='.png', filetypes=[('PNG Files', '*.png')],
                                                 initialfile=default_filename, title=dialog_title)
        if file_path:
            pixmap = QPixmap.grab(Ui_Dialog)
            pixmap.save(file_path, 'PNG')

    def update_labels(self):
        total_attended_student = []
        total_attended_teacher = []
        total_group_lesson = []
        total_planned_lesson = 0
        total_completed_lesson = []
        total_cancelled_lesson = []
        total_missed_student = []
        total_attentioner_lesson = []
        total_academic_lesson = []
        cancelled_by_student = []
        cancelled_by_teacher = []
        cancelled_by_company = []
        month = self.comboBox_5.currentIndex()
        year = self.spinBox.text()
        months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        date_selected = year + '-' + months[month]
        for student in data_objects.students:
            for lesson in student['student_attended']:
                if date_selected in lesson:
                    total_attended_student.append(student['name']+ ' '+student['surname'])
            for lesson in student['student_skipped']:
                if date_selected in lesson:
                    total_missed_student.append(student['name']+ ' '+student['surname'])
        for employee in data_objects.employees:
            for lesson in employee['teacher_attended']:
                if date_selected in lesson:
                    total_attended_teacher.append(employee['name'] + ' ' + employee['surname'])
                    total_completed_lesson.append(employee['name'] + ' ' + employee['surname'])
                    if 'Grup' in lesson:
                        total_group_lesson.append(employee['name'] + ' ' + employee['surname'])
                    if 'Attentioner' in lesson:
                        total_attentioner_lesson.append(employee['name'] + ' ' + employee['surname'])
                    if 'Akademik' in lesson:
                        total_academic_lesson.append(employee['name'] + ' ' + employee['surname'])
            for lesson in employee['schedule_cancelled']:
                if date_selected in lesson:
                    total_cancelled_lesson.append(employee['name'] + ' ' + employee['surname'])
                    if 'Ogrenci' in lesson:
                        cancelled_by_student.append(employee['name'] + ' ' + employee['surname'])
                    if 'Ogretmen' in lesson:
                        cancelled_by_teacher.append(employee['name'] + ' ' + employee['surname'])
                    if 'Kurum' in lesson:
                        cancelled_by_company.append(employee['name'] + ' ' + employee['surname'])
        total_planned_lesson = len(total_completed_lesson) + len(total_cancelled_lesson)

        self.label.setText("Toplam Katilan Ogrenci: {}".format(len(total_attended_student)))
        self.label_2.setText("Toplam Katilan Ogretmen: {}".format(len(total_attended_teacher)))
        self.label_3.setText("Toplam Planlanan Ders: {}".format(total_planned_lesson))
        self.label_4.setText("Toplam Tamamlanan Ders: {}".format(len(total_completed_lesson)))
        self.label_5.setText("Toplam Iptal Edilen Ders: {}".format(len(total_cancelled_lesson)))
        self.label_6.setText("Toplam Ders Kaciran Ogrenci: {}".format(len(total_missed_student)))
        self.label_7.setText("Toplam Grup Dersi: {}".format(len(total_group_lesson)))
        self.label_8.setText("Toplam Attentioner Dersi: {}".format(len(total_attentioner_lesson)))
        self.label_9.setText("Toplam Akademik Ders: {}".format(len(total_academic_lesson)))
        self.label_11.setText("Iptal Edilen Ders (Ogrenci Tarafindan): {}".format(len(cancelled_by_student)))
        self.label_12.setText("Iptal Edilen Ders (Ogretmen Tarafindan): {}".format(len(cancelled_by_teacher)))
        self.label_13.setText("Iptal Edilen Ders (Kurum Tarafindan): {}".format(len(cancelled_by_company)))
        self.label_14.setText("Yapilan Deneme Dersi: {}".format(len(cancelled_by_company)))
        self.label_15.setText("Toplam Yeni Kayit: {}".format(len(cancelled_by_company)))
        self.label_16.setText("Deneme Dersi -> Kayit: {}".format(len(cancelled_by_company)))
        self.label_17.setText("Yeni Kayit (Ozel): {}".format(len(cancelled_by_company)))
        self.label_18.setText("Yeni Kayit (Raporlu): {}".format(len(cancelled_by_company)))
        self.label_19.setText("Yeni Kayit (Karma): {}".format(len(cancelled_by_company)))




    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Genel Kurum Istatistikleri"))
        self.label.setText(_translate("Dialog", "Toplam Katilan Ogrenci: "))
        self.label_2.setText(_translate("Dialog", "Toplam Katilan Ogretmen: "))
        self.label_3.setText(_translate("Dialog", "Toplam Planlanan Ders:"))
        self.label_4.setText(_translate("Dialog", "Toplam Tamamlanan Ders:"))
        self.label_5.setText(_translate("Dialog", "Toplam Iptal Edilen Ders: "))
        self.label_6.setText(_translate("Dialog", "Toplam Ders Kaciran Ogrenci: "))
        self.label_7.setText(_translate("Dialog", "Toplam Grup Dersi:"))
        self.label_8.setText(_translate("Dialog", "Toplam Attentioner Dersi:"))
        self.label_9.setText(_translate("Dialog", "Toplam Akademik Ders:"))
        self.label_10.setText(_translate("Dialog", "Aylik Ders Istatistikleri"))
        self.label_11.setText(_translate("Dialog", "Iptal Edilen Ders (Ogrenci Tarafindan): "))
        self.label_12.setText(_translate("Dialog", "Iptal Edilen Ders (Ogretmen Tarafindan): "))
        self.label_13.setText(_translate("Dialog", "Iptal Edilen Ders (Kurum Tarafindan): "))
        self.label_14.setText(_translate("Dialog", "Yapilan Deneme Dersi: "))
        self.label_15.setText(_translate("Dialog", "Toplam Yeni Kayit: "))
        self.label_16.setText(_translate("Dialog", "Deneme Dersi -> Kayit: "))
        self.label_17.setText(_translate("Dialog", "Yeni Kayit (Ozel): "))
        self.label_18.setText(_translate("Dialog", "Yeni Kayit (Raporlu): "))
        self.label_19.setText(_translate("Dialog", "Yeni Kayit (Karma): "))


def barchart_general():
    Dialog = QtWidgets.QDialog()
    Dialog.setStyle(QtWidgets.QStyleFactory.create("WindowsVista"))
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    Dialog.exec_()

