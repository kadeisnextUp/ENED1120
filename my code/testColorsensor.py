#!/usr/bin/env python3
from ev3dev2.sensor import *
from ev3dev2.console import Console
from ev3dev2.sensor.lego import *
from ev3dev2.sound import Sound
from ev3dev2.display import *
from ev3dev2.motor import *
from apr import APR 
import time
from os import *

#testing color sensor
colorScanner = ColorSensor(INPUT_1)

x = 0
values = []

#while x <4:
    #scan = colorScanner.reflected_light_intensity
    #values.append(scan)
    #x = x+1

#print(values)
