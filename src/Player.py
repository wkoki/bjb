# -*-coding:utf-8-*- #
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/./src')

#---------- Player Class ----------#
class Player(object):
    def __init__(self, i):
        self.name = raw_input(str(i+1) + "番目のプレイヤー名：")
        self.order = i+1
        self.myfalls = []
        self.total = 0
        self.over = False

    def reach(self):
        ans = 21 - self.total
        return ans

    def judge(self):
        if self.total == 21:
            self.over = True
            return True
        else:
            return False
