# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Anzal Khan
# Section:      580
# Assignment:   Lab 6.14
# Date:         5 October 2022
#
from math import *
UserInput = int(input("Enter a positive integer: "))
print(f"The Juggler sequence starting at {UserInput} is:")
output_list = [UserInput]
x = UserInput
i = 0 #loop variable, used to count iterations
while x >= 1:
    if x == 1:
        break
    elif x > 0:
        if x % 2 == 0:
            x = floor(sqrt(x))
            output_list.append(x)
            i += 1
            continue
        elif x % 2 == 1:
            x = floor(x**(3/2))
            output_list.append(x)
            i += 1
            continue
y1 = str(output_list)
y2 = y1.replace("[","")
output_list_fixed = y2.replace("]","")
print(output_list_fixed)
print(f'It took {i} iterations to reach 1')
    
        
            