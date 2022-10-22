from gpiozero import LED
from time import sleep

led = LED(17)
want = "on"

while (want == "on"):
    print("On")
    led = LED(17)
    led.on()
    sleep(1)
    led.off()
    sleep(1)
    want = input("on or off").lower
while (want == "off"):
    led.off()
    want = input("on or off").lower
else:
    want = input("on or off").lower