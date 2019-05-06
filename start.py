from microbit import *
import radio
radio.config(channel=3)

radio.on()

while True:
    light_level = display.read_light_level()
    if light_level < 140:
        radio.send("Start")
        sleep(1000)
