import RPi.GPIO as GPIO

class GPIOcleanup(GPIO):
	GPIO.cleanup()