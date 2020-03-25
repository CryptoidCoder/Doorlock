#imports
import RPi.GPIO as GPIO
import time

#ledpin variable enter what pin the LED is in below
ledpin = 25

#GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(ledpin, GPIO.OUT)

#testing
for i in range(3):

    print("LED on")
    GPIO.output(ledpin, GPIO.HIGH)
    time.sleep(1)
    print("LEd off")
    GPIO.output(ledpin, GPIO.LOW)

print("end of program")
input("press any key to continue...")
