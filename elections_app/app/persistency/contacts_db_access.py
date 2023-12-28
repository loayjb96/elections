import logging
from typing import Optional

from sqlalchemy.exc import SQLAlchemyError

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

    def get_all(self, page: int = 1, page_size: int = 25):
        with Session(self.engine) as session:
            # Calculate offset
            offset = (page - 1) * page_size
            # Query with limit and offset for pagination
            return session.query(Contact).offset(offset).limit(page_size).all()

    def update_contact_voted_status(self, id: Optional[str], ballot_order_id: Optional[str], voted: bool):
        with Session(self.engine) as session:
            try:
                query = session.query(Contact)
                if id:
                    query = query.filter(Contact.identity_number == id)
                if ballot_order_id:  # Changed to a separate if statement
                    query = query.filter(Contact.ballot_order_id == ballot_order_id)

                contact = query.one_or_none()

                if contact:
                    contact.voted = voted
                    session.commit()
                    return contact
                else:
                    return None
            except SQLAlchemyError as e:
                logging.error(f"Database error occurred: {e}")
                # Depending on how you want to handle errors, you might raise an exception here
                # or return a specific value indicating an error occurred.
                return None


