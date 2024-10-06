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
################################ VARIABLES ####################################

#num1 = int(input("please enter a number from 1 - 100"))
#num2 = int(input("please enter a number from 1 - 100"))
#num3 = int(input("please enter a number from 1 - 100"))

numbers = [0,2]

for i in range(3):
    num = int(input("please enter a numbers ranging from 1 - 100."))
    
    while num < 1 or num > 100:
        print("please enter an integer from 1 - 100.")
        num = int(input("please enter a numbers ranging from 1 - 100."))
        
    numbers.append(num)
    print("You have entered", numbers)

################################ VARIABLES ####################################


def sum():
    numSum = num1 + num2 + num3
    print("Sum: ", numSum)
    
def max_val():
    numbers = 
    
def min_val():
    
def average():
    
def product():

def main():
    