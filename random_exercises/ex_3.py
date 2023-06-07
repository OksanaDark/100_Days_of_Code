# Exercise 3:
# Write a program that prompts the user to enter a positive integer. Then, print the sum of all the numbers
# from 1 to that integer.

# user_input = int(input("Write positive integers"))
# total = 0
# for i in range(1, user_input + 1):
#     total += i
# print(total)


user_input = int(input("Write positive integers: "))
total = 0
i = 1

while i <= user_input:
    total += i
    i += 1

print(total)