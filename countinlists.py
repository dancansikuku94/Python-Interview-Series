# Find out the number of elements in a list using recursion.
l = [1,2,3]
def count_len(L):
    if not l:
        return 0
    return 1+count_len(l[1:])

# Count each element in the list
fruits = ["Apple","Oranges","Apples","Mangoes","Apple","Mangoes"]
apple = fruits.count("Apple")
oranges = fruits.count("Oranges")
mangoes = fruits.count("Mangoes")
print(f"Apples = {apple} , Oranges = {oranges} , Mangoes = {mangoes}") # Apples = 2 , Oranges = 1 , Mangoes = 2
