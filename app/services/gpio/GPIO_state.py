import RPi.GPIO as GPIO
from time import sleep

from app.services.GPIO_pins import relay_pins, digital_input_pins
from app.services.Set_GPIO import SetUp_GPIO


# get the relay pin
def get_relay_pin(relay_id):
    global relay_pins
    relay_pin_number = relay_pins[relay_id]
    return relay_pin_number


# get pin status
def relay_pin_status(relay_id):
    pin_number = get_relay_pin(relay_id)
   #GPIO.setmode(GPIO.BOARD)  # Set pin numbering mode to board
    state = GPIO.input(pin_number)
    return "ON" if state else "OFF"


# get the digital-input pin
def get_digital_input_pin(dgip_id):
    global digital_input_pins
    dgip_pin_number = digital_input_pins[dgip_id]
    return dgip_pin_number


# get pin status
def dgip_pin_status(dgip_id):
    pin_number = get_digital_input_pin(dgip_id)
    #GPIO.setmode(GPIO.BOARD)  # Set pin numbering mode to board
    state = GPIO.input(pin_number)
    return "ON" if state else "OFF"
