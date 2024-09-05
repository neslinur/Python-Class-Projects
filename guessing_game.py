# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Neslinur Kaya
# Section: 403
# Assignment: lab 10.15
# Date: 01 11 2023


print("Guess the secret number! Hint: it's an integer between 1 and 100...")
secret = 27
#make it zero to start it off
guess = 0
count = 0

def ask():
    guess = input("What is your guess? ")
    return guess

def high_low(a,b):
    if a < b:
        print("Too low!")
    elif a > b:
        print("Too high!")
    

while guess != secret:
    #ask here so it keeps asking
    guess = ask()
    #make this to check if input is valid
    while True:
        try: 
            guess = int(guess)
            #it will break when input is valid
            break
        except:
            guess = input("Bad input! Try again: ")
            #it will keep asking if input is invalid
    high_low(guess,secret)
    #add a count for every try
    count += 1



print(f"You guessed it! It took you {count} guesses.")