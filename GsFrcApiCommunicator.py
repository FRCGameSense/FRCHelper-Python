__author__ = 'Ty'

import FRCEventListing
from urllib2 import Request, urlopen
import json


def getEventListing(season, eventCode):
    eventRequest = FRCEventListing.FRCEventListingRequest(season, eventCode)

    requestUri = eventRequest.buildUri()

    apiResponseString = sendAndGetResponse(requestUri)




def sendAndGetResponse(uri):
    request = Request(uri)
    Request.add_header(request, "Accept", "application/json")
    Request.add_header(request, "Authorization", "Token communitysampletoken")
    response_body = urlopen(request).read()

    return response_body

