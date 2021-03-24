import random


class Game:
    def __init__(self, player1, player2, turn):
        self.player1 = player1
        self.player2 = player2
        self.turn = turn

    def start(self):
        # self.deal_cards()
        self.turn_logic()
        return self.grand_winner()
    # def deal_cards(self):
    #     random.shuffle(self.deck.cards)
    #     import pdb; pdb.set_trace()
    #     self.player1.deck.cards.clear()
    #     self.player2.deck.cards.clear()
    #     self.player1.deck.cards = self.deck.cards[0:25]
    #     self.player2.deck.cards = self.deck.cards[26:52]


    def turn_logic(self):
        turn_count = 0
        while not (self.player1.has_lost() or self.player2.has_lost() or turn_count == 1000000):
            winner = self.turn.winner()
            if winner == "No Winner":
                print("Mutually assured destruction 6 cards removed from play")
                self.turn.pile_cards()
            else:
                print("Turn " + str(turn_count) + self.turn.type() + ": " + str(winner.name) + ' won... ')
                self.turn.pile_cards()
                print(str(len(self.turn.spoils)) + ' cards!')
                self.turn.award_spoils(winner)
            turn_count += 1


    def grand_winner(self):
        if self.player1.has_lost():
            return self.player2.name
        else:
            return self.player1.name