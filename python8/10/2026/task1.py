def f(a,b):
    if b ==0: # stop if condition satify
        return 1
    return a * f(a,b-1) # recursive call with b-1
print(f(2,5)) # output 32