#!/usr/bin/env python3

# 
# Activity Project 4
# File: scanner.py
# Date: 11/14/23
# By: Kaden Sawyer
# Section: 001
# Team: 029
# 
# ELECTRONIC SIGNATURE
# Kaden Sawyer
# 
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
# 
# code for the color scanner
# 
from ev3dev2.sensor import *
from ev3dev2.console import Console
from ev3dev2.sensor.lego import *
from ev3dev2.sound import Sound
from ev3dev2.display import *
from ev3dev2.motor import *
from apr import APR 
import time
from os import *


# start sound
note = Sound()
#spkr.play_note("D4", 0.25, 100, Sound.PLAY_NO_WAIT_FOR_COMPLETE)

#box 1: wwwb box 2:wbwb box 3:wwbb box 4:bwwb


#reads barcodes vertically 
def barcodeScanner():
    robot = APR(OUTPUT_B,OUTPUT_A,INPUT_2,OUTPUT_C)

    #display
    console = Console()
    console.set_font("Lat15-TerminusBold18X12")

    colorscanner = ColorSensor(INPUT_1)

   
    scan = 0
    bar1 = 0
    bar2 = 0
    bar3 = 0
    k = 0
    done = 0
    scan = 0

    scanner = colorscanner.reflected_light_intensity
    note.play_note("G1", 0.25, 100, Sound.PLAY_NO_WAIT_FOR_COMPLETE)
    while scan == 0:
        scanner = colorscanner.reflected_light_intensity
        robot.back_wheels.on(5)

        print("Scanner value:", scanner)  # Print the scanner value for debugging

        #9 = black 47 = white those number will probably chnage on test day
        if scanner == 9 or scanner == 47:
            scan = 1
            robot.back_wheels.stop()

        time.sleep(0.3)

        
 #0 means no color, 9 means black, and 47 means white
    while (done == 0):
        #spkr.play_note("F4", 0.25, 100, Sound.PLAY_NO_WAIT_FOR_COMPLETE)
        while (k < 3):
            scanner = colorscanner.reflected_light_intensity
            time.sleep(1)
    
            if (k==0):
                bar1 = colorscanner.reflected_light_intensity
                note.play_note("G3", 0.25, 100, Sound.PLAY_NO_WAIT_FOR_COMPLETE)
                time.sleep(1)
            if (k == 1):
                robot.forkLift.on_for_degrees(5,50)
                bar2 = colorscanner.reflected_light_intensity
                note.play_note("G3", 0.25, 100, Sound.PLAY_NO_WAIT_FOR_COMPLETE)
                time.sleep(1)
            if (k == 2):
                robot.forkLift.on_for_degrees(5,80)
                bar3 = colorscanner.reflected_light_intensity
                note.play_note("G3", 0.25, 100, Sound.PLAY_NO_WAIT_FOR_COMPLETE)
                done = 1
            k = k + 1
            time.sleep(1)


    if (bar1 >= 46):
        if (bar2 >= 46):
            if (bar3 >= 46):
                box = 1
            else:
                box = 4
        else:
            box = 2
    else:
        box = 3
            
    
    return box


   