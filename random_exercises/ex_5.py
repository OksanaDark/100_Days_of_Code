# Exercise 5:
# Write a program that calculates the factorial of a given number entered by the user.
# The factorial of a number n is the product of all positive integers from 1 to n.

user_input = int(input("Write a number: "))
factorial = 1
i = 0


while i < user_input:
    i += 1
    factorial *= i

print(factorial)
