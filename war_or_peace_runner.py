import random
from lib.turn import *
from lib.player import *
from lib.deck import *
from lib.card import *

suits = ['Heart', 'Diamond', 'Club', 'Spade']
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
rank = 1
deck = []

for s in suits:
    for v in values:
        deck.append(Card(s, v, rank))
        rank += 1
    rank = 1

random.shuffle(deck)

print(
    'Welcome to War! (or Peace) This game will be played with 52 cards.\n'
    'The players today are Megan and Aurora.\n'
    'Type \'GO\' to start the game!\n'
    '------------------------------------------------------------------')

