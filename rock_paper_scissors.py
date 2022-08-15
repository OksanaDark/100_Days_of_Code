import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
value_list = [rock, paper, scissors]
# Write your code below this line 👇

player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
computer_choice = random.randint(0, 2)


print(f"You choose {player_choice} \n {value_list[int(player_choice)]}")
print(f"Computer choose {computer_choice} \n {value_list[computer_choice]}")

if player_choice == "0" and computer_choice == 0:
    print("DRAW")
elif player_choice == "0" and computer_choice == 1:
    print("Player Loose. Computer Win!")
elif player_choice == "0" and computer_choice == 2:
    print("Player Win. Computer Loose!")
elif player_choice == "1" and computer_choice == 0:
    print("Player Win. Computer Loose!")
elif player_choice == "1" and computer_choice == 1:
    print("DRAW")
elif player_choice == "1" and computer_choice == 2:
    print("Player Loose. Computer Win!")
elif player_choice == "2" and computer_choice == 0:
    print("Player Loose. Computer Win!")
elif player_choice == "2" and computer_choice == 1:
    print("Player Loose. Computer Win!")
elif player_choice == "2" and computer_choice == 2:
    print("DRAW")
else:
    print("WTF")
