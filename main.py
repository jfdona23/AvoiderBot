from machine import Pin, PWM
from utime import sleep
from motors import Motors
from hcsr04 import HCSR04


# LED port definitions
ledBoard = Pin(2, Pin.OUT)
ledRed = Pin(22, Pin.OUT)
ledBlue = Pin(23, Pin.OUT)

# HC-SR04 port definitions
sonar = HCSR04(trigger_pin=25, echo_pin=26)

# Servo motor port definitions
servo1 = PWM(Pin(21), freq=50)  # Duty cycle for my SG09 servo is between 20 - 125. Usual freq for servos is 50Hz.
                                # Detailed info in https://learn.sparkfun.com/tutorials/pulse-width-modulation/all

# DC Motor port definitions
motorRA = Pin(27, Pin.OUT)
motorRB = Pin(14, Pin.OUT)
motorLA = Pin(12, Pin.OUT)
motorLB = Pin(13, Pin.OUT)
motion = Motors(motorRA, motorRB, motorLA, motorLB)
