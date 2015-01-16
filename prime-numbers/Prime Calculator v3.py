# Prime Calculator v3
# Checks a number for primality
# By Atharv Sonwane and Inigo Rhode

import math

print("Welcome to the Prime Checker v3 \n")

x=int(input("Enter an interger to check if its prime"))
print("")

y=math.sqrt(x)
z=2
a=3
prime=True

while a<y:
    if (x%z)==0:
        if (x%z)==0:
            print("Sorry not prime, divisible by " + str(z) + "\n")
            prime=False
            break
        elif (x%z)>0:
            print("Good : Not divisible by " + str(z))
    else:
        if (x%a)==0:
            print("Sorry not prime, divisible by " + str(a) + "\n")
            prime=False
            break
        else:
            print("Good : Not divisible by " + str(a))
            a += 2
if prime==False:
    print("Your number ", x, " is not prime \n")
else:
    print("Congratulations, your number " + str(x) + " is prime \n") 
    
print("Thank-you for using Prime Checker v3")
print("Made by Atharv Sonwane and Inigo Rhode, credits go to all those who have taught us.")
