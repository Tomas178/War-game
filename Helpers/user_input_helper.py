from Models.player import Player


def get_players_names() -> list[Player]:
    players = []
    players_count = 2
    for i in range(players_count):
        name = input(f"Enter the name of player {i + 1}: ")
        players.append(Player(name, []))
    return players
