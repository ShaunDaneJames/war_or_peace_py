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

