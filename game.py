# Write your code here
import random

# intro
name = input("Enter your name:")
print("Hello,", name)

# setting the starting score - reading the scores from file or setting the initial score to 0
file = open("rating.txt", "r", encoding="UTF-8")
scores = file.readlines()

# print(scores)

for table_score in scores:
    if name in table_score:
        user_score = int(table_score.split(" ")[1:][0])
        break
    else:
        user_score = 0

print("your start score is:", user_score)

# reading the list of options for game

initial_game_options = input().split(",")

if initial_game_options == ['']:
    initial_game_options = ["rock", "paper", "scissors"]

# print(initial_game_options)
print("Okay, let's start")

# main: input and output
while True:
    computer_choice = random.choice(initial_game_options)
    game_options = initial_game_options.copy()

    user_input = input()

    if user_input == "!exit":
        print("Bye!")
        break
    elif user_input == "!rating":
        print("Your rating:", user_score)
        continue
    elif user_input not in initial_game_options:
        print("Invalid input")
    elif user_input == computer_choice:
        # Draw
        print(f"There is a draw ({user_input})")
        user_score += 50
    else:
        # different scenarios for first/last elements in list and elements in the middle
        if user_input == game_options[0] or user_input == game_options[-1]:
            game_options.remove(user_input)
        else:
            list_to_move = game_options[(game_options.index(user_input) + 1):]
            # print(list_to_move)
            del game_options[game_options.index(user_input):]
            game_options = list_to_move + game_options
            # print(game_options)

        # list of options which beat the user input - first half, the other half will be defeated
        beating_options = game_options[:int((len(game_options) / 2))]
        # defeated_by = game_options[(len(game_options) / 2):]
        # Lose condition
        if computer_choice in beating_options:
            print(f"Sorry, but the computer chose {computer_choice}")
        else:
            # Win condition
            print(f"Well done. The computer chose {computer_choice} and failed")
            user_score += 100

file.close()
