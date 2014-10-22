__author__ = 'ttremblay'


class FrcEvent:
    def __init__(self, code, name, type, district_code, venue, location, dateStart, dateEnd):
        self.code = code
        self.name = name
        self.type = type
        self.district_code = district_code
        self.venue = venue
        self.location = location
        self.dateStart = dateStart
        self.dateEnd = dateEnd



def create_frc_event_from_json(json_obj):
    code = json_obj.get('code')
    name = json_obj.get('name')
    type = json_obj.get('type')
    district_code = json_obj.get('districtCode')
    venue = json_obj.get('venue')
    location = json_obj.get('location')
    date_start = json_obj.get('dateStart')
    date_end = json_obj.get('dateEnd')

    return FrcEvent(code, name, type, district_code, venue, location, date_start, date_end)

