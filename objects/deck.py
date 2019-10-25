from objects.card import Card, Suits
import random


class Deck:

    def __init__(self, n_sets=2):
        values = [str(v) for v in range(2, 11)] + ['J', 'Q', "K", 'A']
        suits = [Suits.S, Suits.C, Suits.H, Suits.D]
        self.cards = []
        for _ in range(n_sets):
            self.cards.extend([Card(v, s) for v in values for s in suits])

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def __str__(self):
        return ", ".join([str(c) for c in self.cards])
