# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? \n")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
column_split = ''.join(position[0])
row_split = ''.join(position[1])

if row_split == "1":
    row1[int(column_split) - 1] = "X "
elif row_split == "2":
    row2[int(column_split) - 1] = "X "
else:
    row3[int(column_split) - 1] = "X "





# match row_split:
#     case "1":
#         row1[int(column_split) - 1] = "X "
#     case "2":
#         row2[int(column_split) - 1] = "X "
#     case "3":
#         row3[int(column_split) - 1] = "X "



# Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
