# import random
#
# words = ["credentials", "beekeeper", "cringe"]
# word_chosen = random.choice(words)
#
# hashed_word = "*" * len(word_chosen)
#
# while "*" in hashed_word:
#     user_input = input("Please type a letter: ")
#     if user_input in word_chosen:
#         for i in range(len(word_chosen)):
#             if word_chosen[i] == user_input:
#                 hashed_word = hashed_word[:i] + user_input + hashed_word[i+1:]
#         print(hashed_word)
#     else:
#         print("Sorry, the letter is not in the word. Please try again.")
#
# print("Congratulations! You guessed the word.")
import random

from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

from hangman_art import logo

print(logo)


print(f'Pssst, the solution is {chosen_word}.')


display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:

        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    from hangman_art import stages

    print(stages[lives])
