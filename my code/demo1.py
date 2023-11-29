#!/usr/bin/env python3
#this needs to be at the top of every code when dealing with the robot

# 
# Project 4 demo 1
# File: demo1.py
# Date: 10/19/23
# By: Kaden Sawyer
# Section: 001
# Team: 29
# 
# ELECTRONIC SIGNATURE
# Kaden Sawyer
# 
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
# 
# Follows the tasks of the first demo
# 

# all the neccessary imports for now
from time import sleep
from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B,OUTPUT_C,SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.led import Leds
from ev3dev2.sensor import *
from ev3dev2.console import Console
from ev3dev2.sensor.lego import *
from ev3dev2.sound import Sound
from ev3dev2.display import *
import sys
import time

#distance
x = 0

#assign the motors to know which is the steering motor or the drive motor
backWheels = LargeMotor(OUTPUT_B)
frontWheels = LargeMotor(OUTPUT_A)
forkLift = MediumMotor(OUTPUT_C)
stop = False

#cirumferecne of wheel we used for back wheels is 175.93 mm
# I converted the measurment to cm 
wheelcircumference = 17.593
#rotations  = distance/wheel circumference

def debug_print(*args, **kwargs):
    #Print debug messages to stderr.

    #This shows up in the output panel in VS Code.
    
    print(*args, **kwargs, file=sys.stderr)


# large motors don't have a hold function so I made my own to lock the front wheels in place
#   when steering or not steering.
#def hold_steering_motor(check):
 #       while check == True:
  #          position = frontWheels.position
   #         frontWheels.on_to_position(0,position)

#distance has to be in cm
def moveForward(forward,speed):
    distance = x
    rotations = distance/wheelcircumference
    if forward == True:
        backWheels.polarity = 'normal'
        backWheels.on_for_rotations(speed,rotations)
    else:
        backWheels.polarity = 'inversed'
        backWheels.on_for_rotations(speed,rotations)



#turn mechanic move front motor to turn
def turn(right,degrees):
    #turn right
    if(right == True):
        frontWheels.on_for_degrees(5,degrees)
    else:
        #turn left
        frontWheels.on_for_degrees(5,-degrees)
    
    

# lift mechanic using a meduium motor
def lift():
    time.sleep(3)
    speed =3.5
    #lift goes up to pick up item
    forkLift.polarity = 'normal'
    forkLift.on_for_rotations(speed,0.3)
    time.sleep(3)
    #lift goes down to 
    forkLift.polarity = 'inversed'
    forkLift.on_for_rotations(speed,0.3)


def barcodeScanner():

    #display
    console = Console()
    console.set_font("Lat15-TerminusBold18X12")

    colorscanner = ColorSensor(INPUT_1)

    #0 means no color, 1 means black, and 6 means white
    scan = 0


    while(scan == 0 ):
        currentScan = colorscanner.reflected_light_intensity
        backWheels.on(20)
        if (currentScan > 4 and currentScan <15):
            scan = 1






#demo1 route
while not stop:
    x = float(input("\nEnter distance in cm "))
    forward = input("Enter \"y\" for forward and \"n\" for backward: ")
    speed = float(input("Enter the speed you want: "))

    if forward.capitalize() == "Y":
        moveForward(True, speed)
    else:
        moveForward(False, speed)
    
    checkTurn = input("\nEnter right or left for the turn")

    if checkTurn.capitalize() == "Right":
        turn(True,30)
    elif checkTurn.capitalize() == "Left":
        turn(False,30)
    
    x = float(input("\nEnter distance in cm "))
    forward = input("Enter \"y\" for forward and \"n\" for backward: ")
    speed = float(input("Enter the speed you want: "))
    if forward.capitalize() == "Y":
        moveForward(True, speed)
    else:
        moveForward(False, speed)

    useFork = input("Enter \"y\" to use forklift")
    if useFork.capitalize() == "Y":
        lift()


    check = input("\n\nContinue? Enter y/n: ")
    check = check.capitalize()

    if check == "N":
        stop = True
        print("Program concludes")
   
    
       

    
    
    


exit()



    


    
