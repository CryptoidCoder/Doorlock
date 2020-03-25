import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

#LED
GPIO.setup(25, GPIO.OUT)
#Buzzer
GPIO.setup(24, GPIO.OUT)

while True: # Run forever
    if GPIO.input(18) == GPIO.HIGH:
        print("Button was pushed!")
        GPIO.output(25, GPIO.HIGH)
        GPIO.output(24, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(25, GPIO.LOW)
        GPIO.output(24, GPIO.LOW)