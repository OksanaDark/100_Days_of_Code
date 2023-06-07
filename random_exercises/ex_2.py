# Exercise 2:
# Write a program that asks the user to enter a password. Keep asking for the password until the user enters the correct
# password "password123".

user_input = input("Please enter the password: ")
correct_password = "password123"
password_attempts = 1

while user_input != correct_password:
    if password_attempts < 5:
        if user_input == " " or user_input == "":
            user_input = input("Your password cannot be an empty string, try again: ")
            password_attempts += 1
        else:
            user_input = input("Password incorrect, please try again: ")
            password_attempts += 1
    else:
        print("Try again later")
        break
else:
    print("It`s correct")

