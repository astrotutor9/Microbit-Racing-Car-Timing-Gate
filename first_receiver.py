from microbit import *
import radio

radio.config(channel=3)
radio.on()

print("Ready")

while True:
    message = radio.receive()
    if message:
        print(message)