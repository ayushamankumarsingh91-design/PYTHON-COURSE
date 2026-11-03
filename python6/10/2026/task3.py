# Print the sum of all numbers from 1 to n using Recursion.
n = int(input("Enter a number: "))
def sum_of_numbers(n):
    if n == 1:
        return 1
    return n + sum_of_numbers(n-1)
print(sum_of_numbers(n))