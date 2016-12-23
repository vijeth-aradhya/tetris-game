import pytest
import sys
import os

package_dir = os.path.dirname(os.path.abspath(__file__))
package_dir = package_dir[:-5]
package_dir += 'src'
sys.path.append(package_dir)

from TetrisFunctionality import Gameplay
from Block import Block

game = Gameplay()

def setBoard():
	""" A new board instance from Gameplay() class """
	board_inst = game.getBoard()
	for i in xrange(30):
		board_inst[i][0] = ' '
	return board_inst

def test_checkRowFull_1(): # private method changed
	board_inst = setBoard()
	for i in xrange(30):
		board_inst[i][0] = 'X'
	assert game.checkRowFull(0) == 1

def test_checkRowFull_2():
	board_inst = setBoard()
	for i in xrange(20):
		board_inst[i][0] = 'X'
	assert game.checkRowFull(0) == 0

def test_checkRowempty_1(): # private method changed
	board_inst = setBoard()
	for i in xrange(20):
		board_inst[i][0] = 'X'
	assert game.checkRowEmpty(0) == 0

def test_checkRowempty_2():
	board_inst = setBoard()
	for i in xrange(30):
		board_inst[i][0] = ' '
	assert game.checkRowEmpty(0) == 1

def test_gameOver_1():
	block = Block()
	block.piece_number = 1
	game.fillPiecePos(block)
	test_block = Block()
	test_block.piece_number = 0
	assert game.gameOver(test_block) == 1
	game.clearPiecePos(block)

def test_gameOver_2():
	block = Block()
	block.piece_number = 4
	game.fillPiecePos(block)
	test_block = Block()
	test_block.piece_number = 4
	assert game.gameOver(test_block) == 1
	game.clearPiecePos(block)

def test_gameOver_3():
	block = Block()
	block.piece_number = 4
	assert game.gameOver(block) == 0
	game.clearPiecePos(block)

def test_gameOver_4():
	board_inst = setBoard()
	block = Block()
	block.piece_number = 4
	board_inst[12][0] = 'X'
	board_inst[13][1] = 'X'
	board_inst[14][1] = 'X'
	board_inst[15][1] = 'X'
	assert game.gameOver(block) == 1
	game.clearPiecePos(block)

def test_selectPiece():
	assert (game.selectPiece() >=0 and game.selectPiece() <= 5) == 1

def test_gameTime_1():
	assert game.gameTime(3) == 100

def test_gameTime_2():
	assert game.gameTime(4) == 1000

def test_updateScore_1():
	""" Added 110 to score """
	board_inst = setBoard()
	for i in xrange(30):
		board_inst[i][29] = 'X'
	game.updateScore(29)
	assert game.score == 100
	game.score = -10

def test_updateScore_2():
	""" Added 10 to score """
	board_inst = setBoard()
	game.updateScore(29)
	assert game.score == 0
	game.score = -10

def test_updateScore_3():
	""" Added 110 to score """
	board_inst = setBoard()
	for i in xrange(30):
		board_inst[i][25] = 'X'
	game.updateScore(23)
	assert game.score == 100
	game.score = -10

def test_updateScore_4():
	""" Added 210 to score """
	board_inst = setBoard()
	for i in xrange(30):
		board_inst[i][25] = 'X'
		board_inst[i][26] = 'X'
	game.updateScore(23)
	assert game.score == 200
	game.score = -10