# a1 = [1,2,3,4]
# a2 = [2,3,5,6]
# x = set(a1) # unique elements
# y = set(a2)
# print((x|y) - (x&y)) # union - intersection
 
#2nd way

a1 = [1,2,3,4]
a2 = [2,3,5,6]
def f(a1,a2):
    a1 = set(a1)
    a2 = set(a2)
    result = a1^a2 #symmetric difference
    return result
print(f(a1,a2))
