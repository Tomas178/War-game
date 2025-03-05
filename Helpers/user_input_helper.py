from Models.player import Player
from Helpers import game_helper


def get_players_count() -> int:
    players_count = 0
    while True:
        try:
            players_count = int(input("Enter the number of players (2-4): "))
            if players_count < 2 or players_count > 4:
                print("Invalid input. Please enter a number between 2 and 4.")
                continue
            return players_count
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue


def get_players(players_count: int, cards_count_per_player) -> list[Player]:
    players = []
    for i in range(players_count):
        name = input(f"Enter the name of player {i + 1}: ")
        players.append(Player(name, cards_count_per_player, []))
    return players
