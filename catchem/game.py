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
        self.player = Player(56,63)


    def start(self):
        sense.shoe_message("Catchem",text_colour=colors.o,scroll_speed=0.05)


    def play(self):
        self.start()
        while not self.game_over:
            for event in sense.stick.get_events():
                if event.action == "pressed" and event.direction == "left":
                    print("left")
                elif event.action == "pressed" and event.direction == "right":
                        print("right")
