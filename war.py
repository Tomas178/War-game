from Models.player import Player
from Models.board import Board
from Helpers import user_input_helper


def main():
    print("Welcome to War!")
    players = user_input_helper.get_players_names()
    game = Board(players)
    game.play_game()
    print("Game Over!")


if __name__ == "__main__":
    main()
