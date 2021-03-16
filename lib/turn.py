class Turn:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.spoils = []

    def type(self):
        if self.player1.deck.rank_of_card_at(0) != self.player2.deck.rank_of_card_at(0):
            return "basic"
        elif self.player1.deck.rank_of_card_at(0) == self.player2.deck.rank_of_card_at(0)\
                and self.player1.deck.rank_of_card_at(2) == self.player2.deck.rank_of_card_at(2):
            return "MAD"
        else:
            return "war"

    def winner(self):
        if self.type() == "basic":
            return self.find_basic_winner()
        if self.type() == "war":
            return self.find_war_winner()
        else:
            return "No Winner"

    def find_basic_winner(self):
        if self.player1.deck.rank_of_card_at(0) > self.player2.deck.rank_of_card_at(0):
            return self.player1
        else:
            return self.player2

    def find_war_winner(self):
        if self.player1.deck.rank_of_card_at(2) > self.player2.deck.rank_of_card_at(2):
            return self.player1
        else:
            return self.player2

    def pile_cards(self):
        if self.type() == "basic":
            return self.pile_basic()
        if self.type() == "war":
            return self.pile_war()

    def pile_basic(self):
        self.spoils.append(self.player1.deck.remove_card())
        self.spoils.append(self.player2.deck.remove_card())
        return self.spoils

    def pile_war(self):
        for c in range(3):
            self.spoils.append(self.player1.deck.remove_card())
        for c in range(3):
            self.spoils.append(self.player2.deck.remove_card())
        return self.spoils
