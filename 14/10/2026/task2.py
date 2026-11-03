# Write a function to print each element of the given tuple beside it's index
#t=(10,20,30,40)

t =(10,20,30,40)
# 0 1 2 3
def f(t):
    for i in range(len(t)):
        print(f"{i} : {t[i]}")
        #or
        print(i,":",t[i])

f(t)