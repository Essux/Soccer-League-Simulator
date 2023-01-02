import random
import string
from typing import List
from player import  Player

def generate_squad(team_name: str, team_coefficient: int) -> List[Player]:
    squad = []
    for i in range(11):
        # Generate a random name for the player
        name = ''.join(random.choices(string.ascii_letters, k=10))
        
        # Sample the player's coefficient from a normal distribution with mean team_coefficient and standard deviation of 5
        coefficient = int(random.normalvariate(team_coefficient, 5))
        
        # Clamp the coefficient to the range 1-100
        coefficient = max(1, min(coefficient, 100))
        
        player = Player(name, coefficient)
        squad.append(player)
    return squad
