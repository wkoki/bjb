# -*-coding:utf-8-*- #
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/./src')

#---------- Board Class ----------#
class Board(object):
    def __init__(self):
        self.turn = 0
        self.ball_list = {
            1:True, 2:True, 3:True,
            4:True, 5:True, 6:True,
            7:True, 8:True, 9:True,
            10:True, 11:True, 12:True,
            13:True, 14:True, 15:True, }

    def drop(self, ball):
        self.ball_list[int(ball)] == False



    # 全プレイヤーの得点版を表示
    def show(self, player_list):
        print("===================================")
        print("NAME\tFALLS\tTOTAL\tTO21\tREACHES")
        for i in range(len(player_list)):
            print(player_list[i].name + "\t" + str(player_list[i].myfalls) + "\t" + str(player_list[i].total) + "\t" + str(21 - player_list[i].total) + "\t" + str(player_list[i].reaches))
        print("===================================")

