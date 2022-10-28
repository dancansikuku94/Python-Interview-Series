# Given an array of n non-negative integers , how can you find a non-negative integer that is not in the array?
list_num = [0, 1, 2, 3, 4, 6, 7]


def find_missing_number(L):
    list_dict = {}  # Create empty dictionary
    for i in list_num:
        list_dict[i] = True  # Store all the elements in the dictionary
    for i in range(len(list_dict) + 1):
        if not list_dict.get(i):
            return i
    return None


print(find_missing_number(list_num)) # 5 is the missing integer
