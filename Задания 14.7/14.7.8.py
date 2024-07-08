from random import shuffle

class Card:
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit

	def __str__(self):
		names = ["Jack", "Queen", "King", "Ace"]
		if self.value <= 10:
			return f"{self.value} {self.suit}"
		else:
			return f"{names[self.value-11]} {self.suit}"
		
class Card_group:
	def __init__(self,cards):
		self.cards = cards
	def nextCard(self):
		return self.cards.pop(0)

	def shuffle(self):
		shuffle(self.cards)

	def hasCard(self):
		return len(self.cards) > 0

	def size(self):
		return len(self.cards)

class Deck_two_suits(Card_group):
	def __init__(self):
		self.cards = []
		for s in ["♥", "♠"]:
			for v in range(2,10):
				self.cards.append(Card(v,s))

	def next2(self):
		return f"{self.cards[0]} {self.cards[1]}"

deck = Deck_two_suits()
deck.shuffle()
print(deck.next2())