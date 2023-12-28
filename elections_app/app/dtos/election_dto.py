from typing import Optional

from elections_app.utils import BaseDTODict


class ElectionsRequest(BaseDTODict):
    identity_number: Optional[str] = None
    ballot_number: Optional[str] = None
    ballot_order_number: Optional[str] = None


class ContactsElectionResponse(BaseDTODict):
    id: str
    first_name: Optional[str]
    last_name: Optional[str]
    father_name: Optional[str]
    street: Optional[str]
    house_number: Optional[str]
    ballot: Optional[str]
    voted: Optional[bool]


class UpdateContactRequest(BaseDTODict):
    id: Optional[str] = None
    ballot_order_id: Optional[str] = None
    voted: bool
