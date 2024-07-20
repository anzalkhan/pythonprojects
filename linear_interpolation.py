# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Miranda Izaguirre-Rangel
#               Anzal Khan
#               Chase Dellinger
#               Hunter Phillips
# Section:      580
# Assignment:   Lab 2.8
# Date:         02 09 2022
#Part 1
from sympy import *
from math import *
Time1_minutes = 10
Time2_minutes = 55
Distance1_km = 2026
Distance2_km = 23026
x = symbols("TimeInterested_minutes")
DistanceDesired_km = ((Distance2_km - Distance1_km)/(Time2_minutes - Time1_minutes)) * (x - Time1_minutes) + Distance1_km
#find distance from houston at 25 minutes
print("Part 1:")
print("For t = 25 minutes, the position p =", float(DistanceDesired_km.subs(x, 25)), "kilometers.")
#Part 2
Time1_minutes = 10
Time2_minutes = 55
Distance1_km = 2026
Distance2_km = 23026
#find circumference to find full orbit
Full_Orbit = 2 * pi * 6745
x = symbols("TimeInterested_minutes")
DistanceDesired_km = ((Distance2_km - Distance1_km)/(Time2_minutes - Time1_minutes)) * (x - Time1_minutes) + Distance1_km
#find the remainder from dividing the full distance traveled with the full orbit distance in order to find displacement from Houston.
Distance_From_Houston = float(DistanceDesired_km.subs(x, 300)) % Full_Orbit
print("Part 2:")
print ("For t = 300 minutes, the position p =", Distance_From_Houston, "kilometers.")