from objects.card import Card, Suits
from objects.deck import Deck
from objects.player import Player


class GameService:

    def __init__(self):
        self.deck = Deck(n_sets=2)
        self.players = []
        self.trump_suit = None

    def set_table(self, n_players=6):
        self.players = [Player() for _ in range(n_players)]
        while len(self.deck.cards) % n_players != 0:
            rand_card = Card(value='2', suit=Suits.get_random_suit())
            if rand_card in self.deck.cards:
                self.deck.cards.remove(rand_card)

    def deal_cards(self):
        while len(self.deck.cards) != 0:
            for player in self.players:
                player.deal_card(self.deck.cards.pop())


