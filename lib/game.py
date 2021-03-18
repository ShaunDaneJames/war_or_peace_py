import random


class Game:
    def __init__(self, player1, player2, deck, turn):
        self.player1 = player1
        self.player2 = player2
        self.deck = deck
        self.turn = turn

    def start(self):
        self.deal_cards()
        self.turn_logic()

    def deal_cards(self):
        random.shuffle(self.deck.cards)

        self.player1.deck.cards.append(self.deck.cards[0:25])
        self.player2.deck.cards.append(self.deck.cards[26:52])

    def turn_logic(self):
        while not self.player1.has_lost() or self.player2.has_lost():
            self.turn.pile_cards()
            print(self.turn.winner() + ' won ' + str(len(self.turn.spoils)) + ' cards!')
            self.turn.award_spoils(self.turn.winner)

