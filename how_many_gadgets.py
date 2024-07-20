# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Anzal Khan  
# Section:      580
# Assignment:   Lab 4.18
# Date:         21 September 2022
#
#input
x = int(input("Please enter a positive value for day: "))
if x < 1:
    print("You entered an invalid number!")
elif x < 11:
    Gadgets = 5 * x
    print(f'The total number of gadgets produced on day {x} is {Gadgets}')
elif x <= 60:
    DaysAfter10 = x - 10
    Gadgets2 = (50 * DaysAfter10) + (5 * 10)
    print(f'The total number of gadgets produced on day {x} is {Gadgets2}')
elif x > 60 and x < 100:
    DaysAfter60 = x - 60
    Trapezoid = .5 * (50 + (50 - DaysAfter60)) * DaysAfter60
    Gadgets3 = int(2550 + Trapezoid - .5 * DaysAfter60)
    print(f'The total number of gadgets produced on day {x} is {Gadgets3}')
elif x >= 101:
    Gadgets4 = 3730
    print(f'The total number of gadgets produced on day {x} is {Gadgets4}')