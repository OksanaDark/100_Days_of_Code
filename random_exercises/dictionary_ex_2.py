# Exercise 2:
# Create an empty dictionary called "phonebook". Prompt the user to enter a name and phone number,
# and add them as key-value pairs to the dictionary. Repeat this process until the user enters "quit".
# Print the phonebook dictionary.

phonebook = {}
user_quit = False

while not user_quit:
    user_name = input("Please write your name: ")
    user_age = input("Please write your age: ")
    phonebook[user_name] = user_age
    ask_quit = input("Do you want to continue? Write yes or quit: ")
    if ask_quit == "quit":
        user_quit = True
        print(phonebook)


