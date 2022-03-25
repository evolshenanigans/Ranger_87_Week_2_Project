import random

player_name = input("What is your name? ")
print(f"Hi, {player_name}!")
victories = 0
defeats = 0
ties = 0

while True:
    user_action = input("Enter a choice(rock, paper, scissors): ")
    user_action = user_action.lower()
    possible_actions = ["rock", "paper", "scissors"]
    if user_action not in possible_actions:
        print("Invalid input. Please enter one of the following: rock, paper, scissors")
        continue
    computer_action = random.choice(possible_actions)
    print(f'\nYou chose {user_action}; the computer chose {computer_action}.\n')

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
        ties += 1
        print(f"\nRecord: {player_name} - {victories}, computer - {defeats}; ties - {ties}\n")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
            victories += 1 
        else:
            print("Paper covers rock! You lose.")
            defeats += 1
        print(f"\nRecord: {player_name} - {victories}, computer - {defeats}; ties - {ties}\n")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You Win!")
            victories += 1
        else:
            print("Scissors cuts paper! You lose.")
            defeats += 1
        print(f"\nRecord: {player_name} - {victories}, computer - {defeats}; ties - {ties}\n")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
            victories += 1
        else:
            print("Rock smashes scissors! You lose.")
            defeats += 1
        print(f"\nRecord: {player_name} - {victories}, computer - {defeats}; ties - {ties}\n")
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        print(f"Thanks for playing, {player_name}! Final statistics:")
        print(f"Games played: {victories + ties + defeats}; {player_name} - {victories}, computer - {defeats}; ties - {ties}\n")
        break