
from collections import defaultdict
from dataclasses import dataclass
from typing import Dict, List

from match import Match


@dataclass
class TeamStats:
    goals_scored: int
    goals_against: int
    matches_won: int
    matches_tied: int
    matches_lost: int
    goal_difference: int
    points: int

def compute_results(matches: List[Match]) -> Dict[str, TeamStats]:
    # Dictionary to store the stats for each team
    team_stats = defaultdict(lambda: TeamStats(0, 0, 0, 0, 0, 0, 0))
    
    # Calculate the stats for each match
    for match in matches:
        # Get the stats for each team
        stats_a = team_stats[match.team_a.name]
        stats_b = team_stats[match.team_b.name]
        
        # Increment the goals scored and goals against for each team
        stats_a.goals_scored += match.score_a
        stats_a.goals_against += match.score_b
        stats_b.goals_scored += match.score_b
        stats_b.goals_against += match.score_a
        
        # Increment the matches won, tied or lost for each team
        if match.score_a > match.score_b:
            stats_a.matches_won += 1
            stats_b.matches_lost += 1
        elif match.score_a < match.score_b:
            stats_a.matches_lost += 1
            stats_b.matches_won += 1
        else:
            stats_a.matches_tied += 1
            stats_b.matches_tied += 1
        
        # Calculate the goal difference and points for each team
        stats_a.goal_difference = stats_a.goals_scored - stats_a.goals_against
        stats_b.goal_difference = stats_b.goals_scored - stats_b.goals_against
        stats_a.points = 3 * stats_a.matches_won + stats_a.matches_tied
        stats_b.points = 3 * stats_b.matches_won + stats_b.matches_tied
    
    return team_stats

def print_standings(team_stats: Dict[str, TeamStats]) -> None:
    # Sort the teams by points in descending order
    sorted_teams = sorted(team_stats.items(), key=lambda x: x[1].points, reverse=True)
    
    # Print the table header
    print("{:<30} {:>10} {:>10} {:>10} {:>10} {:>10} {:>10} {:>10}".format(
        "Team", "GS", "GA", "W", "T", "L", "GD", "Pts"
    ))
    print("-" * 120)
    
    # Print the stats for each team
    for team, stats in sorted_teams:
        print("{:<30} {:>10} {:>10} {:>10} {:>10} {:>10} {:>10} {:>10}".format(
            team, stats.goals_scored, stats.goals_against, stats.matches_won, stats.matches_tied,
            stats.matches_lost, stats.goal_difference, stats.points
        ))
