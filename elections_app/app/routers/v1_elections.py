import logging
from typing import List

from fastapi import APIRouter, Request, Query

from elections_app.app.dtos.election_dto import ElectionsRequest, ContactsElectionResponse
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
                         response_model=List[ContactsElectionResponse],
                         description="contact information",
                         response_model_exclude_none=True)
def get_all_contact_enrichment(page: int = Query(1, alias="page")):
    election_service = Elections()
    result = election_service.get_all(page=page)
    return result

