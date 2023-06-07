# Exercise 4:
# Write a program that generates and prints a random number between 1 and 10.
# Keep asking the user to guess the number until they guess it correctly.
import random

random_number = random.randint(1, 10)
user_input = int(input("Write one number from 1 to 10"))

while user_input != random_number:
    user_input = int(input("It is wrong number, try again!"))
else:
    print("You win!")





