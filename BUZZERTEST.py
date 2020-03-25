
#imports
import RPi.GPIO as GPIO
import time

#ledpin variable enter what pin the BUZZER is in below
buzzerpin = 24

#GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(buzzerpin, GPIO.OUT)

#testing
for i in range (3):
    print("BUZZER on")
    GPIO.output(buzzerpin, GPIO.HIGH)
    time.sleep(1)
    print("BUZZER off")
    GPIO.output(buzzerpin, GPIO.LOW)

print("end of program")
input("press any key to continue...")
