""" This module defines the board and all it's functions """

class Board():
	global board

	board = [[' ' for x in range(32)] for y in range(30)]

	def __init__(self):
		self.num = 0

	def draw(self, stdscr, nextblock):
		"""draws the board at each frame/sec (since time is kept at one sec)"""
		for i in xrange(1, 31):
			for j in xrange(2, 34):
				stdscr.addstr(j, i, str(board[i-1][j-2]))
		for i in xrange(49, 53):
			for j in xrange(23, 27):
				stdscr.addstr(j, i, nextblock.pieces[nextblock.piece_number][i-49][j-23])
		stdscr.refresh()
		return

	def clearPiecePos(self, block):
		""" clears the piece/block from it's position on the board """
		for i in xrange(4):
			for j in xrange(4):
				if block.pieces[block.piece_number][i][j] == 'X':
					if (block.pos['x']+i)<30 and (block.pos['y']+j)<32 and (block.pos['x']+i)>=0 and (block.pos['y']+j)>=0:
						board[block.pos['x']+i][block.pos['y']+j] = ' '

	def fillPiecePos(self, block):
		""" fills the piece/block on it's current position on the board """
		for i in xrange(4):
			for j in xrange(4):
				if block.pieces[block.piece_number][i][j] == 'X':
					if (block.pos['x']+i)<30 and (block.pos['y']+j)<32 and (block.pos['x']+i)>=0 and (block.pos['y']+j)>=0:
						board[block.pos['x']+i][block.pos['y']+j] = 'X'
		return

	def checkPiecePos(self, block):
		""" checks if a particular piece/block can be put on the board """
		for i in xrange(4):
			for j in xrange(4):
				if block.pieces[block.piece_number][i][j] == 'X':
					if (block.pos['x']+i)>29 or (block.pos['y']+j)>31 or (block.pos['x']+i)<0 or (block.pos['y']+j)<0:
						return 0
					if board[block.pos['x']+i][block.pos['y']+j] != ' ':
						return 0
		return 1

	def createBoard(self, stdscr, level, totalscore):
		""" this is used to create the Game board/Instructions/Score """
		self.clearBoard(stdscr)
		self.createBoundary(stdscr)
		stdscr.addstr(4, 46, "LEVEL " + str(level))
		stdscr.addstr(7, 40, "Instructions (Press) :")
		stdscr.addstr(8, 40, "'a' to ssmove left")
		stdscr.addstr(9, 40, "'d' to move right")
		stdscr.addstr(10, 40, "'s' to rotate piece anti-clockwise")
		stdscr.addstr(11, 40, "'m' to go to main menu")
		stdscr.addstr(12, 40, "'q' to quit the game")
		stdscr.addstr(13, 40, "Spacebar to let piece freefall")
		stdscr.addstr(15, 45, "Total Score : " + str(totalscore))
		stdscr.addstr(21, 47, "Next Up :")
		for i in xrange(23, 29):
			stdscr.addstr(i, 58, "|")
		for i in xrange(23, 29):
			stdscr.addstr(i, 42, "|")
		for i in xrange(42, 59):
			stdscr.addstr(22, i, "-")
		for i in xrange(42, 59):
			stdscr.addstr(28, i, "-")
		stdscr.refresh()
		stdscr.move(34,0)
		self.changeBoard(level)

	def clearBoard(self, stdscr):
		""" this function clears the whole screen """
		for i in xrange(1, 79):
			for j in xrange(1, 35):
				stdscr.addstr(j, i, " ")

	def changeBoard(self, level):
		""" this PRIVATE method changes the board according to the current level """
		if level == 1:
			for i in xrange(30):
				for j in xrange(32):
					board[i][j] = " "
		else:
			for i in xrange(30):
				for j in xrange(32):
					if j == 15 and i < 10:
						board[i][j] = "O"
					elif j == 23 and i < 25 and i > 15:
						board[i][j] = "O"
					elif j == 28 and i > 25 and i < 30:
						board[i][j] = "O"
					elif j == 7 and i > 20 and i < 27:
						board[i][j] = "O"
					else:
						board[i][j] = " "

	def createBoundary(self, stdscr):
		"""  this creates the game board boundar """
		for i in xrange(31):
			stdscr.addstr(1, i, "-")
			stdscr.addstr(34, i, "-")
		for i in xrange(1, 35):
			stdscr.addstr(i, 0, "|")
			stdscr.addstr(i, 31	, "|")

	def setBoard(self):
		""" sets the board up """
		global board
		board = [[' ' for x in range(32)] for y in range(30)]

	def getBoard(self):
		""" gets the board """
		return board