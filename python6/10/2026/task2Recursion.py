# print no. of ways to reach on the top stair if input is given as total no. of stairs = 2
# two possibilities ek step me or 2 step me
# no. of ways to reach top by 1 stair + no. of ways to reach top by 2 stairs
# n = 1 return 1 or if n = 2 then return 2
# here is 2 base conditions
n = int(input())

def f (n): # no. of ways to reach top
    if n== 1:
        return 1
    if n== 2:
        return 2

    return f(n-1) + f(n-2)

print(f(n)) #funtion call
