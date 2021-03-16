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


def test_knows_basic_turn_type():
    card1 = Card("diamond", "Queen", 12)
    card2 = Card("spade", "3", 3)
    card3 = Card("Heart", "Ace", 14)
    card4 = Card("spade", "7", 7)
    cards1 = [card1, card2]
    cards2 = [card3, card4]

    deck1 = Deck(cards1)
    deck2 = Deck(cards2)
    player1 = Player('Calvin', deck1)
    player2 = Player('Hobbes', deck2)
    turn = Turn(player1, player2)

    assert turn.type() == "basic"

def test_knows_war_turn_type():
    card1 = Card("diamond", "Queen", 12)
    card2 = Card("spade", "3", 3)
    card3 = Card("Heart", "Queen", 12)
    card4 = Card("spade", "7", 7)
    cards1 = [card1, card2]
    cards2 = [card3, card4]

    deck1 = Deck(cards1)
    deck2 = Deck(cards2)
    player1 = Player('Calvin', deck1)
    player2 = Player('Hobbes', deck2)
    turn = Turn(player1, player2)

    assert turn.type() == "war"

def test_knows_MAD_turn_type():
    card1 = Card("diamond", "Queen", 12)
    card2 = Card("spade", "3", 3)
    card3 = Card("Heart", "Queen", 12)
    card4 = Card("Heart", "3", 3)
    cards1 = [card1, card2]
    cards2 = [card3, card4]

    deck1 = Deck(cards1)
    deck2 = Deck(cards2)
    player1 = Player('Calvin', deck1)
    player2 = Player('Hobbes', deck2)
    turn = Turn(player1, player2)

    assert turn.type() == "MAD"

def test_knows_winner_of_basic_turn():
    card1 = Card("diamond", "Queen", 12)
    card2 = Card("spade", "3", 3)
    card3 = Card("Heart", "Ace", 14)
    card4 = Card("spade", "7", 7)
    cards1 = [card1, card2]
    cards2 = [card3, card4]

    deck1 = Deck(cards1)
    deck2 = Deck(cards2)
    player1 = Player('Calvin', deck1)
    player2 = Player('Hobbes', deck2)
    turn = Turn(player1, player2)

    assert turn.type() == "basic"
    assert turn.winner() == player2

def test_knows_winner_of_war_turn():
    card1 = Card("diamond", "Queen", 12)
    card2 = Card("spade", "3", 3)
    card3 = Card("Heart", "Queen", 12)
    card4 = Card("spade", "7", 7)
    cards1 = [card1, card2]
    cards2 = [card3, card4]

    deck1 = Deck(cards1)
    deck2 = Deck(cards2)
    player1 = Player('Calvin', deck1)
    player2 = Player('Hobbes', deck2)
    turn = Turn(player1, player2)

    assert turn.type() == "war"
    assert turn.winner() == player2