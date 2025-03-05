import random


class Board:
    def __init__(self, players: list):
        self.players = players
        self.deck = self.create_deck()
        self.DECK_SIZE = len(self.deck) // len(self.players)
        self.deal_cards()

    def create_deck(self) -> list[str]:
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = {
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "J": 11,
            "Q": 12,
            "K": 13,
            "A": 14,
        }
        deck = [
            (f"{rank} of {suit}", value)
            for suit in suits
            for rank, value in ranks.items()
        ]
        random.shuffle(deck)
        return deck

    def deal_cards(self) -> None:
        for player in self.players:
            for _ in range(self.DECK_SIZE):
                player.hand.append(self.deck.pop())

    def play_round(self) -> None:
        if not all(player.has_cards() for player in self.players):
            return False

        player1_card, player1_value = self.players[0].draw_card()
        player2_card, player2_value = self.players[1].draw_card()
        table_cards = [(player1_card, player1_value), (player2_card, player2_value)]

        print(f"{self.players[0].name} plays {player1_card}")
        print(f"{self.players[1].name} plays {player2_card}")

        if player1_value > player2_value:
            self.players[0].add_cards(table_cards)
            print(f"{self.players[0].name} wins the round!\n")
        elif player1_value < player2_value:
            self.players[1].add_cards(table_cards)
            print(f"{self.players[1].name} wins the round!\n")
        else:
            print("It's a tie! each player draws 3 more cards...\n")
            self.handle_tie(table_cards)

        return True

    def handle_tie(self, table_cards: list) -> None:
        for i in range(1):
            for player in self.players:
                if player.has_cards():
                    table_cards.append(player.draw_card())

        if all(player.has_cards() for player in self.players):
            player1_card, player1_value = self.players[0].draw_card()
            player2_card, player2_value = self.players[1].draw_card()
            table_cards.extend(
                [(player1_card, player1_value), (player2_card, player2_value)]
            )

            print(f"{self.players[0].name} plays {player1_card}")
            print(f"{self.players[1].name} plays {player2_card}")

            if player1_value > player2_value:
                self.players[0].add_cards(table_cards)
                print(f"{self.players[0].name} wins the round!\n")
            elif player1_value < player2_value:
                self.players[1].add_cards(table_cards)
                print(f"{self.players[1].name} wins the round!\n")
            else:
                print("Another tie! each player draws 3 more cards...\n")
                self.handle_tie(table_cards)

        else:
            winner = next(player for player in self.players if player.has_cards())
            winner.add_cards(table_cards)
            print(
                f"{winner.name} wins the round due to the reason that the opponent has no cards left\n"
            )

    def play_game(self):
        round_count = 1
        while self.play_round():
            print(f"Round {round_count} complete.")
            round_count += 1

        winner = max(self.players, key=lambda p: len(p.hand))
        print(f"{winner.name} wins the game!")
