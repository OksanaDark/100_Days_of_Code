# def arithmetic(first_number, second_number, third_number, first_operation, second_operation):
#     if operation == "+":
#         print(first_number + second_number)
#     elif operation == "-":
#         print(first_number - second_number)
#     elif operation == "*":
#         print(first_number * second_number)
#     elif operation == "/":
#         print(first_number / second_number)
#     else:
#         print("Unknown operation")


# arithmetic(2, 2, 2, "+", "*")

some_list = "((((())))(((()))()()()()()()())())))))()((((()())(()()()()"
some_variable = 0
for variable in some_list:
    if variable == "(":
        some_variable += 1
    elif variable == ")":
        some_variable -= 1
print(some_variable)