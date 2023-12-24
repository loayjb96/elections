import csv
from typing import List

from elections_app.app.db.firebase import FirebaseDataReader
from elections_app.app.dtos.election_dto import ElectionsRequest, ContactsElectionResponse


class Elections:

    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.db_access = FirebaseDataReader()

    def get_contact_details(self, request: ElectionsRequest) -> List[ContactsElectionResponse]:
        all_records = self.db_access.list_records_by_filter('תעודת זהות', request.id)
        filtered_records = []

        for id, record in all_records.items():

            filtered_records.append(ContactsElectionResponse(
                id=record['תעודת זהות'],
                first_name=record["שם פרטי"],
                last_name=record["שם משפחה"],
                father_name=record["שם אב"],
                street=record["שם רחוב"],
                house_number=record["מספר בית"],
                ballot=record["מס קלפי"],
                voted=False
            ))
        return filtered_records
