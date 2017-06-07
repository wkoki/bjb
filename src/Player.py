# -*-coding:utf-8-*- #
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/./src')

from Board import *

#---------- Player Class ----------#
class Player(object):
    def __init__(self, i):
        self.name = raw_input(str(i+1) + "番目のプレイヤー名：")
        self.order = i+1
        self.myfalls = []
        self.total = 0
        self.over = False
        self.reaches = []
        self.finished_turn = 0

    # 2個以内で上がることのできる手を表示
    def reach(self, board):

        for k1, v1 in board.ball_list.items():
            if v1 == True:
                if k1 + self.total == 21:
                    self.reaches.append(k1)

                for k2, v2 in board.ball_list.items():
                       if v2 == True:
                           if k1 + k2 + self.total == 21 and k1 < k2:
                               self.reaches.append([k1, k2])

    def drop(self, board, ball):
        board.ball_list[int(ball)] = False
        self.myfalls.append(ball)
        self.total += int(ball)
        self.reach(board)
        if self.total == 21:
            self.over = True
            self.finished_turn = board.turn
