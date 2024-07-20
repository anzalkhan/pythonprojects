# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Anzal Khan
# Section:      580
# Assignment:   Lab 3.18
# Date:         10 September 2022
#
from math import *

def printresult(shape, side, area):
    '''Print the result of the calculation'''
    print(f'A {shape} with side {side:.2f} has area {area:.3f}')

# example function call:
# printresult(<string of shape name>, <float of side>, <float of area>)
# printresult('square', 2.236, 5)

#Equilateral triangle
side = float(input("Please enter the side length: "))
area = 0.5 * side * ((side/2) * sqrt(3))
printresult("triangle", side, area)
#Square
area = side**2
printresult("square", side, area)
#Pentagon
area = 0.25 * sqrt(5 * (5 + (2 * sqrt(5)))) * side**2
printresult("pentagon", side, area)
#Dodecagon
area = 3 * (2 + sqrt(3)) * side**2
printresult("dodecagon", side, area)
