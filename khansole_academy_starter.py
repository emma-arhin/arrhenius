"""
File: khansole_academy.py
-------------------------
Khansole Academy is a program that teaches users how to add by asking users to input answers for the addition of two
randomly generating integers between 10 and 99 inclusive. The program returns feedback based on the User's answers.

"""

import random
#the computer should give out a random number
# ********************************** YOUR CODE GOES BELOW HERE *********************************************************
z=random.randint(10,99)
#random.randint is assign to a variable z
y=random.randint(10,99)
#random.randint is assign to a variable y
b=z+y
#z+y is assign to variable b
count=1
# means it count the number the user gets the answer correct
while count<=3:
    z = random.randint(10, 99)
    y = random.randint(10, 99)
    b = z + y
    num = print("what is",z,"+",y, "?")
#the print is assign to a variable num
    kk = int(input("Answer"))
#the inputed answer should be an integer and assign to a variable kk
    if kk==b:
#when kk equals b it should print
        print("Correct!! You've gotten", count,"times")
        count +=1
#means the indexing variable
    else:
       count=1
#means the user gets the answer incorrect it should start all over again
       print("incorrect. The expected number was", b)
print('Congrats! You mastered Addition')


