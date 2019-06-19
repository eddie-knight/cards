# __init__.py

import random

class deck_builder():
	suit = [
			"A", "K", "Q", "J",
			"10", "9", "8",
			"7", "6", "5",
			"4", "3", "2"
			]

	def __init__(self):
		self.deck = []
		self.build()

	def build(self):
		for name in ["H", "S", "D", "C"]:
			for card in self.suit:
				self.deck.append(name + card)

	def list(self):
		return self.deck

	def shuffle(self):
		random.shuffle(self.deck)

	def draw(self):
		return self.deck.pop(0)
