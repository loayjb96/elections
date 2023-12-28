import csv
from typing import List

from elections_app.app.dtos.election_dto import ElectionsRequest, ContactsElectionResponse
from elections_app.app.persistency.contacts_db_access import ContactsDbAccess


class Elections:

    def __init__(self):
        self.db_access = ContactsDbAccess({})

    def get_contact_details(self, request: ElectionsRequest) -> List[ContactsElectionResponse]:
        # Determine the search criterion and value from the request
        if request.identity_number:
            criterion, value = 'identity_number', request.identity_number
        elif request.ballot_number:
            criterion, value = 'ballot_number', request.ballot_number
        elif request.ballot_order_number:
            criterion, value = 'ballot_order_number', request.ballot_order_number
        else:
            raise ValueError("No valid search criterion provided in the request")

        # Search for records using the new method
        all_records = self.db_access.search_contacts(criterion, value)
        filtered_records = []

        for record in all_records:
            filtered_records.append(ContactsElectionResponse(
                id=record.identity_number,
                first_name=record.first_name,
                last_name=record.last_name,
                father_name=record.father_name,
                street=record.street_name,  # Assuming street_name is the correct field
                house_number=record.house_number,
                ballot=record.ballot_number,
                voted=False  # Assuming default value as False
            ))
        return filtered_records

    def get_all(self, page: int) -> List[ContactsElectionResponse]:
        # Retrieve all records from the database
        all_records = self.db_access.get_all(page)  # Assuming get_all_contacts is the method to fetch all records
        all_contacts = []

        for record in all_records:
            all_contacts.append(ContactsElectionResponse(
                id=record.identity_number,
                first_name=record.first_name,
                last_name=record.last_name,
                father_name=record.father_name,
                street=record.street_name,  # Assuming street_name is the correct field
                house_number=record.house_number,
                ballot=record.ballot_number,
                voted=False  # Assuming default value as False
            ))
        return all_contacts
