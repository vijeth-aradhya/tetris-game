import pytest
import sys
import os

package_dir = os.path.dirname(os.path.abspath(__file__))
package_dir = package_dir[:-5]
package_dir += 'src'
sys.path.append(package_dir)

from Menu import Menu

menu = Menu()

def test_action_1():
	assert menu.action(1, 0) == 0

def test_action_2():
	assert menu.action(3, 0) == 1

def test_action_3():
	assert menu.action(3, 1) == 1

def test_action_3():
	assert menu.action(2, 5) == 3

def test_action_4():
	assert menu.action(2, 0) == 2

def test_action_5():
	assert menu.action(2, 1) == 0