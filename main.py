from machine import Pin, PWM
from utime import sleep
from motors import Motors
from hcsr04 import HCSR04


# LED port definitions
ledBoard = Pin(2, Pin.OUT)
ledRed = Pin(16, Pin.OUT)
ledBlue = Pin(17, Pin.OUT)

# HC-SR04 port definitions
sonar = HCSR04(trigger_pin=25, echo_pin=26)

# Servo motor port definitions
servo1 = PWM(Pin(21), freq=50)  # Duty cycle for my SG09 servo is between 20 - 125. Usual freq for servos is 50Hz.
                                # Detailed info in https://learn.sparkfun.com/tutorials/pulse-width-modulation/all

# DC Motor port definitions
motorLA = Pin(27, Pin.OUT)
motorLB = Pin(14, Pin.OUT)
motorRA = Pin(12, Pin.OUT)
motorRB = Pin(13, Pin.OUT)
motion = Motors(motorRA, motorRB, motorLA, motorLB)
motion.stop() # Ensure the motors are stopped

"""
Useful function to control led blinking.
Parameters are:
- The led to control as a Pin object.
- The ON time in seconds
- The OFF time in seconds
- The amount of blinks.
"""
def blinkLed(led, onTime, offTime, blinks):
    for _ in range(blinks):
        led.value(not led.value())
        sleep(onTime)
        led.value(not led.value())
        sleep(offTime)

"""
This function is intended to provide visual feedback the user about the HW functioning.
It has not any way to recognize faulting hardware, so that depends on the user only.
Tests:
- Turn on the board's led for 2 seconds.
- Turn on the red led for 2 seconds.
- Turn on the red led for 2 seconds.
- Move the ultrasonic sensor to the right and left, then leave it in  the middle.
- Call sonar.distance_cm() and if it's grater than 5cm blink the board's led two times.
  Otherwise board's led will blink four times.
- Call motion.left() and motion.right() to test the motors.
  That way if one of the motors is failing, it should be easier to see.
"""
def selfTest():
    blinkLed(ledBoard, 2, 0.1, 1)
    blinkLed(ledRed, 2, 0.1, 1)
    blinkLed(ledBlue, 2, 0.1, 1)

    sleep(0.5)

    servo1.duty(70); sleep(0.3)
    servo1.duty(20); sleep(0.3)
    servo1.duty(70); sleep(0.3)
    servo1.duty(125); sleep(0.3)
    servo1.duty(70); sleep(0.3)

    sleep(0.5)

    if sonar.distance_cm() > 5:
        blinkLed(ledBoard, 0.5, 0.3, 2)
    else:
        blinkLed(ledBoard, 0.5, 0.3, 4)

    sleep(0.5)

    motion.left()
    sleep(0.5)
    motion.stop()

    motion.right()
    sleep(0.5)
    motion.stop()

def fixDirection():
  motion.backward()
  sleep(0.3)
  motion.stop()

  # Look for nearby objects
  servo1.duty(20) # Turn sonar to the Right
  distRight = sonar.distance_cm()
  sleep(0.5)
  servo1.duty(125) # Turn sonar to the Left
  distLeft = sonar.distance_cm()
  sleep(0.5)
  servo1.duty(70) # Leave sonar in the middle

  if distLeft > distRight:
    motion.left()
    sleep(0.4)
    motion.stop()
  else:
    motion.right()
    sleep(0.4)
    motion.stop()

def main():
  while True:
    if sonar.distance_cm() < 25:
      motion.stop()
      fixDirection()
    else:
      motion.forward()

selfTest()
main()