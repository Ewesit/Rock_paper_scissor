# Get and print a random choice for the computer
import random

# def get_computer_choice():
#     return random.choice(['rock', 'paper', 'scissors'])

# computer_choice = get_computer_choice();

# print(computer_choice);

#Get a random choice for the user

def get_user_choice():
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    return user_choice

user_choice = get_user_choice();
        
