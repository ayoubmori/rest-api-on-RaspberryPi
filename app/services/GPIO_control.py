import RPi.GPIO as GPIO
from time import sleep

from app.services.GPIO_pins import relay_pins, digital_input_pins
from app.services.GPIO_state import *


### configure relay
def configure_relay(relay_id, state):
    # Set the GPIO pin number you want to use
    pin_number = get_relay_pin(relay_id)
    # Set up the pin as an output
    sleep(0.2)
    if state.upper() == "ON":
        GPIO.output(pin_number, GPIO.HIGH)
    elif state.upper() == "OFF":
        GPIO.output(pin_number, GPIO.LOW)
    else:
        print("Invalid state. Please specify 'on' or 'off'.")




