from dataclasses import dataclass


@dataclass
class Player:
    name: str
    hand_size: int
    hand: list
