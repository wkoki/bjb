# -*-coding:utf-8-*- #
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/./src')

#---------- Board Class ----------#
class Board(object):
    def __init__(self):
        self.blist = {
            1:True, 2:True, 3:True,
            4:True, 5:True, 6:True,
            7:True, 8:True, 9:True,
            10:True, 11:True, 12:True,
            13:True, 14:True, 15:True, }
