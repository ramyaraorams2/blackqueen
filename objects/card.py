class Card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def get_points(self):
        if self.value not in ['A', 'Q', '10', '5']:
            return 0
        else:
            if self.value == 'Q' and self.suit == 'spade':
                return 30
            elif self.value == 'A':
                return 15
            else:
                return int(self.value)

    def __str__(self):
        return "{} : {}".format(self.value, self.suit)

    def __eq__(self, other):
        flg = (self.suit == other.suit and
               self.value == other.value)
        return flg
