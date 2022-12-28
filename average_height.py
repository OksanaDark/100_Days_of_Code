student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# student_heights = [180 128 165 173 189 169 146]
total_amount = 0
total_height = 0
for height in student_heights:
    total_height += height
    total_amount += 1
result = total_height / total_amount
print("The highest score in the class is: " + str(round(result)))

