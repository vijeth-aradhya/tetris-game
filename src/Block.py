""" Block module defines a block and it's possible movements """

from Board import *

class Block(Board): 
	"""defining Board as the Parent Class of Block (since each block obj corresponds to a board)"""
	def __init__(self):
		Board.__init__(self)
		self.pieces = [[[' ', ' ', ' ', ' '],
						['X', 'X', 'X', 'X'],
						[' ', ' ', ' ', ' '],
						[' ', ' ', ' ', ' ']],
						[[' ', 'X', ' ', ' '],
						[' ', 'X', ' ', ' '],
						[' ', 'X', ' ', ' '],
						[' ', 'X', ' ', ' ']],
						[[' ', ' ', ' ', ' '],
						[' ', ' ', ' ', ' '],
						['X', 'X', 'X', ' '],
						['X', ' ', ' ', ' ']],
						[[' ', ' ', ' ', ' '],
						[' ', 'X', 'X', ' '],
						[' ', 'X', 'X', ' '],
						[' ', ' ', ' ', ' ']],
						[[' ', ' ', ' ', ' '],
						[' ', ' ', 'X', ' '],
						[' ', 'X', 'X', ' '],
						[' ', 'X', ' ', ' ']],
						[[' ', ' ', ' ', ' '],
						[' ', ' ', ' ', ' '],
						[' ', 'X', 'X', 'X'],
						[' ', ' ', 'X', ' ']]]

		self.pos = {'x':12, 'y':0}

		self.piece_number = 0

	def rotate(self, block):
		""" Rotates the given block anti-clockwise """
		self.clearPiecePos(block)
		temporaryInstance = block.pieces[block.piece_number]
		block.pieces[block.piece_number] = (zip(*block.pieces[block.piece_number][::-1]))
		if self.checkPiecePos(block):
			self.fillPiecePos(block)
		else:
			block.pieces[block.piece_number] = temporaryInstance
			self.fillPiecePos(block)
		return

	def moveDown(self, block):
		""" moves the given block down by one unit """
		self.clearPiecePos(block)
		block.pos['y'] += 1
		if self.checkPiecePos(block):
			self.fillPiecePos(block)
			return 0
		else:
			block.pos['y'] += -1
			self.fillPiecePos(block)
			return 1

	def moveFullDown(self, block):
		""" moves the given block to the bottom """
		self.clearPiecePos(block)
		while self.checkPiecePos(block):
			block.pos['y'] += 1
		block.pos['y'] += -1
		self.fillPiecePos(block)
		return

	def moveRight(self, block):
		""" moves the given block to the right """
		self.clearPiecePos(block)
		block.pos['x'] += 1
		if self.checkPiecePos(block):
			self.fillPiecePos(block)
		else:
			block.pos['x'] += -1
			self.fillPiecePos(block)

	def moveLeft(self, block):
		""" moves the given block to the left """
		self.clearPiecePos(block)
		block.pos['x'] += -1
		if self.checkPiecePos(block):
			self.fillPiecePos(block)
		else:
			block.pos['x'] += 1
			self.fillPiecePos(block)
