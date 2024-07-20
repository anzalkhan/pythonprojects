# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Names:        Anzal Khan
# Section:      580
# Assignment:   Lab 11.11
# Date:         16 November 2022
#
#input and reading file
fileinput = input("Enter the name of the file: ")
with open(fileinput,"r") as barcodes:
    barcodeslist = barcodes.read().split("\n")

#determining valid
validlist = []
for line in barcodeslist:
    line = str(line)
    group1 = [line[0],line[2],line[4],line[6],line[8],line[10]]
    group2 = [line[1],line[3],line[5],line[7],line[9],line[11]]
    intgroup1 = []
    intgroup2 = []
    for i in group1:
        x = int(i)
        intgroup1.append(x)
    for i in group2:
        y = int(i)
        intgroup2.append(y)
    lastdigit = int(line[12])
    sumgroup1 = sum(intgroup1)
    sumgroup2 = sum(intgroup2)
    arithmetic = str(3*sumgroup2 + sumgroup1)
    if 10 - int(arithmetic[-1]) == lastdigit:
        validlist.append(line.replace("'",""))
    else:
        continue
    
#producing valid_barcodes.txt
destination = "valid_barcodes.txt"
validstr = "\n".join(validlist)
with open(destination,"w") as x:
    x.write(validstr)
print(f'There are {len(validlist)} valid barcodes')
#with open(destination,"r") as x:
    #print(x.read())
    
    