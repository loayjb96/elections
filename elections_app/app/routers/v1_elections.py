import logging
from fastapi import HTTPException
from typing import List

from fastapi import APIRouter, Request, Query

from elections_app.app.dtos.election_dto import ElectionsRequest, ContactsElectionResponse, UpdateContactRequest
from elections_app.app.service.election_service import Elections

v1_elections_routes = APIRouter(prefix='/v1/elections', tags=['/v1/elections'])


@v1_elections_routes.post('/data',
                          response_model=List[ContactsElectionResponse],
                          description="contact information",
                          response_model_exclude_none=True)
def contact_enrichment(contacts_enrichment_request: ElectionsRequest, unused_request: Request):
    election_service = Elections()
    print(election_service)
    result = election_service.get_contact_details(contacts_enrichment_request)
    return result


@v1_elections_routes.get('/data',
                         response_model=ContactsElectionResponse,
                         description="contact information",
                         response_model_exclude_none=True)
def get_all_contact_enrichment(page: int = Query(1, alias="page")):
    election_service = Elections()
    result = election_service.get_all(page=page)
    return result


@v1_elections_routes.put('/data',
                         response_model=bool,
                         description="Update a contact's voted status")
def update_contact(update_request: UpdateContactRequest):
    election_service = Elections()

    # Validate the request
    if not update_request.id and not update_request.ballot_order_id:
        raise HTTPException(status_code=400, detail="Either id or ballot_order_id must be provided")

    # Perform the update operation
    updated_contact = election_service.update_contact_voted(update_request)

    if not updated_contact:
        raise HTTPException(status_code=404, detail="Contact not found")

    return updated_contact
