__author__ = 'Ty'


class FrcScheduleTeam:
    def __init__(self, number, station, surrogate):
        self.number = number
        self.station = station
        self.surrogate = surrogate


def create_frc_schedule_team_from_json(json):
    number = json.get('number')
    station = json.get('station')
    surrogate = json.get('surrogate')

    return FrcScheduleTeam(number, station, surrogate)