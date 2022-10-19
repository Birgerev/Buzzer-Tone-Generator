import RPi.GPIO as GPIO
import time

#----- PINS ------#
# Uses 3v3 pin 17 
# Uses ground pin 20
buzzerPin = 24 # IO pin 18

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzerPin, GPIO.OUT)

print("Enter desired frequency as a number:")
freq = int(input())
cycleDuration = 1 / freq

print("Now playing frequency: " + str(freq) + "Hz")
print("A single cycle spans: " + str(cycleDuration) +"s")
print("")
print("A tone should now be heard (Best of luck otherwise)")

try:
	while True:
		GPIO.output(buzzerPin, GPIO.HIGH)
		time.sleep(cycleDuration/2)
		GPIO.output(buzzerPin, GPIO.LOW)
		time.sleep(cycleDuration/2)


# Detect CTRL + C command to exit program
except KeyboardInterrupt:
	print ("keyboard interrupt detected!")
finally:
	GPIO.cleanup()
	print ("exit...")
	time.sleep(0.5)
