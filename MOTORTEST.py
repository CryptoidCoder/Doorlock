#imports
import RPi.GPIO as GPIO
import time

#ledpin variable enter what pin the LED is in below
motorpin1 = 10
motorpin2 = 9

#GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(motorpin1, GPIO.OUT)
GPIO.setup(motorpin2, GPIO.OUT)

input("press any key to move motor...")
# motor movement
GPIO.output(motorpin1, 0)
GPIO.output(motorpin2, 1)

#wait
time.sleep(0.3)

#turning off the motor
GPIO.output(motorpin1, 0)
GPIO.ouput(motorpin2, 0)

input("press any key to move motor other direction... ")

# motor movement
GPIO.output(motorpin1, 1)
GPIO.output(motorpin2, 0)

#wait
time.sleep(0.3)

#turning off the motor
GPIO.output(motorpin1, 0)
GPIO.ouput(motorpin2, 0)

print("program finished")
input("press nay key to continue...")