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

class Standart_deck(Card_group):
	def __init__(self):
		self.cards = []
		
		for s in ["♣", "♦", "♥", "♠"]:
			for v in range(2,15):
				self.cards.append(Card(v, s))

class Player(Card_group):
	def __init__(self):
		self.cards = []		

player_1 = Player()
player_2 = Player()


deck = Standart_deck()
deck.shuffle()
player_1.cards = deck.cards[:26]
player_2.cards = deck.cards[26:]


print("Для следующего хода нажимайте Enter")
sign = ""
while player_1.hasCard() and player_2.hasCard():
	card1 = player_1.nextCard()
	card2 = player_2.nextCard() 

	if card1.value == card2.value:
		sign = "="

	elif card1.value > card2.value:
		player_1.cards.extend([card1,card2])
		sign = ">"
	elif card2.value > card1.value:
		player_2.cards.extend([card2,card1])
		sign = "<"
	print("игрок1 -",card1, sign ,card2,"- игрок_2")
	print(f"Количество карт : игрок1 - {player_1.size()}, игрок2 - {player_2.size()}")
	input()
print("Игра закончена.")






	

