# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Anzal Khan
# Section:      580
# Assignment:   Lab 5.4
# Date:         28 September 2022
#
#Start with the input from the user (the desired excess temperature)
ET_Desired = float(input("Enter the excess temperature: "))

#List the points that are given from the boiling graph
#A: (1.3, 1000)
#B: (5, 7000)
#C: (30, 1.5E6)
#D: (120, 2.5E4)
#E: (1200, 1.5E6)

#Define variables from the points
ET_A = 1.3 #ET is excess temperature, label for the x axis
SHF_A = 1000 #SHF is surface heat flux, label for the y axis
ET_B = 5
SHF_B = 7000
ET_C = 30
SHF_C = 1.5e6
ET_D = 120
SHF_D = 2.5e4
ET_E = 1200
SHF_E = 1.5e6

#Define interpolation formula
#Since the graph is logarithmical, a new linear interpolation formula is needed
#y = y0*(x/x0)**m
#m = (log10(y1/y0))/(log10(x1/x0))
#x0,x1,y0,y1 can be substituted as needed by data from the points given

#Create if-elif-else statements based on what stage of the graph EF_Desired falls in
#There are 4 different line segments, so 4 areas of interpolation

#interpolation formula for A-B
from math import *
mAB = (log10(SHF_B/SHF_A))/(log10(ET_B/ET_A))
yAB = SHF_A * (ET_Desired/ET_A)**mAB

#interpolation formula for B-C
mBC = (log10(SHF_C/SHF_B))/(log10(ET_C/ET_B))
yBC = SHF_B * (ET_Desired/ET_B)**mBC

#interpolation formula for C-D
mCD = (log10(SHF_D/SHF_C))/(log10(ET_D/ET_C))
yCD = SHF_C * (ET_Desired/ET_C)**mCD

#interpolation formula for D-E
mDE = (log10(SHF_E/SHF_D))/(log10(ET_E/ET_D))
yDE = SHF_D * (ET_Desired/ET_D)**mDE

#Now define if-elif-else statements

#if-elif-else statements for A-B
from sympy import *
SHF_Desired = symbols("SHF_Desired")
if ET_Desired < ET_A: #There is no data, so print an error
    print("Surface heat flux is not available") 
elif ET_Desired == ET_A:
    SHF_Desired = SHF_A #This is an edge case if the input falls on a point
    print(f'The surface heat flux is approximately {SHF_Desired} W/m^2')
elif ET_Desired > ET_A and ET_Desired < ET_B:
    SHF_Desired = round(yAB)
    print(f'The surface heat flux is approximately {SHF_Desired} W/m^2')
    
#if-elif-else statements for B-C
elif ET_Desired == ET_B:
    SHF_Desired = SHF_B
    print(f'The surface heat flux is approximately {SHF_Desired} W/m^2')
elif ET_Desired > ET_B and ET_Desired < ET_C:
    SHF_Desired = round(yBC)
    print(f'The surface heat flux is approximately {SHF_Desired} W/m^2')

#if-elif-else statements for C-D
elif ET_Desired == ET_C:
    SHF_Desired = SHF_C
    print(f'The surface heat flux is approximately {SHF_Desired} W/m^2')
elif ET_Desired > ET_C and ET_Desired < ET_D:
    SHF_Desired = round(yCD)
    print(f'The surface heat flux is approximately {SHF_Desired} W/m^2')
    
#if-elif-else statements for D-E
elif ET_Desired == ET_D:
    SHF_Desired = SHF_D
    print(f'The surface heat flux is approximately {SHF_Desired} W/m^2')
elif ET_Desired > ET_D and ET_Desired < ET_E:
    SHF_Desired = round(yDE)
    print(f'The surface heat flux is approximately {SHF_Desired} W/m^2')
elif ET_Desired > ET_E: #There is no data, so print an error
    print("Surface heat flux is not available") 
    