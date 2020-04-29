# AvoiderBot - Another "dodge everything" robot

## Table of contents
1. [About](#about)
2. [How it works...briefly](#how-it-worksbriefly)
3. [Additional libraries used in this project](#additional-libraries-used-in-this-project)
4. [What's next?](#whats-next)

## About
This project is just for fun and serves to improve my skill using micropython among other things.\
It's based on the already known ESP32, it's in particular is a **DOIT DevKit v1 board** (see the pinout [here](./esp32_devkit_v1-1.png) and further details [here](https://circuits4you.com/2018/12/31/esp32-devkit-esp32-wroom-gpio-pinout/)). Also this robot features an *independent* Quelima SQ12 camera attached to the chases to record its trip.

## How it works...briefly
The robot acts by its own using a **HC-SR04** ultrasonic sensor to detect any obstacle in front of him. Then analyzes his surroundings moving the sensor 90 degrees in both directions and deciding which direction has the farest obstacle. The motor part is handled by two 3v-12v DC motors with gearbox (yes, the yellow ones) and a tiny **L9110** which is a simple double *H bridge* to control the motor and its spin direction.

The [SQ12](https://org-info.mobi/manual/sq12-en.htm) camera is a tiny DVR camera, generally used in sports or short trips due its small battery (around 200mah).\
In my case the battery just got fried so I'm investigating the  best and safer way to supply power to this tiny thing without need to buy a new battery:
1. ~~One option is supply the camera through its own "USB" port, but I need to use the provided USB cable since is has a non-standard USB socket on the camera.~~
2. A second option is soldering two wires where the original battery was and connect it to 5v on the breadboard. I'm not so confident that it has an internal 3V3 regulator, however it should have one. (**I've chosen this option and it worked flawlessly**).

I've chosen [micropython](https://github.com/micropython/micropython) as the main language for this project due I already know the language and also I prefer to work with its [REPL](https://github.com/micropython/webrepl) instead of upload Arduino *.ino* files everytime I need to test a new change.\

Oh, and it has two leds to provide feedback to the user. I've not decided what kind of feedback although.

## Additional libraries used in this project
* **HCSR04** library is from [here](https://github.com/rsc1975/micropython-hcsr04). I've tweaked the library (PR [here](https://github.com/rsc1975/micropython-hcsr04/pull/7)) to imports *sleep_us* from *utime* instead of *time* itself. Also from *machine* only imports the needed functions, which are *Pin* and *time_pulse_us*. Micro libraries (those with 'u' at the begining) are better suitbale for hardware like microcontrollers, therefore are more efficent. Finally, bear in mind I re-wrote the lines containing *time.* and *machine.* to fit with this change. For instance:
```python
# Replaced
pulse_time = machine.time_pulse_us(self.echo, 1, self.echo_timeout_us)
# with this:
pulse_time = time_pulse_us(self.echo, 1, self.echo_timeout_us)
```
* Servos doesn't need any library to work with an ESP32 but I've learned about how to use them [from here](https://icircuit.net/micropython-controlling-servo-esp32-nodemcu/2385). And also a few PWM details from [this Sparkfun website](https://learn.sparkfun.com/tutorials/pulse-width-modulation/all).
* **Motors** library is just a Class made by me to get the motors logic apart from the main code.
* **Credentials** is another Class made by me to store passwords and personal data. Then I ignore *credentials.py* file using *.gitignore*. The Class content is the following:
```python
class Creds:
    def __init__(self, hostname, user, passwd):
        self.hostname = hostname
        self.user = user
        self.passwd = passwd

# And then I can create any secret as an object:
my_wifi = creds("dummyHost", "mySSID", "mySuperPassword")
```
* Not a library per se, but I did a remix from an existing [3D printed chassis](https://www.thingiverse.com/thing:1843364/makes) that could be useful to mount the robot.\
I ended up doing my own chassis because 3D printing is pretty expensive in my country (Argentina) but I've uploaded the original files and the remixed ones adding a roof for additional components and shortening the base a little bit. Also, there are a few files to reach the author and his/her original post.

## What's next?
A few future ideas are:
* Be able to control the robot through WiFi or Bluetooth. (See [RestfulBot](https://github.com/jfdona23/RestfulBot) project)
* Remove the camera and add a few motors to shoot Nerf darts. I got the idea from [here](https://create.arduino.cc/projecthub/Little_french_kev/bluetooth-nerf-turret-03363b)
* Improve the robot capabilities using the Cloud. Maybe some AWS Lambda functions and an API gateway, IFTTT webhooks or even Machine Learning, why not?
* At some point, I would like to replace the wheels with tank tracks (caterpillar tracks).
