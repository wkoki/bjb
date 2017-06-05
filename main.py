# -*-coding:utf-8-*- #
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/./src')

from Game import *

#---------- Main Routine ----------#
game = Game()

game.start()
