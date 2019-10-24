
class Player:

    def __init__(self):
        self.dealt_set = []
        self.hands_won = []
        self.score_cards = []
        self.score = 0

    def deal_card(self, card):
        self.dealt_set.append(card)

    def play_card(self, card):
        if card in self.dealt_set:
            self.dealt_set.remove(card)
        else:
            msg = ("Invalid card! Player's hand "
                   "does not contain that card")
            raise IndexError(msg)

    def add_hand_won(self, hand_played):
        self.hands_won.append(hand_played)
        for card in hand_played:
            pts = card.get_points()
            if pts != 0:
                self.score_cards.append(card)
                self.score += pts
