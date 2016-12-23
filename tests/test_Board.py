import pytest
import sys
import os
import curses

package_dir = os.path.dirname(os.path.abspath(__file__))
package_dir = package_dir[:-5]
package_dir += 'src'
sys.path.append(package_dir)

from Board import Board
from Block import Block

def curses_init():
	sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=35, cols=80))
	stdscr = curses.initscr()
	curses.noecho()
	return stdscr

def test_fillPiecePos():
	block = Block()
	block.piece_number = 0
	board = Board()
	block.piece_number = 0
	board.fillPiecePos(block)
	isFilled = 1
	board_inst = board.getBoard()
	for i in xrange(4):
			for j in xrange(4):
				if(board_inst[block.pos['x']+i][block.pos['y']+j] != block.pieces[0][i][j]):
					isFilled = 0
	assert isFilled == 1

def test_clearPiecePos():
	block = Block()
	block.piece_number = 0
	board = Board()
	board.fillPiecePos(block)
	board.clearPiecePos(block)
	isFilled = 0
	board_inst = board.getBoard()
	for i in xrange(4):
			for j in xrange(4):
				if(board_inst[block.pos['x']+i][block.pos['y']+j] != ' '):
					isFilled = 1
	assert isFilled == 0

def test_checkPiecePos_1():
	block = Block()
	block.piece_number = 0
	board = Board()
	assert board.checkPiecePos(block) == 1

def test_checkPiecePos_2():
	block = Block()
	board = Board()
	block.piece_number = 0
	board_inst = board.getBoard()
	board_inst[12][1] = 'X'
	board_inst[13][2] = 'X'
	board_inst[14][2] = 'X'
	print board.checkPiecePos(block)
	assert board.checkPiecePos(block) == 0

def test_checkPiecePos_3():
	block = Block()
	board = Board()
	block.piece_number = 3
	board.fillPiecePos(block)
	block.piece_number = 0
	assert board.checkPiecePos(block) == 0

def test_changeBoard(): # private method changed
	board = Board()
	board.changeBoard(2)
	board_inst = board.getBoard()
	assert board_inst[4][15] == 'O'
