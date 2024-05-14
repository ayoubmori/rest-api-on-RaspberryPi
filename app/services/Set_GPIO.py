import RPi.GPIO as GPIO

def SetUp_GPIO():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
