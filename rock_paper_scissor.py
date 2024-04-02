## Get and print a random choice for the computer
import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

computer_choice = get_computer_choice();

print(computer_choice);
