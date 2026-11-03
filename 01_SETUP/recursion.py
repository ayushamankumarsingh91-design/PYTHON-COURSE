# 25/09/2026
# recursion : when a fn call's itself until a particular condition is satisfied.
# do repeatitive action
# it is also the core mechanism of several algorithm.
# backtracking use in recursion
# both recursion and back tracking are a technique
# alogrithm : set of instructions , technique : made by you you can do modification into it
# syntax of recursion
def f(n):
    if(n==4):
        return
    print(n)
    f(n+1)

f(1)

# factorial
def fact(n):
    if n==1 or n==0:
        return 1
    return n*fact(n-1)

print(fact(5))