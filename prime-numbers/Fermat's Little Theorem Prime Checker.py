# Fermat's Little Theorem Prime Checker
# Uses Fermat's Little Theorem to check prime numbers
# By Atharv Sonwane

import random
print("Welcome to Fermat's Little Theorem Prime Checker\n")
p=int(input("Which number would you like to test for primality? "))
if p == 1:
    print("1 is NOT PRIME, due to your foolishness this program will exit")
    sys.exit(1)
print("")
n=1
cm=(561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341, 41041, 46657, 52633, 62745, 63973, 75361, 101101, 115921, 126217, 162401, 172081, 188461, 252601, 278545, 294409, 314821, 334153, 340561, 399001, 410041, 449065, 488881, 512461)
should_restart=True
while should_restart==True:
    rn=random.randint(1,p-1)
    if rn in cm: 
        should_restart=True
    else:
        if (rn**(p-1))%p==1:
            print("The number ", p, " is prime (very probably)\n")
        else:
            print("The number ", p, " is composite\n")
    should_restart=False
print("Thank-you for using Fermat's Little Theorem Prime Checker")
print("Made by Atharv Sonwane, credits go to all those who have tought him and a special thanks to Perre de Fermat for thinking up his Litlle Theorem, he was a true genius.")
