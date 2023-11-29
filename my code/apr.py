#!/usr/bin/env python3

# 
# Activity Project 4
# File: apr.py
# Date: 11/17/23
# By: Kaden Sawyer
# Section: 001
# Team: 023
# 
# ELECTRONIC SIGNATURE
# Kaden Sawyer
# 
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
# 
# attempt to make the robot autonomus 
# 

from ev3dev2.wheel import *
from ev3dev2.motor import *
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
import math
import os
import time
import movement



"""
    A class that will track the robot's positon at all times
    102 by 114
    home A(6,-6), home B(102,-6), home C(6, 114), home D(102,114)

"""

#inches to cm is in*2.54
class APR():
    #initialize values / sensors
    #OUTPUT_B,OUTPUT_A,INPUT_2,OUTPUT_C
    def __init__(self, back_wheels_motor_port, front_wheels_motor_port,gyro_port,forkPort):
        self.back_wheels = LargeMotor(back_wheels_motor_port)
        self.back_wheels.polarity = 'normal'
        self.front_wheels = LargeMotor(front_wheels_motor_port)
        self.front_wheels.polarity = 'normal'
        self.forkLift = MediumMotor(forkPort)
        self.color_sensor = ColorSensor()
        self.gyro_sensor = GyroSensor(gyro_port)
        self.x_position = 0  # Initial x position
        self.y_position = 0  # Initial y position
        self.face_postion = 0 #positon the robot needs to face a box
        self.wheel_circumference = 17.593 #cm
    
    #calibrates gyro sensor and rotations are set to zero. you only have to call this once
    def calibrateGyro(self):
        self.gyro_sensor.calibrate()
        self.gyro_sensor.reset()

    #makes the APR location with the setup info
    def apr_locator(self,x = 0,y=0,face=0):
        self.x_position = x
        self.y_position = y
        self.face_positon = face



    """Calculating distance

    This should calculate the distance between two points using the coordinates given in the project
        description all measurements are given in inches and I use cm in all my programs
        so every inch value would be multiplied by 2.54 to convert.
    """
    def CalculateDistance(self, x1,y1,x2,y2):
        return((math.sqrt((x2-x1)**2+(y2-y1)**2)))*2.54
    

    #This calculates the face value the APR needs to have to face the target point
    
    def CalculateAngle(self,x1,y1,x2,y2):
        y_Difference = y2-y1
        x_Difference = x2-x1
        if x_Difference == 0:
            if y2>y1:
                return 0
            return 180
        if y_Difference == 0:
            if x2>x1:
                return 90
            return -90
        return math.atan(y_Difference/x_Difference)
    
        
    
    #CalculateMotorRotations returns the motor rotation value based on the distance given
    def CalculateMotorRotations(self, distance):
        return distance/self.wheel_circumference
    

    """
    TurnToAngle turns to the inputted angle
    The angle of the gyro sensor is printed to the screen
    True = right turn False = left turn
    """
    def TurnToAngle(self,angle,direction):
        # prepares to turn
        time.sleep(.1) 
        INITIAL_TURN_SPEED = 15
        CORRECT_TURN_SPEED = 10

        if direction:
            #Turn left while the angle is less than the inputted angle
            while self.gyro_sensor.angle<angle:
                self.front_wheels.polarity = 'inversed' 
                self.front_wheels.on(INITIAL_TURN_SPEED)

                

            #Stop the motor to get more accurate results
            self.front_wheels.stop()
            time.sleep(0.25)

            #Turn right while the angle is greater than the inputted angle
            while self.gyro_sensor.angle>angle:
                self.front_wheels.polarity = 'normal' 
                self.front_wheels.on(CORRECT_TURN_SPEED)
                

        else:
             #Turn left while the angle is less than the inputted angle
            while self.gyro_sensor.angle<angle:
                self.front_wheels.polarity = 'inversed' 
                self.front_wheels.on(INITIAL_TURN_SPEED)
                

            #Stop the motor to get more accurate results
            self.front_wheels.stop()
            time.sleep(0.25)

            #Turn right while the angle is greater than the inputted angle
            while self.gyro_sensor.angle>angle:
                self.front_wheels.polarity = 'normal' 
                self.front_wheels.on(CORRECT_TURN_SPEED)

        #Stop the motors to get more accurate results
        self.front_wheels.stop()
        time.sleep(.1)
        
        #Display the gyro's angle to the screen
        print("{0:.2f} degrees".format(self.gyro_sensor.angle))
        

    
    """
    True = turning towards the box and False = turning away from the box
    the array contains (x and y position of box center)
    """
    def HallTurn(self, direction, container):
        INITIAL_TURN_SPEED = 15
        CORRECTION_TURN_SPEED = 10
        y_cont_pos = container[1]
        #assign the steering wheels
        steering = self.front_wheels

        """ 
        Create a modifier for the direction based on whether the APR is turning 
            into the container or away from it
        positive directionMod = turn in, negative directionMod = turn out
        """
        if direction:
            directionMod = 1
        else:
            directionMod = -1

        # Determine the direction to turn based on the container's y-value
        #   -dir is turn right, +dir is turn left
        if y_cont_pos == 13*2.54:
            dir = -1
        elif y_cont_pos == 35*2.54:
            dir = 1
        elif y_cont_pos == 37*2.54:
            dir = -1
        elif y_cont_pos == 59*2.54:
            dir = 1
        elif y_cont_pos == 61*2.54:
            dir = -1
        elif y_cont_pos == 83*2.54:
            dir = 1
        elif y_cont_pos == 85*2.54:
            dir = -1
        elif y_cont_pos == 107*2.54:
            dir = 1

        # Change the direction of the turn based on its  "direction" parameter
        dir *= directionMod

        # Determine what angle to turn to
        TURN_ANGLE = self.gyro_sensor.angle + dir*90

        #Turn to towards or away from the box
        if dir > 0:     # If turning left,
            while self.gyro_sensor < TURN_ANGLE:     # Loop while the angle is less than calculated angle
                # Set the motor to run at the speed multiplied by the modifier
                # If the modifier is -, then the robot will turn away from the container
                # If the modifier is +, then the robot will turn towards the container
                steering.on(INITIAL_TURN_SPEED*directionMod)
        else:       # Otherwise, the robot is turning right
            while self.gyro_sensor > TURN_ANGLE:     # Loop while the angle is less than calculated angle
                # Set the motor to run at the speed multiplied by the modifier
                # If the modifier is -, then the robot will turn away from the container
                # If the modifier is +, then the robot will turn towards the container
                steering.on(INITIAL_TURN_SPEED*directionMod)
        
        # Stop running the motor
        steering.stop()


    
    """
    moveDistance moves the APR a given distance at a specified speed.
    Distance is measured in cm and speed is a percentage out of 100.

    This function is designed to correct the APR's x orientation based on the gyro sensor's angle.
    The motor rotation count of the left motor is printed to the screen for debugging purposes.
    """
    def moveDistance(self, DISTANCE,SPEED = 50):
        ROTATIONS = DISTANCE/self.wheel_circumference    

        # Prepare updater variables to enter loop
        frontMotorOffset = self.front_wheels.position
        backMotorOffset = self.back_wheels.position
        frontMotorPosition = self.front_wheels.position - frontMotorOffset
        backMotorPosition = self.back_wheels.position - backMotorOffset

        gyroAngleOffset = self.gyro_sensor.angle
        gyroAngle = self.gyro_sensor.angle - gyroAngleOffset


        # Loop until the distance has been reached
        while abs(backMotorPosition) < ROTATIONS:
            # Reset motor speeds to the inputted speed
            backMotorSpeed = SPEED

            # Update accessor variables
            gyroAngle = self.gyro_sensor.angle  #Negative when turning left, positive when turning right
            frontMotorPosition = self.front_wheels.position - frontMotorOffset
            backMotorPosition = self.back_wheels.position - backMotorOffset

            # Adjust motor speed by the gyro's angle
            backMotorSpeed -= gyroAngle - gyroAngleOffset

            # Disallow speeds larger than the given speed
            if backMotorSpeed>SPEED:
                backMotorSpeed = SPEED
            if backMotorSpeed < -SPEED:
                backMotorSpeed = -SPEED


            # Set motors to calculated speed
            self.front_wheels.on(0)
            self.back_wheels.on(backMotorSpeed)

            # for debugging
            #print("{0:.2f} P=".format(motorLPosition))
            #time.sleep(0.001)

        #End
        self.back_wheels.stop()
        self.front_wheels.stop()

        # Update the position variables based on the orientaiton of the APR
        if self.gyro_sensor.angle <10 and self.gyro_sensor.angle>-10:
            self.y_position += DISTANCE

        elif self.gyro_sensor.angle <100 and self.gyro_sensor.angle>80:
            self.x_position += DISTANCE

        elif self.gyro_sensor.angle<190 and self.gyro_sensor.angle>170:
            self.y_position -= DISTANCE

        else:
            self.x_position -= DISTANCE




    

    
    #Make the APR drive to a point    
    def DriveToPoint(self, x, y, reverse = False):
        SPEED = 50

        # Turn towards the point
        angle = self.CalculateAngle(self.x_position, self.y_position, x, y)
        print("{0:.2f} degrees".format(angle))
        self.TurnToAngle(angle)

        # Drive to the point
        distance = self.CalculateDistance(self.x_position, self.y_position, x, y)
        self.moveDistance(distance, SPEED)

    
    """
    Drives the robot to the inputted container
    """
    def DriveToContainer(self, Container):
        SPEED = 50
        target_x = Container[0]
        target_y = Container[1]

        # Drive to the container
        #   Drive to the hall
        self.DriveToPoint(self.x_position, target_y)
        #   Drive to the Container
        self.DriveToPoint(target_x, target_y)

    """
    Drives the robot to the inputted center
    """
    def DriveToCenter(self, Center):
        SPEED = 50
        initial_x = self.x_position
        target_x = Center[0]
        target_y = Center[1]

        # Drive to the container
        #   Drive to the end of the hall
        self.DriveToPoint(target_x, self.y_position)


    def update_position(self, delta_x, delta_y):
        # Update the position based on the movement
        self.x_position += delta_x
        self.y_position += delta_y

    def get_position(self):
        # Return the current position
        return self.x_position, self.y_position
