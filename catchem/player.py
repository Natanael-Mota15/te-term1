import random
from turtle import position

from sense_hat import SenseHat
Sense=SenseHat()




class Player:
    def __init__(self, limit_l, limit_r, sense):
        self.limit_r = limit_r
        self.limit_l = limit_l
        self.position = random.randint(limit_l, limit_r)
        self.sense = sense

    def move_right(self):
        if self.position < self.limit_r:
            self.position=self.position+1
            self.display(1)

    def move_left(self):
        if self.position > self.limit_l:
            self.position = self.position-1
            self.display(-1)

    def display(self, move):
        y=7
        x=self.position%8
        self.sense.set_pixel(x-move,y,(5,5,5))
        self.sense.set_pixel(x,y,(255,255,255))