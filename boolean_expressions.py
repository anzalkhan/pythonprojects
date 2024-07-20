# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Anzal Khan
#               Nicholas Gutteridge
#               Matthew Johnson
#               Raja Momin   
# Section:      580
# Assignment:   Lab 4.15
# Date:         15 September 2022
#
############ Part A ############  
a = input("Enter True or False for a: ")
b = input("Enter True or False for b: ")
c = input("Enter True or False for c: ")
if a == "T":
    a = True
elif a == "True":
    a = True
elif a == "t":
    a = True
elif a == "F":
    a = False
elif a == "False":
    a = False
elif a == "f":
    a = False
if b == "T":
    b = True
elif b == "True":
    b = True
elif b == "t":
    b = True
elif b == "F":
    b = False
elif b == "False":
    b = False
elif b == "f":
    b = False
if c == "T":
    c = True
elif c == "True":
    c = True
elif c == "t":
    c = True
elif c == "F":
    c = False
elif c == "False":
    c = False
elif c == "f":
    c = False
############ Part B ############ 
print("a and b and c:", a and b and c)
print("a or b or c:", a or b or c)
############ Part C ############
XOR = (a and not b) or (not a and b)
print("XOR:", XOR)
odd = (a and b and c) or ((((a and not b) or (not a and b)) and not c) or (((a and not c) or (not a and c)) and not b) or (((b and not c) or (not b and c)) and not a))
print("Odd number:", odd)
############ Part D ############
complex1 = (not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b)
complex2 = (not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b and c) or (a and ((b and not c) or (not b))))
simple1 = (not b or (not a and not c))
simple2 = (a or (not b and c))
print("Complex 1:", complex1)
print("Complex 2:", complex2)
print("Simple 1:", simple1)
print("Simple 2:", simple2)