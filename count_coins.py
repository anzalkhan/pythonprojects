# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Names:        Anzal Khan
# Section:      580
# Assignment:   Lab 11.12
# Date:         16 November 2022
#
#reading game and creating coin list
game = "C:/Users/anzal/Downloads/Spyder Files/LAB_ Counting coins/game.txt"
with open(game,"r") as z:
    gamelist = z.read().split("\n")
    coinlist = []
    for line in gamelist:
        if "coin" in line:
            coinlist.append(line)
        else:
            continue

#analyze coinlist
changelist = []
for i in coinlist:
    if "+" in i:
        val = int(i[6:])
        changelist.append(val)
    else:
        val = int(i[5:])
        changelist.append(val)
totalchange = sum(changelist[:])
print(changelist)
print(f'Total coins collected: {totalchange}')
strlist = []
for i in changelist:
    i = str(i)
    strlist.append(i)
changestr = "\n".join(strlist)

#output and writing new file
destination = "coins.txt"
with open(destination,"w") as x:
    x.write(changestr)


        
        