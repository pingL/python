# greatest of them all
# algorithm demonstration to show how to find biggest number in an array
# By Atharv Sonwane

# sets array
array = [3,4,5,6,657,54,546]

# creates variable current_largest
current_largest = array[0]

# loop goes through every number in array and if the number is greater than the
# current_largest, it sets that number as the current_largest

for i in array:
    if i > current_largest:
        cr = i

# prints the current_largest
print(current_largest)
