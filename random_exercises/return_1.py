# Task: Checking Evenness of a Number
# Write a function is_even(number) that takes a number "number" as input and returns True if the number is even,
# or False if the number is odd.


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


number = int(input("Write a number: "))
result = is_even(number)
print(result)
