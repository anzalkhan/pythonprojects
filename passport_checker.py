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
    
#reading list (not necessary)
#with open(destination, "r") as reading:
    #print(reading.read())
    
#outputs
print(f'There are {len(validlist)} valid passports')
