# -*-coding:utf-8-*- #
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/./src')



from Player import *
from Board import *

#---------- Game Class ----------#
class Game (object):
    def __init__(self):
        self.np = 0
        self.player_list = []
        self.turn = 0

    def start(self):
        self.setting()
        self.playing()

    def setting(self):
        self.np = int(input("プレイヤーの人数："))

        for i in range(self.np):
            self.player_list.append(Player(i))


    def playing(self):
        print("-------------------------")
        print("ゲーム開始！")
        print("-------------------------")

        board = Board()

        while(True):
            # ターン数をインクリメンド
            board.turn += 1

            for i in range(self.np):

                # ショット中のプレイヤーをplayerに格納
                player = self.player_list[i]

                # playerが既にプレイ終了していないかの確認
                if not(player.over):

                    while not(player.over):
                        #盤面を表示
                        board.show(self.player_list)

                        # 入力待ち
                        print("No." + str(player.order) + ": " + player.name)
                        print("(自首の場合は0、何も落ちなければEnter)")
                        ball = raw_input("落ちたボール：")

                        # 入力に応じた処理
                        if ball == '':
                            break
                        elif ball == '0':
                            player.over = True
                            player.finished_turn = board.turn
                        else:
                            player.drop(board, ball)

            if self.judge_end():
                self.show_rank()
                quit()


    def judge_end(self):
        for player in self.player_list:
            if player.over == False:
                return False

        return True




    def comp21(self, x, y):
        a = x.total
        b = y.total
        if a == 21 and not(b == 21):
            return -1
        elif not(a == 21) and b == 21:
            return 1
        else:
            return 0

    def compturn(self, x, y):
        a = x.finished_turn
        b = y.finished_turn
        if a < b:
            return -1
        elif a > b:
            return 1
        else:
            return 0

    def compmax(self, x, y):
        a = max(x.myfalls)
        b = max(y.myfalls)
        if a > b:
            return -1
        elif a < b:
            return 1
        else:
            return 0




    def show_rank(self):
        self.player_list.sort(cmp=self.compturn)
        self.player_list.sort(cmp=self.compmax)
        self.player_list.sort(cmp=self.comp21)
        for player in self.player_list:
            print(player.name)
