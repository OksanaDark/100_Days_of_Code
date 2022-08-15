import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
length_list = len(names) - 1
random_name = random.randint(0, length_list)
random_names = names[random_name]

print(f"{random_names} is going to buy the meal today!")
# # Angela, Ben, Jenny, Michael, Chloe
