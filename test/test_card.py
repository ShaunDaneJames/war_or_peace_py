import pytest
from lib.card import *


def test_it_exists():
    card = Card("diamond", "Queen", 12)
    assert card.suit == "diamond"
    assert card.value == "Queen"
    assert card.rank == 12
