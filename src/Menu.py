""" Menu module defines the menu and it's functions """

import curses

class Menu():
	""" Describes the setting up and working of initial menu """

	def __init__(self):
		self.__x = 27
		self.__y = 12

	def write(self, var, stdscr, levels):
		""" write method to make the menu after each user click ('w' or 's') """
		if var == 1:
			stdscr.addstr((self.__y), (self.__x), "       ")
			stdscr.addstr((self.__y), (self.__x), "PLAY", curses.A_STANDOUT)
			stdscr.addstr((self.__y+2), (self.__x-3), "                                        ")
			stdscr.addstr((self.__y+2), (self.__x), "LEVELS")
			stdscr.addstr((self.__y+4), (self.__x), "       ")
			stdscr.addstr((self.__y+4), (self.__x), "QUIT")
			stdscr.addstr((self.__y+6), (self.__x-3), "                 ")
			stdscr.addstr((self.__y+8), (self.__x), "       ")
			stdscr.addstr((self.__y+10), (self.__x-3), "                         ")
			stdscr.addstr((self.__y+12), (self.__x), "       ")
			stdscr.addstr((self.__y+14), (self.__x-3), "                      ")
			stdscr.addstr((self.__y+16), (self.__x), "    ")
		elif var == 2:
			if levels == 0:
				stdscr.addstr((self.__y), (self.__x), "       ")
				stdscr.addstr((self.__y), (self.__x), "PLAY")
				stdscr.addstr((self.__y+2), (self.__x-3), "                                        ")
				stdscr.addstr((self.__y+2), (self.__x), "LEVELS", curses.A_STANDOUT)
				stdscr.addstr((self.__y+4), (self.__x), "       ")
				stdscr.addstr((self.__y+4), (self.__x), "QUIT")
				stdscr.addstr((self.__y+6), (self.__x-3), "                 ")
				stdscr.addstr((self.__y+8), (self.__x), "       ")
				stdscr.addstr((self.__y+10), (self.__x-3), "                         ")
				stdscr.addstr((self.__y+12), (self.__x), "       ")
				stdscr.addstr((self.__y+14), (self.__x-3), "                      ")
				stdscr.addstr((self.__y+16), (self.__x), "    ")
			elif levels == 1:
				stdscr.addstr((self.__y), (self.__x), "LEVEL 1", curses.A_STANDOUT)
				stdscr.addstr((self.__y+2), (self.__x-3), "Easy level, you'll get used to the game!")
				stdscr.addstr((self.__y+4), (self.__x), "LEVEL 2")
				stdscr.addstr((self.__y+6), (self.__x-3), "Walls all around!")
				stdscr.addstr((self.__y+8), (self.__x), "LEVEL 3")
				stdscr.addstr((self.__y+10), (self.__x-3), "Harder, Better, Stronger!")
				stdscr.addstr((self.__y+12), (self.__x), "LEVEL 4")
				stdscr.addstr((self.__y+14), (self.__x-3), "Immersion in rotation!")
				stdscr.addstr((self.__y+16), (self.__x), "BACK")
			elif levels == 2:
				stdscr.addstr((self.__y), (self.__x), "LEVEL 1")
				stdscr.addstr((self.__y+2), (self.__x-3), "Easy level, you'll get used to the game!")
				stdscr.addstr((self.__y+4), (self.__x), "LEVEL 2", curses.A_STANDOUT)
				stdscr.addstr((self.__y+6), (self.__x-3), "Walls all around!")
				stdscr.addstr((self.__y+8), (self.__x), "LEVEL 3")
				stdscr.addstr((self.__y+10), (self.__x-3), "Harder, Better, Stronger!")
				stdscr.addstr((self.__y+12), (self.__x), "LEVEL 4")
				stdscr.addstr((self.__y+14), (self.__x-3), "Immersion in rotation!")
				stdscr.addstr((self.__y+16), (self.__x), "BACK")
			elif levels == 3:
				stdscr.addstr((self.__y), (self.__x), "LEVEL 1")
				stdscr.addstr((self.__y+2), (self.__x-3), "Easy level, you'll get used to the game!")
				stdscr.addstr((self.__y+4), (self.__x), "LEVEL 2")
				stdscr.addstr((self.__y+6), (self.__x-3), "Walls all around!")
				stdscr.addstr((self.__y+8), (self.__x), "LEVEL 3", curses.A_STANDOUT)
				stdscr.addstr((self.__y+10), (self.__x-3), "Harder, Better, Stronger!")
				stdscr.addstr((self.__y+12), (self.__x), "LEVEL 4")
				stdscr.addstr((self.__y+14), (self.__x-3), "Immersion in rotation!")
				stdscr.addstr((self.__y+16), (self.__x), "BACK")
			elif levels == 4:
				stdscr.addstr((self.__y), (self.__x), "LEVEL 1")
				stdscr.addstr((self.__y+2), (self.__x-3), "Easy level, you'll get used to the game!")
				stdscr.addstr((self.__y+4), (self.__x), "LEVEL 2")
				stdscr.addstr((self.__y+6), (self.__x-3), "Walls all around!")
				stdscr.addstr((self.__y+8), (self.__x), "LEVEL 3")
				stdscr.addstr((self.__y+10), (self.__x-3), "Harder, Better, Stronger!")
				stdscr.addstr((self.__y+12), (self.__x), "LEVEL 4", curses.A_STANDOUT)
				stdscr.addstr((self.__y+14), (self.__x-3), "Immersion in rotation!")
				stdscr.addstr((self.__y+16), (self.__x), "BACK")
			elif levels == 5:
				stdscr.addstr((self.__y), (self.__x), "LEVEL 1")
				stdscr.addstr((self.__y+2), (self.__x-3), "Easy level, you'll get used to the game!")
				stdscr.addstr((self.__y+4), (self.__x), "LEVEL 2")
				stdscr.addstr((self.__y+6), (self.__x-3), "Walls all around!")
				stdscr.addstr((self.__y+8), (self.__x), "LEVEL 3")
				stdscr.addstr((self.__y+10), (self.__x-3), "Harder, Better, Stronger!")
				stdscr.addstr((self.__y+12), (self.__x), "LEVEL 4")
				stdscr.addstr((self.__y+14), (self.__x-3), "Immersion in rotation!")
				stdscr.addstr((self.__y+16), (self.__x), "BACK", curses.A_STANDOUT)
		elif var == 3:
			stdscr.addstr((self.__y), (self.__x), "       ")
			stdscr.addstr((self.__y), (self.__x), "PLAY")
			stdscr.addstr((self.__y+2), (self.__x-3), "                                        ")
			stdscr.addstr((self.__y+2), (self.__x), "LEVELS")
			stdscr.addstr((self.__y+4), (self.__x), "       ")
			stdscr.addstr((self.__y+4), (self.__x), "QUIT", curses.A_STANDOUT)
			stdscr.addstr((self.__y+6), (self.__x-3), "                 ")
			stdscr.addstr((self.__y+8), (self.__x), "       ")
			stdscr.addstr((self.__y+10), (self.__x-3), "                         ")
			stdscr.addstr((self.__y+12), (self.__x), "       ")
			stdscr.addstr((self.__y+14), (self.__x-3), "                      ")
			stdscr.addstr((self.__y+16), (self.__x), "    ")

	def action(self, var, levels):
		""" action of menu user presses Enter; required to proceed further """
		if var == 1 and levels == 0:
			return 0
		elif var == 3:
			return 1
		elif var == 2 and levels == 0:
			return 2
		elif var == 2 and levels == 5:
			return 3
		else:
			return 0

	def createMenuBoundary(self, stdscr):
		""" creates a bigger boundary for menu display """
		for i in xrange(71):
			stdscr.addstr(1, i, "-")
			stdscr.addstr(34, i, "-")
		for i in xrange(1, 35):
			stdscr.addstr(i, 0, "|")
			stdscr.addstr(i, 71	, "|")
		stdscr.addstr(0, 27, "TETRIS by Vijeth Aradhya")
		stdscr.addstr(2, 29, "'w' to go up")
		stdscr.addstr(4, 29, "'s' to come down")