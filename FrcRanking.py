__author__ = 'ttremblay'

class FrcRanking:
    def __init__(self, rank, team_id, qual_score, hybrid_points, assist_points, truss_and_catch_points, teleop_points, wins, losses, ties, dq, matches_played):
        self.rank = rank
        self.team_id = team_id
        self.qual_score = qual_score
        self.hybrid_points = hybrid_points
        self.assist_points = assist_points
        self.truss_and_catch_points = truss_and_catch_points
        self.teleop_points = teleop_points
        self.wins = wins
        self.losses = losses
        self.ties = ties
        self.dq = dq
        self.matches_played = matches_played

def create_frc_ranking_from_json(json):
    rank = json.get('Rank')
    team_id = json.get('TeamId')
    qual_score = json.get('QualScore')
    hybrid_points = json.get('HybridPoints')
    assist_points = json.get('AssistPoints')
    truss_and_catch_points = json.get('TrussAndCatchPoints')
    teleop_points = json.get('TeleopPoints')
    wins = json.get('Wins')
    losses = json.get('Losses')
    ties = json.get('Ties')
    dq = json.get('DQ')
    matches_played = json.get('MatchesPlayed')

    return FrcRanking(rank, team_id, qual_score, hybrid_points, assist_points, truss_and_catch_points, teleop_points, wins, losses, ties, dq, matches_played)