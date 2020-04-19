from machine import Pin, PWM
from utime import sleep
from motors import Motors
from hcsr04 import HCSR04


# LED port definitions
ledBoard = Pin(2, Pin.OUT)
ledRed = Pin(3, Pin.OUT)
ledBlue = Pin(4, Pin.OUT)

# HC-SR04 port definitions
sonar = HCSR04(trigger_pin=5, echo_pin=6)

# Servo motor port definitions
servo1 = PWM(Pin(7), freq=50)   # Duty cycle for my SG09 servo is between 20 - 125. Usual freq for servos is 50Hz.
                                # Detailed info in https://learn.sparkfun.com/tutorials/pulse-width-modulation/all

# DC Motor port definitions
motorRA = Pin(13, Pin.OUT)
motorRB = Pin(14, Pin.OUT)
motorLA = Pin(15, Pin.OUT)
motorLB = Pin(16, Pin.OUT)
motion = Motors(motorRA, motorRB, motorLA, motorLB)
