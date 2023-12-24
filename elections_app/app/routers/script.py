import csv

# Database configuration (if needed)
from elections_app.app.persistency.contacts_db_access import ContactsDbAccess

db_config = {
    # Your database configuration details
}

# Initialize ContactsDbAccess
contacts_db_access = ContactsDbAccess(db_config=db_config)

# Read and clean CSV file
csv_file = '/Users/loayjaber/elections/imported_files/election_names.csv'
cleaned_data = []

# Define the mapping from Hebrew to English
field_mapping = {
    'ת.ז': 'identity_number',
    'שם משפחה': 'last_name',
    'שם פרטי': 'first_name',
    'שם אב': 'father_name',
    'סמל יישוב': 'locality_code',
    'סמל יישוב ': 'locality_code',
    'מס קלפי': 'ballot_number',
    'שם יישוב': 'locality_name',
    'סמל רחוב': 'street_code',
    'שם רחוב': 'street_name',
    'מספר בית': 'house_number',
    'מס סידורי קלפי ': 'ballot_order_number',
    'מיקוד ': 'postal_code',
    # Add more mappings as needed
}

with open(csv_file, mode='r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    headers = next(csv_reader)

    # Translate column names to English
    headers = [field_mapping.get(header, header) for header in headers]

    for row in csv_reader:
        if not any(row):
            continue

        cleaned_row = {headers[i]: cell.strip() for i, cell in enumerate(row) if cell}
        if cleaned_row:
            cleaned_row.pop("", None)
            cleaned_data.append(cleaned_row)

# Write cleaned data to PostgreSQL using ContactsDbAccess
for index, item in enumerate(cleaned_data):
    try:
        contacts_db_access.insert_contacts_info(item)
        print(f"Uploaded item {index + 1}/{len(cleaned_data)}")
    except Exception as e:
        print(f"Error uploading item {index + 1}: {e}")
        print(f"Problematic item data: {item}")
        break

print("Data upload process completed.")
