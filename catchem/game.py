from sense_hat import SenseHat
import random
import time
from player import Player

sense=SenseHat()

class Game:
    def __init__(self):
        self.score = 0
        self.speed = 0.5
        self.berry = []
        self.game_over = False
        self.player = Player(56,63,sense)


    def start(self):
        sense.show_message("Catchem",text_colour=(0,0,255),scroll_speed=0.05)
        

    def play(self):
        self.start()
        self.player.display()
        while not self.game_over:
            for event in sense.stick.get_events():
                if event.action == "pressed" and event.direction == "left":
                    self.player.move_left()
                elif event.action == "pressed" and event.direction == "right":
                    self.player.move_right()
