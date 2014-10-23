__author__ = 'ttremblay'

import FrcApiSettings
import FrcEvent
import FrcRanking
import FrcScheduleMatch
import logging


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
        self.convert_to_object(json_obj)

    def convert_to_object(self, json_obj):
        events_dict_list = json_obj.get('Events')

        for item in events_dict_list:
            self.events_list.append(FrcEvent.create_frc_event_from_json(item))

        self.event_count = json_obj.get('eventCount')


class FrcRankingsRequest:
    def __init__(self, season, event_code, top=0):  # if top is 0, gets all rankings data
        self.season = season
        self.event_code = event_code
        self.top = top

    def build_uri(self):
        url = FrcApiSettings.frc_api_url
        url = url + "rankings/" + str(self.season) + "/" + self.event_code
        if self.top != 0:
            url = url + "?" + str(self.top)
        return url


class FrcRankingsResponse:
    def __init__(self, json):
        self.rankings_list = []
        self.convert_to_object(json)

    def convert_to_object(self, json):
        json_rankings = json.get('Rankings')
        for ranking in json_rankings:
            self.rankings_list.append(FrcRanking.create_frc_ranking_from_json(ranking))

    @property
    def to_string(self):
        output_string = ""
        for rank in self.rankings_list:
            output_string += "{0}. {1} ({2}-{3}-{4}, {5} Assist)    ".format(str(rank.rank), str(rank.team_id),
                                                                             str(rank.wins), str(rank.losses),
                                                                             str(rank.ties),
                                                                             str(round(rank.assist_points)).rstrip('0').rstrip('.'))

        return output_string


class FrcScheduleRequest:
    def __init__(self, season, event_code, tournament_level):
        self.season = season
        self.event_code = event_code
        self.tournament_level = tournament_level

    def build_uri(self):
        url = FrcApiSettings.frc_api_url
        url += "schedule/" + str(self.season) + "/" + self.event_code + "/" + self.tournament_level
        return url


class FrcScheduleResponse:
    def __init__(self, json):
        self.schedule = []
        self.convert_to_object(json)

    def convert_to_object(self, json):
        json_schedule = json.get('Schedule')
        for match in json_schedule:
            self.schedule.append(FrcScheduleMatch.create_frc_schedule_match_from_json(match))

        return self.schedule

