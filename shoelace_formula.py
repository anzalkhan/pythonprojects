# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Anzal Khan
#               Tyler Cooper
#               Elizabeth Cross
#               Archer Poreda
# Section:      580
# Assignment:   Lab 9.15
# Date:         2 November 2022
#

#getpoints
def getpoints(vertices):
    listsplit = vertices.split(" ")
    a = 0
    pointlist= []
    while a <= len(listsplit) - 1:
        pointlist.append(listsplit[a].split(","))
        for i in pointlist[a]:
            pointlist[a][0] = int(pointlist[a][0])
            pointlist[a][1] = int(pointlist[a][1])
        a += 1
    return pointlist

#cross
def cross(a,b):
    crossPoints = (a[0]*b[1]) - (a[1]*b[0])
    return crossPoints

#shoelace
def shoelace(finallist):
    c = 0
    d = 1
    sumlist = []
    while d <= len(finallist) - 1:
        sumlist.append(cross(finallist[c],finallist[d]))
        c += 1
        d += 1
    sumlist.append(cross(finallist[d-1],finallist[0]))
    return 0.5*sum(sumlist)

#main
def main():
    vertices = input("Please enter the vertices: ")
    finallist = getpoints(vertices)
    area = shoelace(finallist)
    print(f'The area of the polygon is {area:.1f}')
    
if __name__ == '__main__': 
    main()
