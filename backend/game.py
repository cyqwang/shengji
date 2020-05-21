from cards import *
from players import * 

class Game:

	def __init__(self, numPlayers, high = "A", trumpSuit = None, trumpValue = None, jokers = True):
		self.numPlayers = numPlayers
		self.deck = Deck(jokers)
		self.table = Table(numPlayers)
		self.ordering = {}
		self.orderCards(high, trumpSuit, trumpValue)

	def orderCards(self, high, trumpSuit, trumpValue):

		#set up value Order; should set up error message?
		valueOrder = {"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13,"Little":32,"Big":33}
		if high == "K":
			valueOrder["A"] = 1
			valueOrder["2"] = 2
		if high == "A":
			valueOrder["A"] = 14
			valueOrder["2"] = 2
		if high == "2":
			valueOrder["A"] = 14
			valueOrder["2"] = 15

		#set up suit order; should set up error message?
		suitOrder = {"C":0,"D":0,"S":0,"H":0,"J":2}
		if trumpSuit is not None and trumpSuit in ["C","D","S","H"]:
			suitOrder[trumpSuit] = 1

		for card in self.deck.deck:
			if card.value == trumpValue:
				trumpValueBonus = 32
			else:
				trumpValueBonus = 0
			self.ordering[card] = valueOrder[card.value] + 16 * suitOrder[card.suit] + trumpValueBonus

		return

	def deal(self):
		pass
