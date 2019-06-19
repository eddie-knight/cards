import pytest
from deck_builder import deck_builder

def test_init():
    deck = deck_builder()
    assert len(deck.deck) == 52

def test_shuffle():
	deck = deck_builder()
	start = list(deck.list())
	deck.shuffle()
	finish = list(deck.list())
	assert start is not finish

def test_list():
	deck = deck_builder()
	assert deck.list() is deck.deck

def test_draw():
	deck = deck_builder()
	deck.shuffle()
	start = list(deck.list())
	card = deck.draw()
	finish = list(deck.list())
	assert start[0] == card and start[0] is not finish[0]