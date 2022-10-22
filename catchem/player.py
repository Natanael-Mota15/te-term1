import random
from turtle import position




class Player:
    def __init__(self, left, right):
        
    
        self.left = left
        self.right = right
        self.position = random.randint(left, right)
        

    def move_right(self):
        if position < self.right:
            self.position=self.position+1

    def move_left(self):
        if position > self.left:
            self.position=self.position-1

    def display(self):
        y=7
        x=self.position%8


    def __init__(self,limit_l, limit_r):
        self.limit_r = limit_r
        self.limit_l = limit_l
        self.position = random.randint(limit_l, limit_r)