import re

import data_objects
import json

def check_table_versus_file():
    with open('student_data.txt', 'r', encoding="utf-8") as f:
        data_objects.students = json.load(f)
    with open('employee_data.txt', 'r', encoding="utf-8") as f:
        data_objects.employees = json.load(f)

    for employee in data_objects.employees:
        if employee['status'] == "" or employee['status'] == " ":
            employee['status'] = "Aktif           01-05-2023"
        else:
            pass
    for student in data_objects.students:
        if student['status'] == "" or student['status'] == " ":
            student['status'] = "Aktif           13-05-2023"
        else:
            pass
    for student in data_objects.students:
        if 'Aktif' in student['status']:
            student['student_left'] = "-"
        else:
            pass

    with open("student_data.txt", "w", encoding="utf-8") as f:
        f.writelines(json.dumps(data_objects.students, default=str))
    with open("employee_data.txt", "w", encoding="utf-8") as f:
        f.writelines(json.dumps(data_objects.employees, default=str))


def check_lesson_empty():
    with open('employee_data.txt', 'r', encoding="utf-8") as f:
        data_objects.employees = json.load(f)

    for employee in data_objects.employees:
        for schedule in employee['teacher_schedule']:
            if 'Ders []' in schedule or 'Dersi []' in schedule:
                employee['teacher_schedule'].remove(schedule)
            else:
                pass

    with open("employee_data.txt", "w", encoding="utf-8") as f:
        f.writelines(json.dumps(data_objects.employees, default=str))


