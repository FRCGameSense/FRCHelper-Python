__author__ = 'Ty'

import FrcScheduleTeam
import json

class FrcScheduleMatch:
    def __init__(self, description, level, start_time, match_number, teams):
        self.description = description
        self.level = level
        self.start_time = start_time
        self.match_number = match_number
        self.teams = teams

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


def create_frc_schedule_match_from_json(json):
    description = json.get('description')
    level = json.get('level')
    start_time = json.get('startTime')
    match_number = json.get('matchNumber')
    teams = []
    json_teams = json.get('Teams')

    for team in json_teams:
        teams.append(FrcScheduleTeam.create_frc_schedule_team_from_json(team))

    return FrcScheduleMatch(description, level, start_time, match_number, teams)