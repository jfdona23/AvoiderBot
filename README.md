# AvoiderBot - Another "dodge everything" robot

## About
This project is just for fun and serves to improve my skill using micropython among other things.
It's based on the already known ESP32, it's in particular is a **DOIT DevKit v1 board**. Also features an independent Quelima SQ12 camera to record its trip.

## How it works...briefly
The robot acts by its own using a **HC-SR04** ultrasonic sensor to detect any obstacle in front of him. Then analyzes his surroundings moving the sensor 90 degrees in both directions and deciding which direction has the farest obstacle. The motor part is handled by two 3v-12v DC motors with gearbox (yes, the yellow ones) and a tiny **L9110** which is a simple double "H bridge" to control the motor and its spin direction.

The [SQ12](https://org-info.mobi/manual/sq12-en.htm) camera is a tiny DVR camera, generally used in sports or short trips due its small battery (around 200mah).
In my case the battery just got fried so I'm investigating the  best and safer way to supply power to this tiny thing without need to buy a new battery:
1. One option is supply the camera through its own "USB" port, but I need to use the provided USB cable since is has a non-standard USB socket on the camera.
2. A second option is soldering two wires where the original battery was and connect it to 5v on the breadboard. I'm not so confident that it has an internal 3V3 regulator, however it should have one.

I've chosen [micropython](https://github.com/micropython/micropython) as the main language for this project due I already know the language and also I prefer to work with its [REPL](https://github.com/micropython/webrepl) instead of upload Arduino .ino files everytime I need to test a new change.

Oh, and it has two leds to provide feedback to the user. I've not decided what kind of feedback although.

## What's next?
A few ideas for the future are:
* Be able to control the robot through WiFi or Bluetooth.
* Remove the camera and add a few motors to shoot Nerf darts. I got the idea from [here](https://create.arduino.cc/projecthub/Little_french_kev/bluetooth-nerf-turret-03363b)
* Improve the robot capabilities using the Cloud. Maybe some AWS Lambda functions and an API gateway, IFTTT webhooks or even Machine Learning, why not?
* At some point, I would like to replace the wheels with tank tracks (caterpillar tracks).
