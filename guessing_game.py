# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:         Anzal Khan
# Section:      580
# Assignment:   Lab 10.14
# Date:         9 November 2022
#
count = 0
def guessnum(x): #first function
    count = 0
    secretnum = 26
    while True:
        try:
            x = int(x)
            if x > secretnum:
                x = (input("Too high! What is your guess? "))
                count += 1
            elif x < secretnum:
                x = (input("Too low! What is your guess? "))
                count += 1
            else:
                count += 1
                print(f'You guessed it! It took you {count} guesses.')
                break
        except:
           x = input("Bad input! Try again: ")
def main(): #calling first function
    guess = (input("Guess the secret number! Hint: it's an integer between 1 and 100... What is your guess? "))
    return guessnum(guess)

main()