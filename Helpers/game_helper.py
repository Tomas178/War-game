import random
from Models.player import Player

DECK_SIZE = 52


def get_cards_count_per_player(players_count: int) -> int:
    return DECK_SIZE // players_count


def distribute_cards(players: list[Player], cards_count_per_player: int) -> None:
    deck = get_deck()
    random.shuffle(deck)
    for player in players:
        for _ in range(cards_count_per_player):
            player.hand.append(deck.pop())


def get_deck() -> list[str]:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]
    return deck


def get_starting_player(players: list[Player]) -> int:
    return random.randint(0, len(players) - 1)
