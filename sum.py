# Write a function to check if sum of any two numbers in a list is zero or not.
list_numbers = [1, 2, 3, -1, 4, 5]


def sumoftwonumbers(L):
    l1 = set(list_numbers)  # Create a set of numbers to avoid duplicates
    if len(list_numbers) < 2:
        return False
    for i in list_numbers:
        if -i in l1:
            return True
    return False


print(sumoftwonumbers(list_numbers)) # True
