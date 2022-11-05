from sense_hat import SenseHat
import random
from player import Player
from berry import Berry
from time import sleep


sense=SenseHat()

class Game:
    def __init__(self):
        self.score = 0
        self.speed = 0.5
        # self.berry = []
        self.game_over = False
        self.player = Player(56,63,sense)
        self.berry = Berry(1,1,(255,10,10))


    def start(self):
        sense.show_message("Catchem",text_colour=(0,0,255),scroll_speed=0.05)
        

    def play(self):
        self.start()
      
        while not self.game_over:
            self.berry.display()
            self.berry.drop()
            self.player.display(0)
            
            
            for event in sense.stick.get_events():
                
                if event.action == "pressed" and event.direction == "left":
                    self.player.move_left()
                elif event.action == "pressed" and event.direction == "right":
                    self.player.move_right()


