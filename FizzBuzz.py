for meow in range(1, 101):
    if meow % 3 == 0 and meow % 5 == 0:
        print("FizzBuzz")
    elif meow % 3 == 0:
        print("Fizz")
    elif meow % 5 == 0:
        print("Buzz")
    else:
        print(meow)
