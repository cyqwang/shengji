class Player:
	def __init__(self, name, position):
		self.name = name
		self.position = position
		self.hand = []

	def draw(self, deck):
		self.hand.append(deck.drawCard())

	def showHand(self):
		for card in self.hand:
 			print(str(card), end=" ")
		print("\n")

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