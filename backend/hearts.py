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
		self.scoreBoard = {}
		self.totalScores = {}

	def sitAtTable(self, name):
		if len(self.players) < self.tableLimit:
			player = HeartsPlayer(name,len(self.players))
			self.players.append(player)
			self.scoreBoard[player] = []
			self.totalScores[player] = 0
		else:
			print("Table is Full: Cannot add", name, "to table.")

	def printScores(self):
		pass

class Hearts(Game):

	def __init__(self):
		Game.__init__(self, 4, trumpSuit = "H", jokers = False)
		self.table = HeartsTable()
		self.inPlay = True #overall game
		self.deck.shuffle()
		self.heartsBroken = False
		self.currentSuit = "C"

	def startGame(self, player1, player2, player3, player4):
		print("Beginning a game of hearts...")
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

	def resetCards(self):
		self.deck = Deck(Jokers)
		self.deck.shuffle()
		self.heartsBroken = False
		self.currentSuit = "C"
		for player in self.table.players:
			player.hand = {"C":[], "D":[], "S":[], "H":[]}
			player.wonCards = []

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

	def playTrick(self):
		trickWinner = None
		pot = []
		trick = {}
		for i in range(4):
			player = self.table.players[(self.table.dealer.position + i) % 4]
			played_card = player.playCard()
			pot.append(played_card)
			trick[played_card] = player
			print(player.name, "played", played_card)
		trickWinner = self.compareTrick(trick)
		print(trickWinner.name, "won the trick!")
		trickWinner.winCards(pot)
		self.table.dealer = trickWinner
		self.currentSuit = None

	def showAllCards(self):
		for player in self.table.players:
			print(player.name)
			player.showHand()

	def calculatePoints(self):
		moonshot = None
		#first runthrough
		for player in self.table.players:
			points = player.calculatePoints()
			if points == 26:
				moonshot = player				
				self.table.scoreBoard[player].append(0)
			else:
				self.table.scoreBoard[player].append(points)
				self.table.totalScores[player] += points

		#adjust for moonshot and check if game is over
		for player in self.table.players:
			if moonshot is not None and player is not moonshot:
				self.table.scoreboard[player].pop()
				self.table.scoreBoard[player].append(26)
				self.table.totalScores[player] += 26
			if self.table.totalScores[player] > 100:
				self.inPlay = False

	def showCurrentPoints(self):
		self.table.printScores()

	def playRound(self):
		#reset cards
		self.resetCards()
		print("Dealing cards...")
		self.deal()
		print(self.table.dealer.name, "goes first.")

		#play 13 tricks
		for i in range(13):
			self.playTrick()

		#calculate scores
		self.calculatePoints()
		self.showCurrentPoints()

	def playGame(self):
		roundNum = 1
		while self.inPlay:
			print("Starting Round", roundNum)
			self.playRound()
			roundNum +=1
		print("Game Over!")
		print(max(self.table.totalScores, key=self.table.totalScores.get).name, "has lost.")



hearts = Hearts()
hearts.startGame("crystal","elina","violeta","blossom")
hearts.showAllCards()