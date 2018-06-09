class ChessPiece(object):
	def __init__(self, x, y, name):
	    self.x = x
	    self.y = y
	    self.name = name

	def move(self, x, y):
	    self.x = x
	    self.y = y

	def printData():
	    print("Name of Piece is: " + self.name + "and coordinates are: " + x + ", " + y)

