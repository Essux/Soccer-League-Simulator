from collections import Counter
import random
import itertools
from typing import List, Tuple
from distributions import sample_poisson
from match import Match

from team import Team

def simulate_match(team_a: Team, team_b: Team, matchweek : int) -> Match:
    # Calculate the expected goals for each team based on their coefficients
    expected_goals_a = team_a.coefficient / 40
    expected_goals_b = team_b.coefficient / 40
    
    # Sample the number of goals scored by each team from a Poisson distribution
    goals_a = sample_poisson(expected_goals_a)
    goals_b = sample_poisson(expected_goals_b)
    
    # Create a Match object with the teams and scores
    match = Match(team_a, team_b, goals_a, goals_b, matchweek=matchweek)
    return match


def shuffle_list_halves(lst: List) -> None:
    # Split the list into two halves
    half = len(lst) // 2
    first_half = lst[:half]
    second_half = lst[half:]
    
    # Shuffle the two halves
    random.shuffle(first_half)
    random.shuffle(second_half)
    
    # Concatenate the shuffled halves and assign them back to the original list
    lst[:half] = first_half
    lst[half:] = second_half

def simulate_season(teams: List[Team]) -> List[Match]:
    # List to store the matches
    matches = []
    N = len(teams)
    random.shuffle(teams)

    # Add a dummy team if the number of teams is odd
    if N % 2 == 1:
        raise ValueError("Odd number of teams not supported")

    # List to store the matches
    matches = []
    
    # Generate the pairings for each round
    for round in range(2 * (N - 1)):
        # Split the teams into two halves
        first_half = teams[:int(N/2)]
        second_half = list(reversed(teams[int(N/2):]))

        if round >= N - 1:
            first_half, second_half = second_half, first_half
        
        # Generate the round pairings
        round_matches = []
        for element in range(len(first_half)):
            round_matches.append((first_half[element], second_half[element]))
        
        # Add the round pairings to the list of matches
        matches.extend(round_matches)
        
        # Rotate the teams for the next round
        teams = teams[0:1] + teams[2:] + teams[1:2]

    # List to store the matches for each matchweek
    matchweeks = []
    for i in range(0, len(matches), 10):
        matchweek = matches[i:i+10]
        matchweeks.append(matchweek)

    shuffle_list_halves(matchweeks)
    
    # Simulate the scores for each match
    simulated_matches = []
    matchweek_number = 1
    for matchweek in matchweeks:
        # Print the matchweek title
        print(f"Matchweek {matchweek_number}:")
        matchweek_number += 1
        
        for team_a, team_b in matchweek:
            simulated_match = simulate_match(team_a, team_b, matchweek=matchweek_number)
            simulated_matches.append(simulated_match)
            
            # Print the scores for the match
            print(f"{simulated_match.team_a.name} {simulated_match.score_a} - {simulated_match.score_b} {simulated_match.team_b.name}")
    
    return simulated_matches
