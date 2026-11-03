# Swapcase capital become small and vice versa
# S= "Recursion funtion 24"
# (i)write function
# (ii) write a recursive function

s = input()
clean_s = s.strip()

def swapcase(s):
    te =""
    for i in s:
        if i.isupper():
            te += i.lower()
        elif i.islower():
            te += i.upper()
        else:
            te += i
    return te

print(swapcase(clean_s))