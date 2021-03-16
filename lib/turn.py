class Turn:
    def __init__(self, player1, player2, spoils=[]):
        self.player1 = player1
        self.player2 = player2
        self.spoils = spoils

    def type(self):
        if self.player1.deck.rank_of_card_at(0) != self.player2.deck.rank_of_card_at(0):
            return "basic"
        elif self.player1.deck.rank_of_card_at(0) == self.player2.deck.rank_of_card_at(0)\
                and self.player1.deck.rank_of_card_at(1) == self.player2.deck.rank_of_card_at(1):
            return "MAD"
        else:
            return "war"