from dataclasses import dataclass


@dataclass
class Player:
    name: str
    hand: tuple[str, int]

    def draw_card(self) -> str:
        return self.hand.pop(0) if self.hand else None

    def add_cards(self, cards: list[str]):
        self.hand.extend(cards)

    def has_cards(self) -> bool:
        return len(self.hand) > 0

    def __str__(self):
        return self.name
