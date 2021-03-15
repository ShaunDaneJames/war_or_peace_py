class Deck:
    def __init__(self, cards):
        self.cards = cards

    def rank_of_card_at(self, index):
        return self.cards[index].rank

    def high_ranking_cards(self):
        high_ranked_list = []
        for card in self.cards:
            if card.rank > 10:
                high_ranked_list.append(card)
        return high_ranked_list

    def percent_high_ranking(self):
        return len(self.high_ranking_cards())\
               / len(self.cards)\
               * 100

    def remove_card(self):
        self.cards.pop(0)

    def add_card(self, card):
        self.cards.append(card)
