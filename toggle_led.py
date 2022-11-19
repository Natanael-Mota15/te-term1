from gpiozero import LED
from time import sleep

led = LED(17)
want = "on"

while True:#(want == "on"):
    print(want)

    want = input("on or off").lower()
    if want == "on":
        led.on()
        sleep(1)
        print("Light is on")
    elif want == "off":
        led.off()
        sleep(1)
        print("light is off")
    else:
        print("This shouldn't happen")
    
# while (want == "off"):
#     led.off()
#     want = input("on or off").lower
# else:
#     want = input("on or off").lower