# -*- coding: utf-8 -*-

import csv
#from google.cloud import storage
import os


'''def upload_files(file_name):
    key_path = 'keyfile.json'
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = key_path
    # Create a storage client
    client = storage.Client()

    # Get the bucket to upload to
    bucket_name = 'bucket_disdem'
    bucket = client.get_bucket(bucket_name)

    # Upload the file
    file_path = file_name
    blob = bucket.blob(file_name)
    blob.upload_from_filename(file_path)

def download_files(file_name):
    key_path = 'keyfile.json'
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = key_path
    client = storage.Client()

    # Get the bucket to download from
    bucket_name = 'bucket_disdem'
    bucket = client.get_bucket(bucket_name)

    # Download the file
    blob = bucket.blob(file_name)
    file_path = file_name
    blob.download_to_filename(file_path)

def txt_to_csv(file_txt, file_csv):
    with open(file_txt, 'r', encoding="utf-8") as file:
        data = eval(file.read())  # Convert the text to a list of dictionaries

    # Get the keys of the first dictionary in the list
    headers = list(data[0].keys())

    # Open a new CSV file to write the data
    with open(file_csv, 'w', newline='', encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)

        # Write the column headers to the CSV file
        writer.writeheader()

        # Write each dictionary in the list to a new row in the CSV file
        for row in data:
            writer.writerow(row)

def convert_txt_csv_all():
    txt_to_csv('student_data.txt','student_data.csv')
    txt_to_csv('employee_data.txt','employee_data.csv')
    txt_to_csv('user_list.txt','user_list.csv')'''

#download_files('employee_data.txt')





