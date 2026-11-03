# Write function to calculate 1. min,2.max,3. average whole
def min_max_avg(t):
    if not t:
        return "Tuple is empty."
    
    minimum = min(t)
    maximum = max(t)
    average = sum(t) // len(t)
    
    return minimum, maximum, average
print(min_max_avg((10, 20, 30, 40)))

#or
def min_max_avg(s):
    print(f"Maximum : {max(s)}")
    print(f"Minimum : {min(s)}")
    print(f"Average : {sum(s)//len(s)}")

min_max_avg(s)


