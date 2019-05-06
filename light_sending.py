from microbit import *
import radio
radio.config(channel=3)

radio.on()

while True:
    light_level = display.read_light_level()
    radio.send(str(light_level))
    sleep(1000)