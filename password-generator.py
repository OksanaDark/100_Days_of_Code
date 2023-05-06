import random


class PPO:
    def password_generator():
        letters_list = ['a', 'b', 'c', 'd', 'i', 'f', 'g', 'A', 'B', 'C', 'D', 'I', 'F', 'G']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '@', '#', "$", '&', '*']

        num_letters = int(input("How many letters would you like to have in your password? "))
        numbers_list = int(input("How manu numbers would like to have?"))
        symbols_list = int(input("How manu symbols would like to have?"))

        password_one = ''
        for i in range(num_letters):
            password_one += random.choice(letters_list)

        password_two = ''
        for i in range(numbers_list):
            password_two += random.choice(numbers)

        password_tree = ''
        for i in range(symbols_list):
            password_tree += random.choice(symbols)

        new_password =  password_two + password_one + password_tree

        print("Your password is:", new_password)

x = PPO

x.password_generator()


# letters = ['a', 'b', 'c', 'd', 'i', 'f', 'g', 'A', 'B', 'C', 'D', 'I', 'F', 'G']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '@', '#', "$", '&', '*']

#letters_list = int(input("How many letters would you like to have in your password?"))
#numbers_list = input("How manu numbers would like to have?")
#symbols_list = input("How manu symbols would like to have?")

# import random
# import string
#
#
# def generate_password(length, complexity):
#     letters = string.ascii_letters
#     digits = string.digits
#     symbols = string.punctuation
#     password = ''
#
#     # Ensure that the password meets the length requirement
#     while len(password) < length:
#         # Choose a random character set based on the complexity requirement
#         if complexity == 'low':
#             charset = letters
#         elif complexity == 'medium':
#             charset = letters + digits
#         else:
#             charset = letters + digits + symbols
#         # Add a random character from the chosen character set to the password
#         password += random.choice(charset)
#     return password


# Get user input for password length and complexity
# length = int(input("How long would you like your password to be? "))
# complexity = input("How complex would you like your password to be? (low/medium/high) ")

# Generate a password based on user input
# password = generate_password(length, complexity)
# print("Your password is:", password)

# import random
#
# tt = int(input("how much "))
# values = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_!@"
# temp_value = []
# password = ""
#
# for i in range(tt):
#     x  = random.randint(0, len(values))
#     temp_value.append(values[x])
#     password = ''.join(temp_value)
#
# print(password)

# #
