# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        ALEX HUNG
#               ZAHRA ALMAILADY
#               RONNIE PEQUENO
#               ANZAL KHAN 
# Section:      580
# Assignment:   Lab 5.3
# Date:         28 September 2022

from math import *
#Start with inputs from user
sex = (input("Enter your sex (M/F): "))
age = float(input("Enter your age (years): "))
BMI = float(input("Enter your BMI: "))
meds = (input("Are you on medication for hypertension (Y/N)? "))
strd = (input("Are you on steroids (Y/N)? "))
smoke = (input("Do you smoke cigarettes (Y/N)? "))
#Plugging in inputs and assigned variables from it
if(sex == "m" or sex == "M"):
    sexC  = 0.0
if(sex == "f" or sex == "F"):
    sexC = 0.879    
if(meds == "y" or meds == "Y"):
    medsC = 1.222
if(meds == "n" or meds == "N"):
    medsC = 0.0
if(strd == "y" or strd == "Y"):
    strdC = 2.191
if(strd == "n" or strd == "N"):
    strdC = 0.0
if(smoke == "y" or smoke == "Y"):
    smkeC = .855
if(smoke == "n" or smoke == "N"):
    stillsmoke = input("Did you used to smoke (Y/N)? ") #displays only when needed
    if(stillsmoke == "y" or stillsmoke == "Y"):
        smkeC = -.218
    else:
        smkeC = 0.0
#Continuing inputs after smoke question
his = input("Do you have a family history of diabetes (Y/N)? ")
if(his == "n" or his== "N"):
    hisC = 0.0
if(his == "y" or his == "Y"):
    HisBoth = input("Both parent and sibling (Y/N)? ") #displays only when needed
    if(HisBoth == "y" or HisBoth == "Y"):
        hisC = 0.753
    else:
        hisC = 0.728
#calculating BMI weight to add up
if(BMI < 25):
    BMIC = 0.0
elif(BMI >= 25 and BMI < 27.50):
    BMIC = 0.699
elif(BMI >= 27.5 and BMI < 30):
    BMIC = 1.97
else:
    BMIC = 2.518
#equation used to calculate risk
N = 6.322 + sexC - (0.063 * age) - BMIC - medsC - strdC - smkeC - hisC #final equation adding them all up
risk = 100/(1+exp(N)) #plugging it in into bigger equation
#printing final percentage
print(f'Your risk of developing type-2 diabetes is {risk:.1f}%')
