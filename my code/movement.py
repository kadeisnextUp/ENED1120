#!/usr/bin/env python3
#this needs to be at the top of every code when dealing with the robot

# 
# Project 4 
# File: movement.py
# Date: 11/18/23
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
# all the code for the motors
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


# lift mechanic using a meduium motor
def lift(move):
    if move == False:
        time.sleep(2)
        speed =3.5
        #lift goes up to pick up item
        forkLift.polarity = 'normal'
        forkLift.on_for_degrees(speed,100)
        
        time.sleep(4)
        #lift goes down to 
        forkLift.polarity = 'inversed'
        forkLift.on_for_degrees(speed,90)
    else:
        forkLift.polarity = 'normal'
        forkLift.on_for_degrees(5,10)
        
        
        
        

        
    

#distance has to be in cm
def moveForward(forward,speed):
    lift(True)
    distance = x
    rotations = distance/wheelcircumference
    if forward == True:
        backWheels.polarity = 'normal'
        frontWheels.on_for_degrees(0,0)
        backWheels.on_for_rotations(speed,rotations)
    else:
        backWheels.polarity = 'inversed'
        frontWheels.on_for_degrees(0,0)
        backWheels.on_for_rotations(speed,rotations)



#turn mechanic move front motor to turn
def turn(right,degrees):
    #turn right
    if(right == True):
        frontWheels.on_for_degrees(5,degrees)
    else:
        #turn left
        frontWheels.on_for_degrees(5,-degrees)
    
    





    


lift(True)



"""
while not stop:
    x = float(input("\nEnter distance in cm "))
    forward = input("Enter \"y\" for forward and \"n\" for backward: ")
    speed = float(input("Enter the speed you want: "))

    moveForward(forward.capitalize() == "Y",speed)
    
    checkTurn = input("\nEnter right or left for the turn")

    if checkTurn.capitalize() == "Right":
        turn(True,30)
    elif checkTurn.capitalize() == "Left":
        turn(False,30)
    
    x = float(input("\nEnter distance in cm "))
    forward = input("Enter \"y\" for forward and \"n\" for backward: ")
    speed = float(input("Enter the speed you want: "))
    
    moveForward(forward.capitalize() == "Y",speed)


    useFork = input("Enter \"y\" to use forklift")
    if useFork.capitalize() == "Y":
        lift()


    check = input("\n\nContinue? Enter y/n: ")
    if check.capitalize() == "N":
        stop = True
        print("Program concludes")
        break
   


exit()
"""


    


    
