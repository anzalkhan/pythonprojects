# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Anzal Khan
#               Travis Mason
#               Nicholas Gutteridge
#               Layne Purkerson
# Section:      580
# Assignment:   Lab 3.16
# Date:         8 September 2022
#
#Input section
#Linear interpolation formula: xyz1 = xyz0 + ((xyz2 – xyz0) / (t2 – t0)) * (t1 – t0)
t1Input = input("Enter time 1: ")
x1Input = input("Enter the x position of the object at time 1: ")
y1Input = input("Enter the y position of the object at time 1: ")
z1Input = input("Enter the z position of the object at time 1: ")
t5Input = input("Enter time 2: ")
x5Input = input("Enter the x position of the object at time 2: ")
y5Input = input("Enter the y position of the object at time 2: ")
z5Input = input("Enter the z position of the object at time 2: ")
#Assigning variables for output
#t1
t1Float = float(t1Input)
t1Str = f'{t1Float:.2f}'
x1Float = float(x1Input)
x1Str = f'{x1Float:.3f}'
y1Float = float(y1Input)
y1Str = f'{y1Float:.3f}'
z1Float = float(z1Input)
z1Str = f'{z1Float:.3f}'
t1Position = f'({x1Str}, {y1Str}, {z1Str})'
#t5 (user input t2)
t5Float = float(t5Input)
t5Str = f'{t5Float:.2f}'
x5Float = float(x5Input)
x5Str = f'{x5Float:.3f}'
y5Float = float(y5Input)
y5Str = f'{y5Float:.3f}'
z5Float = float(z5Input)
z5Str = f'{z5Float:.3f}'
t5Position = f'({x5Str}, {y5Str}, {z5Str})'
#t3
t3Float = (t1Float + t5Float) / 2
x3Float = x1Float + ((x5Float - x1Float)/(t5Float - t1Float)) * (t3Float - t1Float)
y3Float = y1Float + ((y5Float - y1Float)/(t5Float - t1Float)) * (t3Float - t1Float)
z3Float = z1Float + ((z5Float - z1Float)/(t5Float - t1Float)) * (t3Float - t1Float)
t3Str = f'{t3Float:.2f}'
x3Str = f'{x3Float:.3f}'
y3Str = f'{y3Float:.3f}'
z3Str = f'{z3Float:.3f}'
t3Position = f'({x3Str}, {y3Str}, {z3Str})'
#t2
t2Float = (t1Float + t3Float) / 2
x2Float = x1Float + ((x5Float - x1Float)/(t5Float - t1Float)) * (t2Float - t1Float)
y2Float = y1Float + ((y5Float - y1Float)/(t5Float - t1Float)) * (t2Float - t1Float)
z2Float = z1Float + ((z5Float - z1Float)/(t5Float - t1Float)) * (t2Float - t1Float)
t2Str = f'{t2Float:.2f}'
x2Str = f'{x2Float:.3f}'
y2Str = f'{y2Float:.3f}'
z2Str = f'{z2Float:.3f}'
t2Position = f'({x2Str}, {y2Str}, {z2Str})'
#t4
t4Float = (t3Float + t5Float) / 2
x4Float = x1Float + ((x5Float - x1Float)/(t5Float - t1Float)) * (t4Float - t1Float)
y4Float = y1Float + ((y5Float - y1Float)/(t5Float - t1Float)) * (t4Float - t1Float)
z4Float = z1Float + ((z5Float - z1Float)/(t5Float - t1Float)) * (t4Float - t1Float)
t4Str = f'{t4Float:.2f}'
x4Str = f'{x4Float:.3f}'
y4Str = f'{y4Float:.3f}'
z4Str = f'{z4Float:.3f}'
t4Position = f'({x4Str}, {y4Str}, {z4Str})'
#Output
print("At time", t1Str, "seconds the object is at", t1Position)
print("At time", t2Str, "seconds the object is at", t2Position)
print("At time", t3Str, "seconds the object is at", t3Position)
print("At time", t4Str, "seconds the object is at", t4Position)
print("At time", t5Str, "seconds the object is at", t5Position)

