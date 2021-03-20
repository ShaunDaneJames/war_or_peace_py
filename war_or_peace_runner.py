from lib.turn import *
from lib.player import *
from lib.deck import *
from lib.card import *
from lib.game import *


suits = ['Heart', 'Diamond', 'Club', 'Spade']
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
rank = 2
cards = []

for s in suits:
    for v in values:
        cards.append(Card(s, v, rank))
        rank += 1
    rank = 2

deck = Deck(cards)
random.shuffle(deck.cards)
player1_deck = Deck(cards[0:25])
player2_deck = Deck(cards[26:52])

decision = input(
    'Welcome to War! (or Peace) This game will be played with 52 cards.\n'
    'The players today are Calvin and Hobbes.\n'
    'Type \'GO\' to start the game!\n'
    '------------------------------------------------------------------\n')

if decision.upper() == "GO":
    calvin = Player('Calvin', player1_deck)
    hobbes = Player('Hobbes', player2_deck)

    turn = Turn(calvin, hobbes)
    game = Game(calvin, hobbes, turn)
    game.start()
    print("yay")
else:
    print('Thanks for playing!')