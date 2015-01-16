# Grade Calculator
# Calculates grades from given mark
# By Atharv Sonwane

from time import sleep
import sys

repeat = True
while repeat == True:

    print("\nTHE SUPREME GRADE CALCULATING BEING")
    i=0
    while i < 4:
        sys.stdout.write('.') 
        sleep(0.5)
        i += 1
    mark = int(input("\nEnter your mark: "))
    
    while i < 9:
        sys.stdout.write('.')
        sleep(0.5)
        i += 1
        
    def report(mark, grade, comment):
        print("Your mark: " + str(mark) + ". Your grade: " + grade + ". Comment: " +
        comment)
    print("")
    if mark >= 81:
        grade = "A"
        report(mark, grade, "Aim for an A*.")
    elif mark >= 75:
        grade = "B"
        report(mark, grade, "Average performance, but not good enough for an A")
    elif mark >= 69:
        grade = "C"
        report(mark, grade, "Poor ...")
    elif mark >= 63:
        grade = "D"
        report(mark, grade, "Very Bad. I expect much more from you")
    elif mark >= 58:
        grade = "E"
        report(mark, grade, "Absolute rubbish. How can you get so bad? That is appauling")
    elif mark < 58:
        grade = "U"
        report(mark, grade, "Get out of my sight.")

    repeatstr = input("\nDo you want to go again? BEWARE! [Y/n] ")
    if repeatstr == "Y" or repeatstr == "y" or repeatstr == '':
        repeat = True
    elif repeatstr == "N" or repeatstr == "n":
        repeat = False
    elif repeatstr == "penguins":
        print("Penguins are cool! Now, for your answer to the question...")
    else:
        print("Give a proper answer or FELL MY WRATH\n")

print("\nThankyou for using The Supreme Grade Calculating Being")
print("Credits go to Atharv Sonwane and those who have taught him")
