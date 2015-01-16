# Squaring Machine
# By Atharv Sonwane

top = int(input("Where do you want me to square up to? "))

def square(top):
    print("Welcome to the squaring machine \n")
    counter = 1
    while counter <= top:
        print("The square of " + str(counter) + " is " + str(counter**2))
        counter += 1
    print("\nThank-you for using the Square Machine by Atharv Sonwane")

square(top)
