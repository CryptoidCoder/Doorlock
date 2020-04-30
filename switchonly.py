#Only use the Buttons to open the door


import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#Motor
GPIO.setup(10, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
#LED
GPIO.setup(25, GPIO.OUT)
#Buzzer
GPIO.setup(24, GPIO.OUT)

while True: # Run forever
    #unlock
    if GPIO.input(18) == GPIO.HIGH:
        print("Button one was pushed!")
        #on
        GPIO.output(25, GPIO.HIGH)
        GPIO.output(24, GPIO.HIGH)
        time.sleep(0.5)
        #off
        GPIO.output(25, GPIO.LOW)
        GPIO.output(24, GPIO.LOW)
        #motor move
        GPIO.output(9, 1)
        GPIO.output(10, 0)
        time.sleep(0.1)
        #motor stop
        GPIO.output(10,0)
        GPIO.ouput(9,0)

    #lock
    elif GPIO.input(27) == GPIO.HIGH:
        print("Button two was pushed!")
        #on
        GPIO.output(25, GPIO.HIGH)
        GPIO.output(24, GPIO.HIGH)
        time.sleep(1)
        #off
        GPIO.output(25, GPIO.LOW)
        GPIO.output(24, GPIO.LOW)
        time.sleep(0.5)
        #on
        GPIO.output(25, GPIO.HIGH)
        GPIO.output(24, GPIO.HIGH)
        time.sleep(1)
        #off
        GPIO.output(25, GPIO.LOW)
        GPIO.output(24, GPIO.LOW)

        #motor move
        GPIO.output(9, 1)
        GPIO.output(10, 0)
        time.sleep(0.1)
        #motor stop
        GPIO.output(10,0)
        GPIO.ouput(9,0)
