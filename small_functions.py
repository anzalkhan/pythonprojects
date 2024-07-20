# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Anzal Khan
# Section:      580
# Assignment:   Lab 9.16
# Date:         2 November 2022
#
from math import *

#part a
def parta(r_sphere,r_hole):
    vSphere = (4/3)*pi*r_sphere**3
    hCap = r_sphere - sqrt((r_sphere)**2 - (r_hole)**2)
    vCylinder = pi*(r_hole**2)*2*(r_sphere - hCap)
    vCaps = (1/3)*pi*hCap*(3*(r_hole)**2 + hCap**2)
    vBead = vSphere - (vCaps + vCylinder)
    return vBead

#part b
def partb(n):
    summer = 0
    endlist = []
    solutionlist = []
    check = False #in order to check when summer is n
    i = 1 #start at 1
    while(i <= n and check == False):
        for j in range(i, n, 2):
            summer += j
            endlist.append(j)
            if(summer == n):#checking if sum works
                check = True
                solutionlist.append(endlist)
                break
            else:
                continue
        summer=0 #resetting the variables if starting at next odd
        endlist=[]
        check = False
        i += 2
    if len(solutionlist) > 1:
        return solutionlist[0]
    elif len(solutionlist) == 1:
        return solutionlist[0]
    else:
        return False
print(partb(75))

#part c
def partc_linecreator(x,char):
    if maxlength > len(x):
        whitespacename_oneside = (maxlength - len(x))/2
        if whitespacename_oneside != int(whitespacename_oneside):
            whitespacename_firstside = int(whitespacename_oneside)
            whitespacename_secondside = whitespacename_firstside + 1
            whitespacestring1 = (whitespacename_firstside)*' '
            whitespacestring2 = (whitespacename_secondside)*' '
            xline = f'{char}  ' + whitespacestring1 + x + whitespacestring2 + f'  {char}'
        else:
            whitespacestring = (int(whitespacename_oneside))*' '
            xline = f'{char}  ' + whitespacestring + x + whitespacestring + f'  {char}'
        return xline
    else:
        xline = f'{char}  ' + x + f'  {char}'
        return xline
def partc(char, name, company, email):
    global maxlength
    if len(name) >= len(company) and len(name) >= len(email):
        maxlength = len(name)
    elif len(company) >= len(name) and len(company) >= len(email):
        maxlength = len(company)
    elif len(email) >= len(name) and len(email) >= len(company):
        maxlength = len(email)
        
    firstlastline = (maxlength+6)*char
    nameline = partc_linecreator(name,char)
    companyline = partc_linecreator(company,char)
    emailline = partc_linecreator(email,char)
    return f'{firstlastline}\n{nameline}\n{companyline}\n{emailline}\n{firstlastline}'

#print(partc('@', 'Anzal Khan', 'Engineering', 'aak210014@tamu.edu'))

#part d
def partd(x):
    x.sort()
    xsorted = x
    minimum = xsorted[0]
    maximum = xsorted[-1]
    middleval = len(xsorted) / 2
    if middleval == int(middleval):
        median = (xsorted[int(middleval-1)] + xsorted[int(middleval)])/2
    else:
        middleval = int(middleval)
        median = xsorted[middleval]
    return (minimum, median, maximum)
#print(partd([1,5,3]))

#part e
def parte(times,distances):
    vlist = []
    element = 1
    i = 0
    while i < len(times) - 1:
        velocity = (distances[element] - distances[element - 1])/(times[element] - times[element - 1])
        vlist.append(velocity)
        element += 1
        i += 1
    return vlist
#print(parte([1,2,3],[3,6,9]))

def partf(numlist):
    a = 0
    b = 1
    goal = 2026
    ans = -1
    while a <= len(numlist) - 1:
        if ans == -1:
            while b <= len(numlist) - 1:
                if numlist[a] + numlist[b] == goal:
                    ans = numlist[a] * numlist[b]
                    break
                else:
                    b += 1
            if ans != -1:
                break
            else:
                a += 1
                b = a + 1
    if ans == -1:
        return False
    else:
        return ans
#print(partf([1,2,3,4,5,2024]))
            


        