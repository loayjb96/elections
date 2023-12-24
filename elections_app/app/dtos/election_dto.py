from typing import Optional

from elections_app.utils import BaseDTODict


class ElectionsRequest(BaseDTODict):
    id: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None


class ContactsElectionResponse(BaseDTODict):
    id: str
    first_name: Optional[str]
    last_name: Optional[str]
    father_name: Optional[str]
    street: Optional[str]
    house_number: Optional[str]
    ballot: Optional[str]
    voted: Optional[bool] = False
