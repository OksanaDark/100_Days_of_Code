print("Welcome to the Rollercoaster!")
height = int(input("What is your height in cm?\n"))
bill = 0

if height >= 120:
    print("You can ride the Rollercoaster")
    age = int(input("What is your age?\n"))
    if age < 12:
        bill = 5
        print("Child ticket 5$")
    elif age <= 18:
        bill = 7
        print("Youth ticket 7$")
    else:
        bill = 12
        print("Adult ticket 12$")
    wants_photo = input("So you want a photo taken? Y or N \n")
    if wants_photo == "Y" or wants_photo == "y":
        bill += 3
        print(f"Your bill is {bill}$")
else:
    print("You can`t ride")
