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

#testing
print("Closing DeadBolt")
GPIO.output(motorpin1, 1)
GPIO.output(motorpin2, 0)
time.sleep(1)

#end of program exit



