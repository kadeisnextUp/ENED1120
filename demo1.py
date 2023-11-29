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
# Follows the tasks of the first status update
# 

# all the neccessary imports for now
from time import sleep
from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B,OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.led import Leds
import sys
import time

#distance
x = float(input("Enter distance in cm "))

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


#distance was in cm
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


#demo1 route
while not stop:
    #moveForward(True,50)
    #turn(True,25)
    #x = float(input("Enter distance to go forward in cm "))
    #moveForward(True,20)
    #turn(False,25)
    #x = float(input("Enter distance to go forward in cm "))
    #moveForward(True,50)
    #lift()
    #x = float(input("Enter distance to go backward in cm "))
    #moveForward(False,50)
    #turn(False,25)
    #x = float(input("Enter distance to go forward in cm "))
    #moveForward(True,35)
    moveForward(True,70)
    turn(True,30)
    x = float(input("Enter distance to go forward in cm "))
    moveForward(True,70)
    turn(False,30)
    x = float(input("Enter distance to go forward in cm "))
    moveForward(True,70)
    x = float(input("Enter distance to go forward in cm "))
    moveForward(False,70)
    turn(False,30)
    x = float(input("Enter distance to go forward in cm "))
    moveForward(False,50)
    turn(True,30)
    x = float(input("Enter distance to go forward in cm "))
    moveForward(True,60)

    check = input("Continue enter y/n ")
    check = check.capitalize()
    if check == "N":
        stop = True
        print("Program concludes")


exit()



    


    
