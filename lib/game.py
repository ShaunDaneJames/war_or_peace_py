import random


class Game:
    def __init__(self, player1, player2, turn):
        self.player1 = player1
        self.player2 = player2
        self.turn = turn

    def start(self):
        # self.deal_cards()
        self.turn_logic()

    # def deal_cards(self):
    #     random.shuffle(self.deck.cards)
    #     import pdb; pdb.set_trace()
    #     self.player1.deck.cards.clear()
    #     self.player2.deck.cards.clear()
    #     self.player1.deck.cards = self.deck.cards[0:25]
    #     self.player2.deck.cards = self.deck.cards[26:52]


    def turn_logic(self):
        while not self.player1.has_lost() or self.player2.has_lost():
            self.turn.pile_cards()
            if self.turn.winner() == "No Winner":
                print("Mutually assured destruction 6 cards removed from play")
            else:
                print(self.turn.type() + ": " + str(self.turn.winner().name) + ' won ' + str(len(self.turn.spoils)) + ' cards!')
                self.turn.award_spoils(self.turn.winner())
            if self.player1.has_lost() or self.player2.has_lost():
                break