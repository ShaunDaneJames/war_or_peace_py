import pytest
from lib.deck import *
from lib.card import *


def test_it_exists():
    card1 = Card("diamond", "Queen", 12)
    card2 = Card("spade", "3", 3)
    card3 = Card("Heart", "Ace", 14)
    cards = [card1, card2, card3]

    deck = Deck(cards)

    assert len(deck.cards) == 3


def test_rank_of_card_at():
    card1 = Card("diamond", "Queen", 12)
    card2 = Card("spade", "3", 3)
    card3 = Card("Heart", "Ace", 14)
    cards = [card1, card2, card3]

    deck = Deck(cards)

    assert deck.rank_of_card_at(0) == 12
    assert deck.rank_of_card_at(2) == 14


def test_returns_high_ranking_cards():
    card1 = Card("diamond", "Queen", 12)
    card2 = Card("spade", "3", 3)
    card3 = Card("Heart", "Ace", 14)
    cards = [card1, card2, card3]

    deck = Deck(cards)

    assert deck.high_ranking_cards()[0] == card1
    assert deck.high_ranking_cards()[1] == card3
    assert len(deck.high_ranking_cards()) == 2


def test_knows_percent_of_high_ranked_cards():
    card1 = Card("diamond", "Queen", 12)
    card2 = Card("spade", "3", 3)
    card3 = Card("Heart", "Ace", 14)
    card4 = Card("Heart", "2", 2)
    cards = [card1, card2, card3, card4]

    deck = Deck(cards)

    assert deck.percent_high_ranking() == 50.0


def test_can_remove_card():
    card1 = Card("diamond", "Queen", 12)
    card2 = Card("spade", "3", 3)
    card3 = Card("Heart", "Ace", 14)
    cards = [card1, card2, card3]

    deck = Deck(cards)
    deck.remove_card()

    assert len(deck.cards) == 2
    assert deck.cards == [card2, card3]


def test_can_add_card():
    card1 = Card("diamond", "Queen", 12)
    cards = [card1]
    deck = Deck(cards)

    assert len(deck.cards) == 1
    assert deck.percent_high_ranking() == 100.0

    card2 = Card("spade", "3", 3)
    deck.add_card(card2)

    assert deck.cards[1] == card2
    assert deck.percent_high_ranking() == 50.0