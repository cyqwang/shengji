from cards import *
from players import * 
from game import *
import time

class HeartsPlayer(Player):
	def __init__(self, name, position):
		Player.__init__(self, name, position)
		self.handOrder = ["C", "D", "S", "H"]
		self.hand = {"C":[], "D":[], "S":[], "H":[]}

	def draw(self, deck):
		drawnCard = deck.drawCard()
		self.hand[drawnCard.suit].append(drawnCard)

	def sortCards(self, ordering):
		for suit, cards in self.hand.items():
			self.hand[suit] = sorted(cards, key = ordering.get)

	def showHand(self):
		for suit in self.handOrder:
			for card in self.hand[suit]:
				print(str(card), end=" ")
		print("\n")

	def playCard(self, card):
		pass

	def calculatePoints(self):
		points = 0
		for card in self.wonCards:
			if card.suit == "H":
				points += 1
			if card == Card("Q","S"):
			    points += 13
		return points

class HeartsTable(Table):
	def __init__(self):
		Table.__init__(self, 4)
		self.dealer = None

	def sitAtTable(self, name):
		if len(self.players) < self.tableLimit:
			self.players.append(HeartsPlayer(name,len(self.players)))
		else:
			print("Table is Full: Cannot add", name, "to table.")


class Hearts(Game):

	def __init__(self):
		Game.__init__(self, 4, trumpSuit = "H", jokers = False)
		self.table = HeartsTable()
		self.inPlay = True
		self.deck.shuffle()
		self.heartsBroken = False
		self.currentSuit = "C"

	def startGame(self, player1, player2, player3, player4):
		print("Beginning a game of war...")
		self.table.sitAtTable(player1)
		print("Player 1", player1, "seated.")
		self.table.sitAtTable(player2)
		print("Player 2", player2, "seated.")
		self.table.sitAtTable(player3)
		print("Player 3", player3, "seated.")
		self.table.sitAtTable(player4)
		print("Player 4", player4, "seated.")
		print("Dealing cards...")
		self.deal()
		print(self.table.dealer.name, "goes first.")

	def deal(self):
		while self.deck.numCards() >= self.numPlayers:
			for player in self.table.players:
				player.draw(self.deck)
		for player in self.table.players:
			player.sortCards(self.ordering)
			if Card("2","C") in player.hand["C"]:
				self.table.dealer = player

	def compareTrick(self, trick):
		bestCard = None
		for card in trick:
			if card.suit is not self.currentSuit:
				pass
			if self.ordering[card] > self.ordering[bestCard]:
				bestCard = card
		return bestCard

	# def playRound(self):
	# 	trickWinner = None
	# 	pot = []
	# 	trick = {}
	# 	for player in self.table.players:
	# 		if player.numCards() == 0:
	# 			self.inPlay = False
	# 			print("The game has ended.")
	# 			print(player.name, "has lost.")
	# 			return
	# 		played_card = player.removeTopCard()
	# 		pot.append(played_card)
	# 		trick[played_card] = player
	# 		print(player.name, "played", played_card)
	# 	trickWinner = self.compareTrick(trick)
	# 	print(trickWinner.name, "won the trick!")
	# 	trickWinner.winCards(pot)

	def showAllCards(self):
		for player in self.table.players:
			print(player.name)
			player.showHand()


hearts = Hearts()
hearts.startGame("crystal","elina","violeta","blossom")
hearts.showAllCards()