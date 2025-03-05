from Models.player import Player
from Helpers import user_input_helper, game_helper


def main():
    print("Welcome to War!")
    players_count = user_input_helper.get_players_count()
    cards_count_per_player = game_helper.get_cards_count_per_player(players_count)
    players = user_input_helper.get_players(players_count, cards_count_per_player)
    game_helper.distribute_cards(players, cards_count_per_player)

    for player in players:
        print(f"{player.name} has been dealt the following cards:")
        print(player.hand)
        print()


if __name__ == "__main__":
    main()
