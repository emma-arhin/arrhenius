"""
File: guessmynumber.py
----------------------
This program checks if a user's guess of a number matches that guessed by the computer
"""

import random
# The computer should input a random number
# ********************************** YOUR CODE GOES BELOW HERE ********************************************************
number=random.randint(1,99)
print('I am thinking of a number from 1-99 ')
# the random should in range of 1-99 and assign to variable called number
while number:
    number=random.randint(1,99)
# the number from user should an integer
    guess=int(input('guess the number: '))
#The number user is going to input should an integer
    if guess > number:
# when the guess number from the user is greater than the number from the computer should move to the line
        print("incorrect, your guess is too high")
#the program should print incorrect,your is too high
    elif guess < number:
#when guess is less than number
        print('incorrect, your guess is too low')
#the program should print incorrect your is too low
    else:
#when non of the conditions are met
        print("congrats!, The number was: ",number)
        break
#break while loop

