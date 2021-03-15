import pytest
from lib.player import *

def test_it_exists():
    player = Player('Calvin')

    assert player.name == 'Calvin'