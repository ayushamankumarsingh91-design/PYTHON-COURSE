# Print all the odd numbers from 1 to n using break/continue
# even wale ko skip kara do
n = 10
for i in range(1,n+1):
    if i%2 == 0:
        continue
    print(i)
