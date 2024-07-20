# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Anzal Khan
#               Nayle Cantu
#               Kevin Long
#               Maryam Eid
# Section:      580
# Assignment:   Lab 7 Gomoves
# Date:         17 October 2022


p1=''
p2=''
turn=1

letlab=[' ','1','2','3','4','5','6','7','8','9']
line1=['1','.','.','.','.','.','.','.','.','.']
line2=['2','.','.','.','.','.','.','.','.','.']
line3=['3','.','.','.','.','.','.','.','.','.']
line4=['4','.','.','.','.','.','.','.','.','.']
line5=['5','.','.','.','.','.','.','.','.','.']
line6=['6','.','.','.','.','.','.','.','.','.']
line7=['7','.','.','.','.','.','.','.','.','.']
line8=['8','.','.','.','.','.','.','.','.','.']
line9=['9','.','.','.','.','.','.','.','.','.'] #elements of the board

biglist=[letlab,line1,line2,line3,line4,line5,line6,line7,line8,line9,] #list of list to make board

def board(): #sets/creates the board
    for i in range (0,10):
        bigliststr = str(biglist[i])
        bigliststr1 = bigliststr.replace("[","")
        bigliststr2 = bigliststr1.replace("]","")
        bigliststr3 = bigliststr2.replace("'","")
        bigliststr4 = bigliststr3.replace(",","") #gets rid of all the syntax around the list to make the board neater
        print(bigliststr4)

board() #prints the board out
print()

if p1 != 'stop' and p2 != 'stop':
    while p1 != 'stop' and p2 != 'stop':
        if turn==1:
            p1row=(input("Player 1: Enter row (1-9) for desired space: "))
            p1col=(input("Player 1: Enter column (1-9) for desired space: "))
            
            if p1row != 'stop' and p1col != 'stop':
                ip1r = int(p1row) #changes variable from string to int to access list elements
                ip1c = int(p1col)
                space=biglist[ip1r][ip1c] #accesses desired element from list of list
                if space == '.': 
                    biglist[ip1r][ip1c] = 'O' #changes to the piece
                    board()
                    turn+=1 #adds 1 to turn so it goes to player 2's turn
                else: 
                    print("Space is invalid! Try another space")
            elif p1row == 'stop' or p1col == 'stop':
                print("Stop by Player 1")
                turn=3 #just so turn isn't 1 or 2
            
        if turn==2:
            p2row=(input("Player 2: Enter row (1-9) for desired space: "))
            p2col=(input("Player 2: Enter column (1-9) for desired space: "))
            if p2row != 'stop' and p2col != 'stop':
                ip2r = int(p2row) #changes variable from string to int to access list elements
                ip2c = int(p2col)
                space2=biglist[ip2r][ip2c] #accesses desired element from list of list
                if space2 == '.': 
                    biglist[ip2r][ip2c] = '@' #changes to the piece
                    board()
                    turn-=1 #subtracts 1 from turn so it goes to player 1's turn
                else: 
                    print("Space is invalid! Try another space")
            elif p2row == 'stop' or p2col == 'stop':
                print("Stop by Player 2")
                turn=3
                
        elif turn==3:
            break #ends the game if a player enters "stop"
        else : 
            print("Turn Error")
