# Microbit-Racing-Car-Timing-Gate
Create a speed trap for toy cars with three Microbits, torches, radio and REPL in Python.

![3D printed timing gate](https://github.com/astrotutor9/Microbit-Racing-Car-Timing-Gate/blob/master/Small_MicroBit_Start_Gate.jpg)

The aim of this exercise is to find the fastest toy car by timing it over a set distance.

### This will utilise:

- 3 Microbit
- Mu Editor
- Sloping ramp
- Two torches
- Sticky tape/tack
- Radio
- While Loops
- If control flow
- REPL ‘Read, Evaluate, Print, Loop’

## How It Works
Two micro bits are used as timing traps. A torch shines a light across the track onto a Microbit. The LED on the front are sensitive to light and when a car’s shadow passes in front of the LED the drop in light intensity signal can be used to trigger a timer. One to start a second another to stop. A third Microbit receives the timing signals, reads the times then calculates and displays the speed for each run.

### Notes for those who don't read instructions

This exercise utilises the Mu Editor for the Microbit.

In the Python **language spelling and punctuation are important**. Capital letters When needed are Important. Brackets () also have a habit of being missed.
Also indented code after a colon : 
is also important. 
Missing the : will result in an error. You have been warned!

**Read the instructions!**

The radio uses a default channel for communication. If there are teams of you making these timers add this radio configuration code to each script before the radio.on line. Where 7 is replaced with a number between 0 and 100. The same number for the three Microbits but different for each team.

`radio.config(channel=7)`

## Printing a Received Radio Message
Take one Microbit and connect to the computer. Open the Mu editor and a new program page. Save this as your ‘receiver’. This is the Microbit that will calculate the speed. 
Start with this basic code:

```
from microbit import *
import radio`

radio.on()
print("Ready")
```

The first two lines of code bring into your program information about the Microbit and how it works and also the radio to receive messages. The next just turns the radio on and then prints a line of text saying ‘ready’. Just to prove the program is running and waiting.

Copy this code to the Microbit by pressing Flash. Then when the code has been successfully copied across click the REPL button. 
A new editor window will open with >>> showing. This shows Python is running on the Microbit. Now **press the reset button on the back** of the Microbit to start the code running. The ‘ready’ message should show up and then the program stops. That is all the program does at the moment. You will use the REPL for the reading the light values and speeds.

Close the REPL by clicking the button again. Now add **below** your code the following: 

```
while True:
   `message = radio.receive()
    if message:
        print(message)
```

Note the : and indented code after the True.

This is a forever loop. Continually checking if any ‘message’ is received. ‘Message’ is just a variable name this code gives to any information received by radio. Message is just a name though. It could just as easily be called ‘car_passed_the_gate’ or  ‘Josephine’. Just as long as it makes sense and you use the same expression throughout the whole code. 
Then if a message is received it is printed in the REPL.

Now flash this code across. Disconnect the Microbit and put aside and replace it with another.

## Sending the Sensed Light Values
Copy the code here into a new editor tab and flash it onto the Microbit. Some lines are the same as before. Save time by **copy/paste** the code across from the other program tab.

```
from microbit import *
import radio

radio.on()

while True:
    light_level = display.read_light_level()
    radio.send(str(light_level))
    sleep(1000)
```

Here there is another forever loop in the code continually reading the light level falling onto the Microbit LED and sending it out by radio. The program then waits a second before doing it again and again. The light_level variable name (note that it is sensibly named) is sent as a string (str) of text not a number. The Microbit radio only sends letters (text) not mathematical numbers. The value sent over radio is not a number you can do maths with, unless it is reconverted back into a number (integer).

![Masked Microbit](https://github.com/astrotutor9/Microbit-Racing-Car-Timing-Gate/blob/master/Small_Microbit_masked.jpg)

Flash the code and disconnect the the Microbit. Stick a piece of tape or Blutac over the LED on the front leaving just the left side clear. This makes for a nice sharp timing gate. Tape the Microbit to the side of the track and place a torch across from it shining onto the LED. Plug in the battery pack.

Reattach the original receiver Microbit to the computer and start the REPL. Remember to restart the Microbit to get the ‘Ready’ message.

Slowly place a car in front of the sensor so that it casts a shadow onto the LED and watch how the values drop. Make sure there is a shadow from the torch light falling onto the LED when a car crosses in front of the Microbit. None of this will work if there is no shadow.

Note down a value that could be used to determine the point that a car crosses the gate. (Our tests with our torches and width of track gave 280 for no car and around 100 as a good cross point).

## Starting the Start, Stopping the Stop
Stop the REPL, remove the receiver Microbit and reinsert the one that is the timing gate. **Change** the timing gate code **utilising your value recorded above** instead of the 100.

DO NOT ADD ALL THIS CODE BELOW WHAT YOU ALREADY HAVE. 
ADD JUST WHAT YOU NEED.

```
from microbit import *
import radio

radio.on()

while True:
   light_level = display.read_light_level()

    if light_level < 100:
        radio.send("Start")
        sleep(1000)
    sleep(10)
```

This new code now only sends a message, which is the word ‘Start”, when the value drops to below the start sensing value. Flash this code onto the Microbit. Set aside as the Start Gate. Now add the third Microbit to the computer.

Use the same code for the third Microbit to be the stopping gate. **Change the radio.send** from ‘Start’ to ‘**Stop**’. Flash the code and remove the Microbit.

## Test the Start Stop
Reconnect the receiver Microbit and start the REPL as before to test the code. With battery packs connected to the other two Microbits place the Start and Stop timing gates on the side of the track with their torches. Place them a measured distance apart from LED to LED. We used 250mm or 0.25m for our tests. Place them near the lower part of the slope so that the car has time to get up to speed.

Let a car run down the track and see if the Start and Stop messages appear on the REPL. Adjust the torches if not to make sure a shadow passes over the LED.

## The Timer
The final coding part is to calculate the speed from the arrival times of the ‘Start’ and ‘Stop’ signals. 

The Microbits can count, in milliseconds, the amount of time that has passed since they are switched on. By recording the time at the point of receiving the two messages and subtracting the lower start time from the larger stop time the elapsed time is found. If you then know the distance between the two LED on the track the speed can be calculated.

## Set up the Track
The final piece of the code is then this for the receiver. **Change** the code you already have **to match this** but with your distance in metres. So half a metre is 0.5.

The ticks_ms is the millisecond timing information to use in the code. One millisecond is a tick of the clock. One thousand milliseconds is one second.

```
import radio
from time import ticks_ms
```

The start_time, and stop_time, are variables that are used to briefly hold the start and stop values for the calculation. These are set to zero just to start with.

```
radio.on()
print("Ready")
start_time = 0
stop_time = 0
```


This is the big bit of code.  The if and elif check to see which message is received when a message is received. (if message is the same as (==) ‘Start’. Else if (elif) the message is the same as (==) ‘Stop’).

The start_time (or stop_time) are then set to the value of the ticks as described above. These times are then printed onto the screen under the REPL. 

```
while True:
    message = radio.receive()

    if message == 'Start':
        start_time = ticks_ms()
        print("Start timing at " + str(start_time))

    elif message == 'Stop':
        stop_time = ticks_ms()
        print("Stop timing at " + str(stop_time))

        time_difference = stop_time - start_time       
        car_speed = (0.25 / (time_difference)) * 1000  
        print("Speed of car " + str(car_speed) + " m/sec")
```

Once the stop message has been received the calculation is made. First the time difference is calculated. Then the speed is the distance travelled between the two gates in metres divided by the time difference between the two gates in milliseconds and then all multiplied by 1000 to convert milliseconds per metre to seconds per metre. And the result is printed.  

Here is an example of the timing achieved on the REPL.

![Screen grab from the Mu REPL](https://github.com/astrotutor9/Microbit-Racing-Car-Timing-Gate/blob/master/Mu_screen.jpg)

So which of your cars is the fastest, or slowest!
