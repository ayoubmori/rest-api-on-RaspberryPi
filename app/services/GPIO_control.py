import RPi.GPIO as GPIO
from time import sleep

from app.services.GPIO_pins import relay_pins, digital_input_pins
from app.services.GPIO_state import *
from app.services.Set_GPIO import SetUp_GPIO


### configure relay
# turn on relay
def turn_relay_on(relay_id):
    SetUp_GPIO()
    # Set the GPIO pin number you want to use
    pin_number = get_relay_pin(relay_id)
    # Set up the pin as an output
    GPIO.setup(pin_number, GPIO.OUT)
    sleep(0.2)
    GPIO.output(pin_number, GPIO.HIGH)


# turn off relay
def turn_relay_off(relay_id):
    SetUp_GPIO()
    # Set the GPIO pin number you want to use
    pin_number = get_relay_pin(relay_id)
    # Set up the pin as an output
    GPIO.setup(pin_number, GPIO.OUT)
    sleep(0.2)
    GPIO.output(pin_number, GPIO.LOW)



