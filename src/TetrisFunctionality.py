""" This is the main functionality of the game combined with everything """

import random
import curses
from Menu import Menu
from Block import *

class Gameplay(Block, Menu):
	""" Gameplay is the subclass of Block(and Board) """

	def __init__(self):
		self.score = -10
		self.totalscore = 0
		Menu.__init__(self)
		Block.__init__(self)

	def checkRowFull(self, row):
		""" this is to check if a row is full, which is used in updateScore() method """
		for i in xrange(30):
			if board[i][row] != 'X':
				return 0
		return 1

	def checkRowEmpty(self, row):
		""" this is to check if a row is empty """
		for i in xrange(30):
			if board[i][row] == 'X':
				return 0
		return 1

	def updateScore(self, currentPositionY):
		""" this is to update the score of the game """
		self.score += 10
		for i in xrange(-2, 6):
			if (currentPositionY-2+i) < 32 and (currentPositionY-2+i) >= 0:
				if self.checkRowFull(currentPositionY-2+i):
					j = currentPositionY-2+i
					while j > 1:
						for i in xrange(30):
							board[i][j] = board[i][j-1]
						j += -1
					self.score += 100
		return "Score : " + str(self.score)

	def gameOver(self, block):
		""" this is to check if the game is over """
		if self.checkPiecePos(block):
			return 0
		else:
			return 1

	def selectPiece(self):
		""" select the pieces randomly """
		return random.randint(0, 5)

	def gameTime(self, level):
		""" set game time according the level """
		if level == 3:
			return 100
		else:
			return 1000
