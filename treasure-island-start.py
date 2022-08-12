print("Welcome to Treasure Island.Your mission is to find the treasure. You're at a cross road\n")
choice = input('Where do you want to go? Type "left" or "right"\n')

if choice.lower() == "left":
    choice = input('You have come to a lake. There is an island in the middle of the lake. '
                   'Type "wait" to wait for a boat. Type "swim" to swim across.\n')
    if choice.lower() == "wait":
        choice = input(
            "You arrive at the island unharmed. There is a house with 3 doors. "
            "One red, one yellow and one blue. Which colour do you choose?\n"
        )
        match choice.lower():
            case "red":
                print("It's a room full of fire. Game Over.")
            case "blue":
                print("You enter a room of beasts. Game Over.")
            case "yellow":
                print("You found the treasure! You Win!")
            case _:
                print("You chose a door that doesn't exist. Game Over.")

    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")

