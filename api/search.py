import requests
from .constants import DOMAIN

PATHNAME = 'groceries/en-GB/promotions/alloffers'

def buildSearchUrl(domain=DOMAIN, pathname=PATHNAME):
    return DOMAIN + PATHNAME

def buildSearchParams(pageNumber):
    return {'page': pageNumber}

def fetchSearchResults(pageNumber=1):
    return requests.get(
        buildSearchUrl(),
        params=buildSearchParams(pageNumber)
        )

def fetchAllSearchResults():
    responses = []
    pageNumber = 1
    
    while True:
        response = fetchSearchResults(pageNumber)
        if response.ok:
            responses.append(response)
        else:
            return responses
