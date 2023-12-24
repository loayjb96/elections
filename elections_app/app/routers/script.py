import csv

import pandas as pd
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Initialize Firebase
cred = credentials.Certificate('/Users/loayjaber/elections/imported_files/elections-de049-firebase-adminsdk-6in3h-37fcce4207.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://elections-de049-default-rtdb.firebaseio.com/'
})

# Read CSV file


# Read and clean CSV file
csv_file = '/Users/loayjaber/elections/imported_files/election_names.csv'
cleaned_data = []

with open(csv_file, mode='r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    headers = next(csv_reader)

    # Rename column
    headers = ['תעודת זהות' if header == 'ת.ז' else header for header in headers]

    for row in csv_reader:
        if not any(row):
            continue

        cleaned_row = {headers[i]: cell.strip() for i, cell in enumerate(row) if cell}
        if cleaned_row:
            cleaned_row.pop("")
            cleaned_data.append(cleaned_row)

# Write cleaned data to Firebase
ref = db.reference('/')  # Reference to the root of your database
for index, item in enumerate(cleaned_data):
    try:
        ref.push(item)
        print(f"Uploaded item {index + 1}/{len(cleaned_data)}")
    except Exception as e:
        print(f"Error uploading item {index + 1}: {e}")
        print(f"Problematic item data: {item}")
        break

print("Data upload process completed.")