# Leap Year Checker
# checks whether or not the a year is a leap year
# By Atharv Sonwane
 
def leapcheck(num):
    if num % 4 == 0:
        return True
    else:
        return False
num = int(input("What number do you want to check?"))
x = leapcheck(num)
