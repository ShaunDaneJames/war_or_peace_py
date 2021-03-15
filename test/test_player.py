import pytest
from lib.player import *
from lib.deck import *
from lib.card import *


def test_it_exists():
    card1 = Card("diamond", "Queen", 12)
    card2 = Card("spade", "3", 3)
    card3 = Card("Heart", "Ace", 14)
    cards = [card1, card2, card3]

    deck = Deck(cards)
    player = Player('Calvin', deck)

    assert player.name == 'Calvin'
    assert len(player.deck.cards) == 3


def test_knows_if_player_lost():
    card1 = Card("diamond", "Queen", 12)
    card2 = Card("spade", "3", 3)
    card3 = Card("Heart", "Ace", 14)
    cards = [card1, card2, card3]

    deck = Deck(cards)
    player = Player('Calvin', deck)

    assert not player.has_lost()

    player.deck.remove_card()
    player.deck.remove_card()

    assert not player.has_lost()

    player.deck.remove_card()
    assert player.has_lost()