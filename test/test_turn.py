import pytest
from lib.turn import *
from lib.player import *
from lib.deck import *
from lib.card import *


def test_it_exists():
    card1 = Card("diamond", "Queen", 12)
    card2 = Card("spade", "3", 3)
    card3 = Card("Heart", "Ace", 14)
    cards = [card1, card2, card3]

    deck = Deck(cards)
    player1 = Player('Calvin', deck)
    player2 = Player('Hobbes', deck)
    turn = Turn(player1, player2)

    assert turn.player1.name == 'Calvin'
    assert turn.player2.name == 'Hobbes'
    assert turn.spoils == []