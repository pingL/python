# Mind Reader
# guesess number using simple higher lower algorithm
# By Atharv Sonwane

import random
import sys
from time import sleep

print("Welcome to the Mind Reader")
print("Think of a number between 1 and 100")
i=0
while i < 7:
        sys.stdout.write('.') 
        sleep(0.5)
        i += 1
print("")
got = False
a = 1
b = 100
while got == False:
    num = random.randrange(a, b)
    usrans = input("Is your number: " + str(num) + "? Enter (g)reater, (s)maller, (o)n target: ")
    if usrans == "o":
        got = True
    elif usrans == "g":
        a = num
        b = 100
    elif usrans == "s":
        a = 1
        b = num
    else:
        print("Enter valid input")
print("\nThanks for using Mind Reader")
print("Created by Atharv Sonwane, credits go to those who have taught him")
