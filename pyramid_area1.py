# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Anzal Khan
#               Colby Bielefeld
#               Elizabeth Cross
#               Ananya Mynam
# Section:      580
# Assignment:   Lab 6.11
# Date:         5 October 2022
#
from math import *
n = float(input("Enter the side length in meters: "))
number_of_layers = int(input("Enter the number of layers: "))

Lateral_Area = 0 #placeholder for loop

Triangle_Area = (sqrt(3)/4)*(n*(number_of_layers))**2

#loop for the sides and side area 
for i in range(number_of_layers):
    side_area = (n)**2 * (3*(i + 1))
    Lateral_Area += side_area 
    
total_area = Triangle_Area + Lateral_Area 
print(f'You need {total_area:.2f} m^2 of gold foil to cover the pyramid')





