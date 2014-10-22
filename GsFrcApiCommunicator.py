__author__ = 'Ty'

import FrcApi as api
from urllib2 import Request, urlopen
import json


def get_event_listing(season, event_code):
    event_request = api.FrcEventListingRequest(season, event_code)
    request_uri = event_request.build_uri()
    api_response_string = send_and_get_response(request_uri)
    json_obj = json.loads(api_response_string)
    event_listing_response = api.FrcEventListingResponse(json_obj)
    return event_listing_response

def get_rankings(season, event, top=0):
    rankings_request = api.FrcRankingsRequest(season, event, top)
    request_uri = rankings_request.build_uri()
    api_response_string = send_and_get_response(request_uri)
    json_obj = json.loads(api_response_string)
    rankings_response = api.FrcRankingsResponse(json_obj)
    return rankings_response


def send_and_get_response(uri):
    request = Request(uri)
    Request.add_header(request, "Accept", "application/json")
    Request.add_header(request, "Authorization", "Token communitysampletoken")
    response_body = urlopen(request).read()

    return response_body