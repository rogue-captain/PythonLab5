# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 19:02:14 2024

@author: Sully
"""

##############################################################################
# Name: Suleyman Erkan-Rijos | CST-121 | Y01

# Program: Lab 5

# Due Date: 10/18/2024
#
# Program Description: 
    
#A
#This program collects 3 integer inputs from user, checks for correct data 
#value and type then returns their sum, product, average, min, max. 

#B
#This program collects height and radius values from user then returns the 
#surface area of a cone and its volume. 

# 
#
# Inputs: A: 3 user number inputs. 
#         B: 2 user number inputs.
#
# Outputs: A: sum, product, mean, min, max.
#          B: Cone surface area and volume.
##############################################################################

import statistics #import stats module
import math # import math module

##################################### A #######################################

################################ VARIABLES ####################################

numbers = [] # array to hold 3 integers being input by user

################################ VARIABLES ####################################
def user_input_sequence():
    
    while len(numbers) < 3: #iterate loop 3 times for 3 inputs
    
        #try / except to act as a input checker for non numericals        
            try:
                num = int(input("Please enter a number ranging from 1 - 100. "))
                
                if num >= 1 or num >= 100: # check for valid number range
                   numbers.append(num) #add to list / array
                                      
                else:
                    print("2nd please enter a number ranging from 1 - 100.")
            
            #except value error in case user enters a letter
            except ValueError:
                
                print("Please enter only a NUMBER ranging from 1 - 100")
                print() #spacer line
                                
    print("\n1You have entered", numbers) 
    
    print() #spacer line

################################ FUNCTIONS ####################################

# Function to calculate and print the sum of the numbers
def calc_sum():
    theSum = sum(numbers)
    print(f"{'Sum:':>10} {theSum:>10}")
    print("*"*32)

# Function to calculate and print the maximum value in the list
def max_val():
    theMax = max(numbers)
    print(f"{'Max:':>10} {theMax:>10}")
    print("*"*32)

# Function to calculate and print the minimum value in the list
def min_val():
    theMin = min(numbers)
    print(f"{'Min:':>10} {theMin:>10}")
    print("*"*32)

# Function to calculate and print the average of the numbers
def average():
    theAverage = statistics.mean(numbers)
    print(f"{'Average:':>10} {theAverage:>10.2f}")
    print("*"*32)

# Function to calculate and print the product of the numbers
def product():
    theProduct = 1
    for num in numbers:
        theProduct *= num  # Multiply each number in the list to get the product
    print(f"{'Product:':>10} {theProduct:>10}")
    print("*"*32)
        
   
#function to call all functions
def main():
    user_input_sequence()
    calc_sum()
    max_val()
    min_val()
    average()
    product()
    print() #spacer line
    
    
    
main() # call main function



##################################### A #######################################



##################################### B #######################################



#define function with 2 parameters passed
def coneCalculations(radius, height):
    
    theVolume = (1/3) * math.pi * ((radius**2) * height) # calculates cone volume
    
    #calculates the surface area
    theSurfaceArea = math.pi * radius * (radius + math.sqrt(radius**2 + height**2))
    
    return theVolume, theSurfaceArea #returns the value of variables to the function.


def main2():
    
    #input variables to collect radius and height
    radius = float(input("Please enter a numerical value for the radius. "))
    height = float(input("\nPlease enter a numerical value for the height. "))
    
    print() #spacer line
    
    #unpack values from function
    theVolume, theSurfaceArea = coneCalculations(radius, height)
    
    print(f"{'Attributes of the Cone':<23} {'Value':>8}")
    print("*"*32)
    print(f"{'Volume = ':>23} {theVolume:>9.2f}")
    print(f"{'Surface Area = ':>23} {theSurfaceArea:>9.2f}")
    
    
    
##################################### B #######################################

main2()
  