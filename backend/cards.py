import random

class Card:

	def __init__(self, value, suit):
		self.value = value
		self.suit = suit

	def __str__(self):
		return self.value+self.suit

	def __eq__(self, other):
		return other.value == self.value and other.suit == self.suit

	def __hash__(self):
		return hash((self.value, self.suit))

class Deck:

	def __init__(self, jokers = True):
		self.deck = []
		self.makeDeck(jokers)

	def makeDeck(self, jokers):
		for value in (["2","3","4","5","6","7","8","9","10","J","Q","K","A"]):
			for suit in (["C","D","S","H"]):
				self.deck.append(Card(value, suit))
		if jokers:
			self.deck.append(Card("Big", "J"))
			self.deck.append(Card("Little", "J"))

	def show(self):
		for card in self.deck:
			print(card)

	def numCards(self):
		return len(self.deck)

	def shuffle(self):
		for i in range(len(self.deck)-1, 0, -1):
			r = random.randint(0,i)
			self.deck[i], self.deck[r] = self.deck[r], self.deck[i]

	def drawCard(self):
		return self.deck.pop()

# class setOfCards:

# 	def __init__(self, canView = False, canShuffle = True, canSort = True):
# 		self.cars = []