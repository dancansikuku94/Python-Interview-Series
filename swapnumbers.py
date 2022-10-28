# Write a function to swap two numbers

def swap(a,b):
    c=a
    a=b
    b=c
    return  a,b
print(swap(1,2))

# Another way
def swap_1(a,b):
    a,b = b,a
    return  a,b
print(swap_1(1,2))