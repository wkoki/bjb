# -*-coding:utf-8-*- #
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/./src')


from Player import *
from Board import *

#---------- Game Class ----------#
class Game (object):
    def __init__(self):
        self.np = 0
        self.plist = []

    def start(self):
        self.setting()
        self.playing()

    def setting(self):
        self.np = int(input("プレイヤーの人数："))

        for i in range(self.np):
            self.plist.append(Player(i))


    def playing(self):
        print("-------------------------")
        print("ゲーム開始！")
        print("-------------------------")

        board = Board()

        while(True):
            for i in range(self.np):

                # ショット中のプレイヤーをplayerに格納
                player = self.plist[i]

                # playerが既にプレイ終了していないかの確認
                if not(player.over):
                    print(str(player.order) + "：" + player.name + "の番です。")

                    while not(player.over):
                        print("(自首の場合は0、何も落ちなければEnter)")
                        fall = raw_input("落ちたボール：")

                        # 何も落ちなければエンターキーで終了
                        if fall == '':
                            break
                        elif fall == '0':
                            player.over = True
                        else:
                            fall = int(fall)
                            board.blist[fall] = False
                            player.myfalls.append(fall)
                            player.total += int(fall)
                            player.judge()

                    # playerのショットが終わったので得点版を表示
                    print("===================================")
                    print("name\tfalls\ttotal\tto21")
                    for j in range(self.np):
                        print(self.plist[j].name + "\t" + str(self.plist[j].myfalls) + "\t" + str(self.plist[j].total) + "\t" + str(self.plist[j].reach()))
                    print("===================================")


