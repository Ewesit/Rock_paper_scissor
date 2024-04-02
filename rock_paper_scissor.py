# Get and print a random choice for the computer
import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

computer_choice = get_computer_choice();

# print(computer_choice);

#Get a random choice for the user

def get_user_choice():
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    return user_choice

user_choice = get_user_choice();

#Determine winner

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"
        
# winner = determine_winner(user_choice, computer_choice);
# print(winner)
    
#play game and determine winner with most wins
def play_game(rounds):
    user_score = 0
    computer_score = 0
    for _ in range(rounds):
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        print(f"You chose: {user_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

    print("Game over!")
    print(f"Your score: {user_score}")
    print(f"Computer's score: {computer_score}")
    if user_score > computer_score:
        print("You win the game!")
    elif computer_score > user_score:
        print("Computer wins the game!")
    else:
        print("It's a tie!")

# Main game loop
while True:
    rounds = int(input("Enter the number of rounds (3 or 5): "))
    if rounds in [3, 5]:
        break
    else:
        print("Invalid number of rounds. Please enter 3 or 5.")

play_game(rounds)