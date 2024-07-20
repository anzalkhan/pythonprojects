# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Anzal Khan  
# Section:      580
# Assignment:   Lab 4.19
# Date:         21 September 2022
#
#inputs
from sympy import *
A = float(input("Please enter the coefficient A: "))

B = float(input("Please enter the coefficient B: "))

C = float(input("Please enter the coefficient C: "))
#functions
x = symbols("x")
f1 = B * x + C
f2 = A * x**2 + B * x + C
Disc = B**2 - 4*A*C
#if-elif-else
if A == 0 and B == 0:
    print("You entered an invalid combination of coefficients!")
elif A == 0:
    f1solnlist = solve(f1)
    f1solnfloat = float(f1solnlist[0])
    print(f'The root is x = {f1solnfloat:.1f}')
elif Disc > 0:
    f2solnlist = solve(f2)
    f2soln1 = float(f2solnlist[1])
    f2soln2 = float(f2solnlist[0])
    print(f'The roots are x = {f2soln1:.1f} and x = {f2soln2:.1f}')
elif Disc == 0:
    f2solnlist = solve(f2)
    f2solnstr = str(f2solnlist[0])
    f2solnfloat = float(f2solnstr)
    print(f'The root is x = {f2solnfloat:.1f}')
elif Disc < 0:
    f3real = (-1 * B)/(2 * A)
    f3imaginary = str(sqrt(Disc)/2)
    f3imaginaryfixed = f3imaginary.replace("*I", "i")
    f3real = float(f3real)
    print(f'The roots are x = {f3real} + {f3imaginaryfixed} and x = {f3real} - {f3imaginaryfixed}')
