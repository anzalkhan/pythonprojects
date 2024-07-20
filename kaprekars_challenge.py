# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Anzal Khan
# Section:      580
# Assignment:   Lab 7.29
# Date:         17 October 2022
#
count = 0
countList = [1]
n = 1
DescInt = 1000
AscInt = 1
OutputList = [0]
def Convert(string):
    N = []
    N[:0] = string
    return N
while n <= 9999:
    NewNum = DescInt - AscInt
    if NewNum == 0:
        countList.append(1)
    else:
        while NewNum != 6174:
            x = str(NewNum)
            if len(x) == 3:
                x = "0" + (x)
            elif len(x) == 2:
                x = "00" + (x)
            elif len(x) == 1:
                x = "000" + (x)
            else:
                x = x
            NewList = Convert(x)
            AscNew = NewList
            AscNew.sort()
            DescInt = int(AscNew[3] + AscNew[2] + AscNew[1] + AscNew[0])
            AscInt = int(AscNew[0] + AscNew[1] + AscNew[2] + AscNew[3])
            NewNum = DescInt - AscInt
            count += 1
        countList.append(count)
    n += 1
        

print(f"Kaprekar's routine takes {sum(countList)} total iterations for all four-digit numbers")
    
    