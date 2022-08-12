print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lower_name1 = name1.lower()
lower_name2 = name2.lower()
together_name = lower_name1 + lower_name2
# value_true = "true"
# value_love = "love"
# x = 0
# y = 0
#
# for i in value_true:
#     x += together_name.count(i)
# for i in value_love:
#     y += together_name.count(i)
#
#
# print(str(x) + str(y))


name1_count_t = together_name.count("t")
name1_count_r = together_name.count("r")
name1_count_u = together_name.count("u")
name1_count_e = together_name.count("e")
count = name1_count_t + name1_count_r + name1_count_u + name1_count_e

name1_count_l = together_name.count("l")
name1_count_o = together_name.count("o")
name1_count_v = together_name.count("v")
name1_count_e = together_name.count("e")
count2 = name1_count_l + name1_count_o + name1_count_v + name1_count_e

together_score = str(count) + str(count2)

if int(together_score) < 10 or int(together_score) > 90:
    print(f"Your score is {together_score}, you go together like coke and mentos.")
elif 40 < int(together_score) < 50:
    print(f"Your score is {together_score}, you are alright together.")
else:
    print(together_score)
