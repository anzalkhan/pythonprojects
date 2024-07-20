# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Names:        Anzal Khan
#               Hao Zheng
#               Tyn Mai
#               Xavier Gilmer
# Section:      580
# Assignment:   Lab 11.10
# Date:         16 November 2022
#
fileinput = input("Enter the name of the file: ")
validlist = []

#reading file and finding valids
with open(fileinput,"r") as passports:
    passlist = str(passports.read()).split("\n\n")
    for line in passlist:
        if "cid:" in line and "pid:" in line and "hgt:" in line and "byr:" in line and "ecl:" in line and "eyr:" in line and "iyr:" in line:
            validlist.append(line)
        else:
            continue
        
#writing valids into new file
validstr = "\n\n".join(validlist)
#print(validstr)
destination = "valid_passports.txt"
with open(destination, "w") as valid:
    valid.write(validstr)

with open(destination,"r+") as valids:
    validlist = valids.read().split("\n\n")

#converting valid passport strings
for i in range(len(validlist)):
    validlist[i] = validlist[i].replace("\n"," ")

for i in range(len(validlist)):
    validlist[i] = validlist[i].split(' ')

finallist = []
for i in range(len(validlist)):
    test = True
    for j in validlist[i]:
        if "byr" in j:
            if not(int(j[4:]) >= 1920 and int(j[4:]) <= 2005):
                test = False
                break
        if "iyr" in j:
            if not(int(j[4:]) >= 2012 and int(j[4:]) <= 2020):
                test = False
                break
        if "eyr" in j:
            if not(int(j[4:]) >= 2022 and int(j[4:]) <= 2032):
                test = False
                break
        if "hgt" in j:
            if "cm" in j:
                num = int(j[4:-2])
                if not(num >= 150 and num <= 193):
                    test = False
                    break
            elif "in" in j:
                num = int(j[4:-2])
                if not(num >= 59 and num <= 76):
                    test = False
                    break
            else:
                test = False
                break
        if "ecl" in j:
            if not(j[4:] == 'amb' or j[4:] == 'blu' or j[4:] == 'brn' or j[4:] == 'gry' or j[4:] == 'grn' or j[4:] == 'hzl' or j[4:] == 'oth'):
                test = False
                break
        if "pid" in j:
            if len(j[4:]) != 9:
                test = False
                break
        if "cid" in j:
            if len(j[4:]) != 3:
                test = False
                break
            if int(j[4:]) < 100:
                test = False
                break
    if test:
        finallist.append(validlist[i])
    else:
        continue

#convert finallist to a list of valid passports
#print(finallist)
for i in range(len(finallist)):
    finallist[i] = ' '.join(finallist[i])

#convert finallist to a big string
finalstr = "\n\n".join(finallist)

#create file
destination = "valid_passports2.txt"
with open(destination, "w") as x:
    x.write(finalstr)

print(f'There are {len(finallist)} valid passports')

#reading to check
#with open(destination, "r") as x:
    #print(x.read())
            
            