# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Anzal Khan
# Section:      580
# Assignment:   Lab 6.15
# Date:         5 October 2022
#
n = int(input("Enter a value for n: "))
#find sum of integers leading up to n
sum_leading = 0
i = 0
for i in range (n-1):
    i += 1
    sum_leading += i
#print(sum_leading)

#find sum of next two integers after n
sum_r = n + 1
r = 1
adding_num = n + 1
i = 0
while sum_r < sum_leading:
    adding_num += 1
    sum_r += adding_num
    #print(sum_right)
    r += 1
    #print(r)
if sum_r > sum_leading:
    print(n, "is not a balancing number")
else:
    print(n, "is a balancing number with r=",r)
