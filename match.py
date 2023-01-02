from dataclasses import dataclass
from team import Team


@dataclass
class Match:
    team_a: Team
    team_b: Team
    score_a: int
    score_b: int
    matchweek: int
