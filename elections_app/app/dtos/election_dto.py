from typing import Optional, List

from elections_app.utils import BaseDTODict


class ElectionsRequest(BaseDTODict):
    identity_number: Optional[str] = None
    ballot_number: Optional[str] = None
    ballot_order_number: Optional[str] = None


class ContactInfo(BaseDTODict):
    id: str
    first_name: Optional[str]
    last_name: Optional[str]
    father_name: Optional[str]
    street: Optional[str]
    house_number: Optional[str]
    ballot: Optional[str]
    voted: Optional[bool]


class ContactsElectionResponse(BaseDTODict):
    results: List[Optional[ContactInfo]]
    total_rows: Optional[int]
    total_pages: Optional[int]


class UpdateContactRequest(BaseDTODict):
    id: Optional[str] = None
    ballot_order_id: Optional[str] = None
    voted: bool
