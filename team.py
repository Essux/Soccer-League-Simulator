from dataclasses import dataclass, field
from typing import List
from player import  Player

@dataclass
class Team:
    name: str
    coefficient: int
    squad: List[Player] = field(default_factory=list)
