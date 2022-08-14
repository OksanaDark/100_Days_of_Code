import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

some_value = random.randint(0, 1)

if some_value == 0:
    print("Tails")
else:
    print("Heads")
