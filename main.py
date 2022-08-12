some_string = '()()()()()))))(((((()()()()()()()()())()(((()))))))((('
x = 0

for symbol in some_string:
    if symbol == '(':
        x = x + 1

    elif symbol == ')':
        x = x - 1


if x > 0:
    print("Багато відкриваючих дужок")

elif x < 0:
    print("Багато закриваючих дужок")

else:
    print("Всі дужки закриті")


