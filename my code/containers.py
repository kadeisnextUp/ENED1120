#!/usr/bin/env python3

# 
# Activity Project 4
# File: containers.py
# Date: 11/16/23
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
#   this has the coordinates for every container and the distance to drive to it
#   remeber all the values are in inches and all the programs operate in cm



class Containers():
    A1 = [[9,13],[15,13],[21,13],[27,13],[33,13],[39,13],
          [9,35],[15,35],[21,35],[27,35],[33,35],[39,35]]
    A2 = [[9,37],[15,37],[21,37],[27,37],[33,37],[39,37],
          [9,59],[15,59],[21,59],[27,59],[33,59],[39,59]]
    
    B1 = [[69,13],[75,13],[81,13],[87,13],[93,13],[99,13],
          [69,35],[75,35],[81,35],[87,35],[93,35],[99,35]]
    B2 = [[69,37],[75,37],[81,37],[87,37],[93,37],[99,37],
          [69,59],[75,59],[81,59],[87,59],[93,59],[99,59]]
    
    C1 = [[9,61],[15,61],[21,61],[27,61],[33,61],[39,61],
          [9,83],[15,83],[21,83],[27,83],[33,83],[39,83]]
    C2 = [[9,85],[15,85],[21,85],[27,85],[33,85],[39,85],
          [9,107],[15,107],[21,107],[27,107],[33,107],[39,107]]
    
    D1 = [[69,61],[75,61],[81,61],[87,61],[93,61],[99,61],
          [69,83],[75,83],[81,83],[87,83],[93,83],[99,83]]
    D2 = [[69,85],[75,85],[81,85],[87,85],[93,85],[99,85],
          [69,107],[75,107],[81,107],[87,107],[93,107],[99,107]]
    
    containerSize = 4 * 2.54
    robotSize = 11.56 * 2.54
    distanceBetweenRobotAndContainer = 0.5 *2.54
    
    distanceBetweenCenters = containerSize/2 + robotSize/2 + distanceBetweenRobotAndContainer

# Contants for the Center Locations
homeAx = 0
homeAy = 0
    
fulfillmentCenterBx = 100 * 2.54
fulfillmentCenterBy = 0

fulfillmentCenterCx = 0
fulfillmentCenterCy = 100 * 2.54

fulfillmentCenterDx = 100 * 2.54
fulfillmentCenterDy = 100 * 2.54

AbHALLy = 21*2.54
