from objects.card import Card
import random


class Deck:

    def __init__(self):
        values = [str(v) for v in range(2, 11)] + ['J', 'Q', "K", 'A']
        suits = ['spade', 'hearts', 'diamonds', 'clubs']
        self.cards = [Card(v, s) for v in values for s in suits]

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def __str__(self):
        return ", ".join([str(c) for c in self.cards])
