from elections_app.app.persistency.base_repo_db_access import BaseDbAccess
from sqlalchemy.orm import Session

from elections_app.app.persistency.db_entities import Contact


class ContactsDbAccess(BaseDbAccess):

    @staticmethod
    def get_schema_name():
        return 'contacts'

    def get_contacts_info(self):
        with Session(self.engine) as session:
            return session.query(Contact).all()

    def insert_contacts_info(self, contact_info: dict):
        new_contact = Contact(**contact_info)
        with Session(self.engine) as session:
            session.add(new_contact)
            session.commit()

    def search_contacts(self, search_criterion: str, search_value: str):
        with Session(self.engine) as session:
            if search_criterion == 'identity_number':
                return session.query(Contact).filter(Contact.identity_number == search_value).all()
            elif search_criterion == 'ballot_number':
                return session.query(Contact).filter(Contact.ballot_number == search_value).all()
            elif search_criterion == 'ballot_order_number':
                return session.query(Contact).filter(Contact.ballot_order_number == search_value).all()
            else:
                raise ValueError("Invalid search criterion")
