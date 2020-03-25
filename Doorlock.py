
# This program allows a user to enter a
# Code. If the C-Button is pressed on the
# keypad, the input is reset. If the user
# hits the A-Button, the input is checked.

import RPi.GPIO as GPIO
import time


# These are the GPIO pin numbers where the
# lines of the keypad matrix are connected
L1 = 5
L2 = 6
L3 = 13
L4 = 19

# These are the four columns
C1 = 12
C2 = 16
C3 = 20
C4 = 21

# The GPIO pin of the column of the key that is currently
# being held down or -1 if no key is pressed
keypadPressed = -1

secretCode = "1234"
#resetcode = "9999"
#endcode = "0123456789"

input = ""

# Setup GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#variables for Buzzer, Motor, LED and switch
motorpin1 = 10
motorpin2 = 9
buzzerpin = 24
ledpin = 25
switchpin = 18

GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(L3, GPIO.OUT)
GPIO.setup(L4, GPIO.OUT)


#switch
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(switch, GPIO.IN)
#LED
GPIO.setup(ledpin, GPIO.OUT)
#Buzzer
GPIO.setup(buzzerpin, GPIO.OUT)

#Motor
GPIO.setup(motorpin1, GPIO.OUT)
GPIO.setup(motorpin2, GPIO.OUT)


def MotorStop():
    GPIO.output(motorpin1, 0)
    GPIO.output(motorpin2, 0)

def motorClockwise():
    GPIO.output(motorpin1, 1)
    GPIO.output(motorpin2, 0)

def MotorAntiClockwise():
    GPIO.output(motorpin1, 0)
    GPIO.output(motorpin2, 1)

def LEDON():
    print ("LED on")
    GPIO.output(ledpin,GPIO.HIGH)

def LEDOFF():
    print("LED off")
    GPIO.output(ledpin, GPIO.LOW)


def Buzzer():
    print("Buzzer")
    GPIO.output(buzzerpin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(buzzerpin, GPIO.LOW)
    time.sleep(0.5)

def unlock():
    print ("unlock")
    motorClockwise()
    for x in range(3):
        LEDON()
        time.sleep(0.5)
        Buzzer()
        LEDOFF()

def lock():
    print("lock")
    for x in range(3):
        LEDON()
        time.sleep(0.5)
        Buzzer()
        LEDOFF()

        #so that when you press the button it will unlock
while true:
    if GPIO.input(18) == GPIO.HIGH:
            unlock()
            Buzzer()
            print("Button Pressed")


# Use the internal pull-down resistors
GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# This callback registers the key that was pressed
# if no other key is currently pressed
def keypadCallback(channel):
    global keypadPressed
    if keypadPressed == -1:
        keypadPressed = channel

# Detect the rising edges on the column lines of the
# keypad. This way, we can detect if the user presses
# a button when we send a pulse.
GPIO.add_event_detect(C1, GPIO.RISING, callback=keypadCallback)
GPIO.add_event_detect(C2, GPIO.RISING, callback=keypadCallback)
GPIO.add_event_detect(C3, GPIO.RISING, callback=keypadCallback)
GPIO.add_event_detect(C4, GPIO.RISING, callback=keypadCallback)

# Sets all lines to a specific state. This is a helper
# for detecting when the user releases a button
def setAllLines(state):
    GPIO.output(L1, state)
    GPIO.output(L2, state)
    GPIO.output(L3, state)
    GPIO.output(L4, state)

def checkSpecialKeys():
    global input
    pressed = False

    GPIO.output(L3, GPIO.HIGH)

    if (GPIO.input(C4) == 1):
        print("Input reset!");
        pressed = True

    GPIO.output(L3, GPIO.LOW)
    GPIO.output(L1, GPIO.HIGH)

    if (not pressed and GPIO.input(C4) == 1):
        if input == secretCode:
            print("Code correct!")
            unlock()
            # TODO: Unlock a door, turn a light on, etc.
        #elif input == resetcode:
            #print("reset code entered")
            #secretCode = int(input("input new code: "))
            #print(secretCode)
            

        #elif input == endcode:
            #print("end code entered.")
            #print("stopping...")
            #print("type 'doorlock' to restart system")
            #exit()

       

        else:
            print("Incorrect code!")
            lock()            
            # TODO: Sound an alarm, send an email, etc.
        pressed = True
        
    GPIO.output(L3, GPIO.LOW)

    if pressed:
        return pressed

# reads the columns and appends the value, that corresponds
# to the button, to a variable
def readLine(line, characters):
    global input
    # We have to send a pulse on each line to
    # detect button presses
    GPIO.output(line, GPIO.HIGH)
    if(GPIO.input(C1) == 1):
        input = input + characters[0]
    if(GPIO.input(C2) == 1):
        input = input + characters[1]
    if(GPIO.input(C3) == 1):
        input = input + characters[2]
    if(GPIO.input(C4) == 1):
        input = input + characters[3]
    GPIO.output(line, GPIO.LOW)

try:
    while True:
        # If a button was previously pressed,
        # check, whether the user has released it yet
        if keypadPressed != -1:
            setAllLines(GPIO.HIGH)
            if GPIO.input(keypadPressed) == 0:
                keypadPressed = -1
            else:
                time.sleep(0.1)
        # Otherwise, just read the input
        else:
            if not checkSpecialKeys():
                readLine(L1, ["1","2","3","A"])
                readLine(L2, ["4","5","6","B"])
                readLine(L3, ["7","8","9","C"])
                readLine(L4, ["*","0","#","D"])
                time.sleep(0.1)
            else:
                time.sleep(0.1)
except KeyboardInterrupt:
    print ("/Application Stopping")