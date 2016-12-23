import pytest
import sys
import os
import time

package_dir = os.path.dirname(os.path.abspath(__file__))
package_dir = package_dir[:-5]
package_dir += 'src'
sys.path.append(package_dir)

from Block import Block

def test_rotate_0():
	new_block = Block()
	new_block.piece_number = 0
	new_block.rotate(new_block)
	new_block.clearPiecePos(new_block)
	assert new_block.pieces[0] == [(' ', ' ', 'X', ' '),
					(' ', ' ', 'X', ' '),
					(' ', ' ', 'X', ' '),
					(' ', ' ', 'X', ' ')]

def test_rotate_1():
	new_block = Block()
	new_block.piece_number = 1
	new_block.rotate(new_block)
	new_block.clearPiecePos(new_block)
	assert new_block.pieces[1] == [(' ', ' ', ' ', ' '),
					('X', 'X', 'X', 'X'),
					(' ', ' ', ' ', ' '),
					(' ', ' ', ' ', ' ')]

def test_rotate_2():
	new_block = Block()
	new_block.piece_number = 2
	new_block.rotate(new_block)
	new_block.clearPiecePos(new_block)
	assert new_block.pieces[2] == [('X', 'X', ' ', ' '),
						(' ', 'X', ' ', ' '),
						(' ', 'X', ' ', ' '),
						(' ', ' ', ' ', ' ')]

def test_rotate_3():
	new_block = Block()
	new_block.piece_number = 3
	new_block.rotate(new_block)
	new_block.clearPiecePos(new_block)
	assert new_block.pieces[3] == [(' ', ' ', ' ', ' '),
						(' ', 'X', 'X', ' '),
						(' ', 'X', 'X', ' '),
						(' ', ' ', ' ', ' ')]

def test_rotate_4():
	new_block = Block()
	new_block.piece_number = 4
	new_block.rotate(new_block)
	new_block.clearPiecePos(new_block)
	assert new_block.pieces[4] == [(' ', ' ', ' ', ' '),
						('X', 'X', ' ', ' '),
						(' ', 'X', 'X', ' '),
						(' ', ' ', ' ', ' ')]

def test_rotate_5():
	new_block = Block()
	new_block.piece_number = 5
	new_block.rotate(new_block)
	new_block.clearPiecePos(new_block)
	print new_block.pieces[5]
	assert new_block.pieces[5] == [(' ', ' ', ' ', ' '),
						(' ', 'X', ' ', ' '),
						('X', 'X', ' ', ' '),
						(' ', 'X', ' ', ' ')]

def test_moveDown_1():
	new_block = Block()
	new_block.piece_number = 5
	prev_y = new_block.pos['y']
	new_block.moveDown(new_block)
	new_block.clearPiecePos(new_block)
	assert (((prev_y+1) == new_block.pos['y']))

def test_moveDown_2():
	new_block = Block()
	new_block.piece_number = 1
	new_block.pos['y'] = 30
	prev_y = new_block.pos['y']
	new_block.moveDown(new_block)
	new_block.clearPiecePos(new_block)
	assert (((prev_y) == new_block.pos['y']))

def test_moveFullDown_1_1():
	new_block = Block()
	new_block.piece_number = 1
	new_block.moveFullDown(new_block)
	new_block.clearPiecePos(new_block)
	assert ((30 == new_block.pos['y']))

def test_moveFullDown_1_2():
	new_block = Block()
	new_block.piece_number = 1
	test_block = Block()
	test_block.piece_number = 4
	test_block.moveFullDown(test_block)
	new_block.moveFullDown(new_block)
	new_block.clearPiecePos(new_block)
	test_block.clearPiecePos(test_block)
	assert ((28 == new_block.pos['y']))

def test_moveFullDown_2_1():
	new_block = Block()
	new_block.piece_number = 0
	new_block.moveFullDown(new_block)
	new_block.clearPiecePos(new_block)
	assert ((28 == new_block.pos['y']))

def test_moveFullDown_2_2():
	new_block = Block()
	new_block.piece_number = 0
	test_block = Block()
	test_block.piece_number = 3
	test_block.moveFullDown(test_block)
	new_block.moveFullDown(new_block)
	new_block.clearPiecePos(new_block)
	test_block.clearPiecePos(test_block)
	assert ((26 == new_block.pos['y']))

def test_moveFullDown_3_1():
	new_block = Block()
	new_block.piece_number = 3
	new_block.moveFullDown(new_block)
	new_block.clearPiecePos(new_block)
	assert ((29 == new_block.pos['y']))

def test_moveFullDown_3_2():
	new_block = Block()
	new_block.piece_number = 3
	test_block = Block()
	test_block.piece_number = 1
	test_block.moveFullDown(test_block)
	new_block.moveFullDown(new_block)
	new_block.clearPiecePos(new_block)
	test_block.clearPiecePos(test_block)
	assert ((28 == new_block.pos['y']))

def test_moveFullDown_4_1():
	new_block = Block()
	new_block.piece_number = 4
	new_block.moveFullDown(new_block)
	new_block.clearPiecePos(new_block)
	assert ((29 == new_block.pos['y']))

def test_moveFullDown_4_2():
	new_block = Block()
	new_block.piece_number = 4
	test_block = Block()
	test_block.piece_number = 5
	test_block.moveFullDown(test_block)
	new_block.moveFullDown(new_block)
	test_block.clearPiecePos(test_block)
	new_block.clearPiecePos(new_block)
	assert ((26 == new_block.pos['y']))

def test_moveFullDown_5_1():
	new_block = Block()
	new_block.piece_number = 5
	new_block.moveFullDown(new_block)
	new_block.clearPiecePos(new_block)
	assert ((28 == new_block.pos['y']))

def test_moveFullDown_5_2():
	new_block = Block()
	new_block.piece_number = 5
	test_block = Block()
	test_block.piece_number = 2
	test_block.moveFullDown(test_block)
	new_block.moveFullDown(new_block)
	new_block.clearPiecePos(new_block)
	test_block.clearPiecePos(test_block)
	assert ((25 == new_block.pos['y']))

def test_moveRight_1_1():
	new_block = Block()
	new_block.piece_number = 1
	prev_x = new_block.pos['x']
	new_block.moveRight(new_block)
	new_block.clearPiecePos(new_block)
	assert ((prev_x+1) == new_block.pos['x'])

def test_moveRight_1_2():
	new_block = Block()
	new_block.piece_number = 1
	new_block.pos['x'] = 30
	new_block.moveRight(new_block)
	new_block.clearPiecePos(new_block)
	assert (30 == new_block.pos['x'])

def test_moveLeft_1_1():
	new_block = Block()
	new_block.piece_number = 1
	prev_x = new_block.pos['x']
	new_block.moveLeft(new_block)
	new_block.clearPiecePos(new_block)
	assert ((prev_x-1) == new_block.pos['x'])

def test_moveLeft_1_2():
	new_block = Block()
	new_block.piece_number = 1
	new_block.pos['x'] = 0
	new_block.moveLeft(new_block)
	new_block.clearPiecePos(new_block)
	assert (0 == new_block.pos['x'])