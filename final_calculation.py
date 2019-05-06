from microbit import *
import radio

from time import ticks_ms

radio.config(channel=3)
radio.on()

print("Ready")

start_time = 0
stop_time = 0

while True:
    message = radio.receive()
    if message == "Start":
        start_time = ticks_ms()
        print("Start time " + str(start_time))
    
    elif message == "Stop":    
        stop_time = ticks_ms()
        print("Stop time " + str(start_time))
        car_speed = (0.4/(stop_time - start_time))*1000
        print("Speed of car " + str(car_speed) + " m/sec")