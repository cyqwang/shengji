class Player:
	def __init__(self, name, position, handVisible = True):
		self.name = name
		self.position = position
		self.hand = []
		self.handVisible = handVisible
		self.wonCards = []

	def draw(self, deck):
		self.hand.append(deck.drawCard())

	def winCards(self, cards):
		self.wonCards.extend(cards)

	def showHand(self):
		if self.handVisible:
			for card in self.hand:
	 			print(str(card), end=" ")
			print("\n")
		else:
			print("You cannot look at your hand.")


class Table:
	def __init__(self, tableLimit):
		self.players = []
		self.tableLimit = tableLimit

	def sitAtTable(self, name):
		if len(self.players) < self.tableLimit:
			self.players.append(Player(name,len(self.players)))
		else:
			print("Table is Full: Cannot add", name, "to table.")

	def showTable(self):
		for player in self.players:
			print(player.name)

