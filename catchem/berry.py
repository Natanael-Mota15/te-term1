import random

from time import sleep

from sense_hat import SenseHat

sense = SenseHat()






class Berry:
    def __init__(self, value, speed, color):
        self.positiony = 0
        self.position = random.randint(0,7)
        self.color=color
        self.speed=speed
        self.value=value

    def drop(self):
        if self.positiony >= 0 and self.position < 7:
            self.positiony+=1
            sleep(self.speed)
            self.display()

    def display(self):
        if self.positiony > 0:
            sense.set_pixel(self.position,(self.positiony-1),self.color)
            sense.set_pixel(self.position,self.positiony-1,self.color)






