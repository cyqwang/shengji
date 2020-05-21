from cards import *
from players import * 
from game import *
import time

class WarPlayer(Player):
	def __init__(self, name, position):
		Player.__init__(self, name, position, False)
		self.wonCards = []

	def removeTopCard(self):
		if len(self.hand) > 0:
			return self.hand.pop()
		elif len(self.wonCards) > 0:
			self.shuffle()
			self.hand = self.wonCards
			self.wonCards = []
			return self.hand.pop()
		else:
			return None

	def winCards(self, cards):
		self.wonCards.extend(cards)

	def shuffle(self):
		for i in range(len(self.wonCards)-1, 0, -1):
			r = random.randint(0,i)
			self.wonCards[i], self.wonCards[r] = self.wonCards[r], self.wonCards[i]

	def numCards(self):
		return len(self.hand) + len(self.wonCards)

	def war(self):
		if len(self.hand) < 4:
			self.shuffle()
			self.hand = self.wonCards + self.hand
			self.wonCards = []
		hiddenCards = []
		for i in range(3):
			hiddenCards.append(self.removeTopCard())
		return hiddenCards


class War2PTable(Table):
	def __init__(self):
		Table.__init__(self,2)

	def sitAtTable(self, name):
		if len(self.players) < self.tableLimit:
			self.players.append(WarPlayer(name,len(self.players)))
		else:
			print("Table is Full: Cannot add", name, "to table.")

class War2P(Game):

	def __init__(self):
		Game.__init__(self,2)
		self.table = War2PTable()
		self.inPlay = True
		self.deck.shuffle()

	def startGame(self, player1, player2):
		print("Beginning a game of war...")
		self.table.sitAtTable(player1)
		print("Player 1", player1, "seated.")
		self.table.sitAtTable(player2)
		print("Player 2", player2, "seated.")
		print("Dealing cards...")
		self.deal()

	def deal(self):
		while self.deck.numCards() >= self.numPlayers:
			for player in self.table.players:
				player.draw(self.deck)

	def currentScore(self):
		for player in self.table.players:
			print(player.name, player.numCards())

	def compareTrick(self, trick):
		bestCards = []
		bestValue = 0
		for card in trick:
			if self.ordering[card] > bestValue:
				bestCards = [card]
				bestValue = self.ordering[card]
			elif self.ordering[card] == bestValue:
				bestCards.append(card)
		if len(bestCards) == 1:
			return trick[bestCards[0]]
		else:
			return None

	def playRound(self):
		trickWinner = None
		pot = []
		trick = {}
		while trickWinner == None:
			for player in self.table.players:
				if player.numCards() == 0:
					self.inPlay = False
					print("The game has ended.")
					print(player.name, "has lost.")
					return
				played_card = player.removeTopCard()
				pot.append(played_card)
				trick[played_card] = player
				print(player.name, "played", played_card)
			trickWinner = self.compareTrick(trick)
			if trickWinner == None:
				print("War!")
				trick = {}
				for player in self.table.players:
					pot.extend(player.war())
		print(trickWinner.name, "won the trick!")
		trickWinner.winCards(pot)		
		self.currentScore()

war = War2P()
war.startGame("crystal","elina")
war.currentScore()
while war.inPlay == True:
	war.playRound()