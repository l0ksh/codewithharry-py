#!/usr/bin/python3

def calculate_sum(n):
    if n == 0:
        return 0
    else:
        return n + calculate_sum(n - 1)

n = int(input("Enter a positive integer: "))
sum_of_natural_numbers = calculate_sum(n)
print("The sum of the first", n, "natural numbers is:", sum_of_natural_numbers)
