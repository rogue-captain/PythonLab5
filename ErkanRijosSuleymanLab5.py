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
#This program 

#B


# 
#
# Inputs: A: 3 user number inputs. 
#         B: 
#
# Outputs: A: 
#          B: 
##############################################################################

import statistics

##################################### A #######################################

################################ VARIABLES ####################################

numbers = [] # array to hold 3 integers being input by user

################################ VARIABLES ####################################
def user_input_sequence():
    
    while len(numbers) < 3: #iterate loop 3 times for 3 inputs
        #try / except to act as a input checker for non numericals        
            try:
                num = int(input("1st Please enter a number ranging from 1 - 100. "))
                
                if num >= 1 or num >= 100:
                   numbers.append(num) # check for valid number range
                   #break # exit if input is valid
                   
                else:
                    print("2nd please enter a number ranging from 1 - 100.")
            
            except ValueError:
                print("Please enter only a NUMBER ranging from 1 - 100")
                print() #spacer line
                                
    print("You have entered", numbers) 

def calc_sum():
    theSum = sum(numbers)
    print("Sum: ",theSum)
    
def max_val():
    theMax = max(numbers)
    print("Max: ", theMax)
    
def min_val():
    theMin = min(numbers)
    print("Min: ", theMin)
    
def average():
    theAverage = statistics.mean(numbers)
    print("Average: ", theAverage)
    
def product():
    theProduct = 1
    
    for num in numbers:
        theProduct *= num
        
    print("Product: ", theProduct)
    

def main():
    user_input_sequence()
    calc_sum()
    max_val()
    min_val()
    average()
    product()
    
    
    
main()

##################################### A #######################################



##################################### B #######################################

################################ VARIABLES ####################################

radius = int(input("Please enter a numerical value for the radius."))
height = int(input("Please enter a numerical value for the height."))

################################ VARIABLES ####################################

def main2():
##################################### B #######################################  