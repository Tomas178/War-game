from dataclasses import dataclass


@dataclass
class Player:
    id: int
    name: str
    hand_size: int
    hand: list

    def draw_card(self) -> str:
        return self.hand.pop()
