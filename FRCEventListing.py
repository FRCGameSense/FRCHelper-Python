__author__ = 'Ty'

import json
import FrcApiSettings


class FRCEventListingRequest:
    def __init__(self, season, eventCode):
        self.season = season
        self.eventCode = eventCode

    def __init__(self, season):
        self.season = season
        self.eventCode = ""

    def buildUri(self):
        url = FRCEventListingRequest
        url = url + self.season + "/events?"
        if self.eventCode != "":
            url = url + "eventcode=" + self.eventCode.upper();
        return url



