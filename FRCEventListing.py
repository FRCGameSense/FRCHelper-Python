__author__ = 'Ty'

import FrcApiSettings
import FrcEvent


class FrcEventListingRequest:
    def __init__(self, season, event_code):
        self.season = season
        self.eventCode = event_code

    def build_uri(self):
        url = FrcApiSettings.frc_api_url
        url = url + str(self.season) + "/events?"
        if self.eventCode != "":
            url = url + "eventcode=" + self.eventCode.upper()
        return url


class FrcEventListingResponse:
    def __init__(self, json_obj):
        self.events_list = []
        self.event_count = 0
        self.deserialize(json_obj)

    def deserialize(self, json_obj):
        events_dict_list = json_obj.get('Events')

        for item in events_dict_list:
            self.events_list.append(FrcEvent.create_frc_event_from_json(item))

        self.event_count = json_obj.get('eventCount')




