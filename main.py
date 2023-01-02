from generate import generate_squad
from results import compute_results, print_standings
from simulate import simulate_season
from team import Team


premier_league_teams = [
    "Arsenal", "Aston Villa", "Brighton & Hove Albion", "Burnley", "Chelsea",
    "Crystal Palace", "Everton", "Leeds United", "Leicester City", "Liverpool",
    "Manchester City", "Manchester United", "Newcastle United", "Norwich City",
    "Nothingham Forest",
    "Southampton", "Tottenham Hotspur", "Watford", "West Ham United", "Wolverhampton Wanderers"
]

team_coefficients = {
    "Arsenal": 75,
    "Aston Villa": 50,
    "Brighton & Hove Albion": 60,
    "Burnley": 55,
    "Chelsea": 80,
    "Crystal Palace": 65,
    "Everton": 70,
    "Leeds United": 65,
    "Leicester City": 75,
    "Liverpool": 90,
    "Manchester City": 85,
    "Manchester United": 80,
    "Newcastle United": 60,
    "Norwich City": 50,
    "Nothingham Forest": 55,
    "Southampton": 65,
    "Tottenham Hotspur": 75,
    "Watford": 60,
    "West Ham United": 70,
    "Wolverhampton Wanderers": 65
}


# Create a Team object for each team
teams = []
for i, team_name in enumerate(premier_league_teams):
    team_coefficient = team_coefficients[team_name]
    team_squad = generate_squad(team_name, team_coefficient)
    team = Team(team_name, team_coefficient, team_squad)
    teams.append(team)

# Print the teams and their squads
for team in teams:
    print(f"{team.name}: {team.coefficient}")
    print("Squad:")
    for player in team.squad:
        print(f"{player.name}: {player.coefficient}")
    print()

matches = simulate_season(teams)

team_stats = compute_results(matches)
print_standings(team_stats)
