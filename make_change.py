# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Anzal Khan
#               Nicholas Gutteridge
#               Matthew Johnson
#               Raja Momin   
# Section:      580
# Assignment:   Lab 4.13
# Date:         15 September 2022
#
Paid_float = 100 * float(input('How much did you pay? '))
Cost_float = 100 * float(input('How much did it cost? '))
Paid_int = int(Paid_float)
Cost_int = int(Cost_float)
x = Paid_int - Cost_int
y = x/100
#If statements
print(f'You received ${y:.2f} in change. That is...')
if x == 25:
        print('1 quarter')
if x == 35:
        print('1 quarter \n1 dime')
if x == 50:
        print('2 quarters')
if x == 75:
        print('3 quarters')
if x == 98:
        print('3 quarters \n2 dimes \n3 pennies')
if x == 65:
        print('2 quarters \n1 dime \n1 nickel')
if x == 5:
        print('1 nickel')
if x == 1:
        print('1 penny')
