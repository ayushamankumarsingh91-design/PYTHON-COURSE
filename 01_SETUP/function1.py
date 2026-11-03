# 23/09/2026
# def hello(name = "Student"):
#     print("Hello" ,name)

# hello("Ravi")
# hello()

# # write a function to print all the elements/items of a given list.
# x = [10,20,30,40,50]
#for i in range(len(L)):
    #print(i)
    #for i in L:
        #print(i)

"""def pl(l):
    for i in range(len(l)):
        print(l[i], end = " " )
pl(x)

x.append(90)"""

# write a fn to print all the digits of a given number {n = 7369}
n = int(input())
print()
def dp(n):
    while (n!=0):
        ld = n%10
        print(ld)
        n = n//10
dp(n)



