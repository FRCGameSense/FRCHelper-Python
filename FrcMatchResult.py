__author__ = 'ttremblay'


class FrcMatchResult:
    def __init__(self, actual_start_time, description, level, number, score_red_final, score_red_foul, score_red_auto,
                 score_blue_final, score_blue_foul, score_blue_auto, team_list):
        self.actual_start_time = actual_start_time
        self.description = description
        self.level = level
        self.number = number
        self.score_red_final = score_red_final
        self.score_red_foul = score_red_foul
        self.score_red_auto = score_red_auto
        self.score_blue_final = score_blue_final
        self.score_blue_foul = score_blue_foul
        self.score_blue_auto = score_blue_auto
        self.team_list = team_list


def create_frc_match_result_from_json(json):
    actual_start_time = json.get("actualStartTime")
    description = json.get('description')
    level = json.get('level')
    number = json.get('number')
    score_red_final = json.get('scoreRedFinal')
    score_red_foul = json.get('scoreRedFoul')
    score_red_auto = json.get('scoreRedAuto')
    score_blue_final = json.get('scoreBlueFinal')
    score_blue_foul = json.get('scoreBlueFoul')
    score_blue_auto = json.get('scoreBlueAuto')
    team_list = json.get('Teams')

    return FrcMatchResult(actual_start_time, description, level, number, score_red_final, score_red_foul,
                          score_red_auto, score_blue_final, score_blue_foul, score_blue_auto, team_list)
