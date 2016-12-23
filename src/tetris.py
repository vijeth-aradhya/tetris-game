import sys
import time
from TetrisFunctionality import *

def main(args):
	end = 0
#### Initialising
	game = Gameplay()
#### Variable 'end' will decide if the script has to be ended or not
	while end == 0:
		curses.curs_set(0)
		stdscr = curses.initscr()
 		curses.noecho()
		curses.cbreak()
		y, x = stdscr.getmaxyx()
		stdscr.nodelay(1)
		stdscr.keypad(1)
		var = 1
		levels = 0
		game.write(var, stdscr, levels)
		game.createMenuBoundary(stdscr)
#### Menu Screen Loop
		while True:
			user = stdscr.getch()
			if user == 115:
				if var<3 and levels == 0:
					var += 1
				if levels>=1 and levels<5:
					levels += 1
				game.write(var, stdscr, levels)
			elif user == 119:
				if var>1 and levels == 0:
					var += -1
				if levels>1 and levels<=5:
					levels += -1
				game.write(var, stdscr, levels)
			elif user == 10:
				end = game.action(var, levels)
				if end == 2:
					levels = 1
				elif end == 3:
					levels = 0
				else:
					if levels == 0:
						levels = 1
					break
				game.write(var, stdscr, levels)
#### End of Menu Screen Loop
		if end == 1:
			break
#### Initialise Game
		newblock = Block()
		nextblock = Block()
		game.setBoard()
		newblock.piece_number = game.selectPiece()
		nextblock.piece_number = game.selectPiece()
		game.createBoard(stdscr, levels, game.totalscore)
		stdscr.addstr(17, 45, (game.updateScore(newblock.pos['y'])))
#### Game Loop
		while True:
			user=stdscr.getch()
			if user == 97:
				game.moveLeft(newblock)
			elif user == 100:
				game.moveRight(newblock)
			elif user == 115:
				game.rotate(newblock)
			elif user == 32:
				game.moveFullDown(newblock)
				stdscr.addstr(17, 45, (game.updateScore(newblock.pos['y'])))
				del newblock
				newblock = nextblock
				newblock.piece_number = nextblock.piece_number
				del nextblock
				nextblock = Block()
				nextblock.piece_number = game.selectPiece()
				if game.gameOver(newblock):
					stdscr.addstr(19, 45, 'Game Over')
					stdscr.refresh()
					time.sleep(2)
					if levels < 4:
						levels += 1
						game.totalscore += game.score
						game.score = 0
						game.createBoard(stdscr, levels, game.totalscore)
					else:
						end = 1
						break
			elif user == 113:
				end=1
				break
			elif user == 109:
				game.clearBoard(stdscr)
				game.score = -10
				game.totalscore = 0
				break
			if game.moveDown(newblock):
				stdscr.addstr(17, 45, (game.updateScore(newblock.pos['y'])))
				del newblock
				newblock = nextblock
				newblock.piece_number = nextblock.piece_number
				del nextblock
				nextblock = Block()
				nextblock.piece_number = game.selectPiece()
				if game.gameOver(newblock):
					stdscr.addstr(19, 45, 'Game Over')
					stdscr.refresh()
					time.sleep(2)
					if levels < 4:
						levels += 1
						game.totalscore += game.score
						game.score = -10
						game.createBoard(stdscr, levels, game.totalscore)
					else:
						game.clearBoard(stdscr)
						break
			if levels == 4:
				game.rotate(newblock)
			game.draw(stdscr, nextblock)
			stdscr.timeout(game.gameTime(levels))
#### End of Game Loop
		curses.endwin()

def windResize():
	""" Resizing the window """
	sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=35, cols=80))

windResize()
curses.wrapper(main)