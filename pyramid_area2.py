# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Anzal Khan
#               Colby Bielefeld
#               Elizabeth Cross
#               Ananya Mynam
# Section:      580
# Assignment:   Lab 6.12
# Date:         5 October 2022
#
from math import *
SL = float(input("Enter the side length in meters: "))
number_of_layers = int(input("Enter the number of layers: ")) #n in sequence

#Triangle Area
Triangle_Area = (sqrt(3)/4)*(SL*(number_of_layers))**2

#Lateral Area (sequence)
n = number_of_layers #number of terms
d = 3 #common difference
a = 3 #First term
side_area = (SL)**2
S_n = (n/2)*(2*a + (n-1)*d)*side_area #sum of first n terms

#Total
Total_Area = S_n + Triangle_Area

print(f'You need {Total_Area:.2f} m^2 of gold foil to cover the pyramid')




