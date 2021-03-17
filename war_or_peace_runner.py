from lib.turn import *
from lib.player import *
from lib.deck import *
from lib.card import *
from lib.game import *

calvin = Player('Calvin', deck=[])
hobbes = Player('Hobbes', deck=[])

turn = Turn(calvin, hobbes)
suits = ['Heart', 'Diamond', 'Club', 'Spade']
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
rank = 2
cards = []
deck = Deck(cards)

for s in suits:
    for v in values:
        cards.append(Card(s, v, rank))
        rank += 1
    rank = 2


decision = input(
    'Welcome to War! (or Peace) This game will be played with 52 cards.\n'
    'The players today are Calvin and Hobbes.\n'
    'Type \'GO\' to start the game!\n'
    '------------------------------------------------------------------\n')

if decision.upper() == "GO":
    game = Game(calvin, hobbes, deck, turn)
    game.start()
    print("yay")
else:
    print('Thanks for playing!')