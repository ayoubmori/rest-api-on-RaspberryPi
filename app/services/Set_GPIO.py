import RPi.GPIO as GPIO
from app.services.GPIO_pins import relay_pins, digital_input_pins

def SetUp_GPIO():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

def setup_pins():
    """Set up all GPIO pins."""
    # Set all relay pins as outputs
    for relay_pin in relay_pins.values():
        GPIO.setup(relay_pin, GPIO.OUT)

    # Set all digital input pins as inputs
    for digital_input_pin in digital_input_pins.values():
        GPIO.setup(digital_input_pin, GPIO.IN)