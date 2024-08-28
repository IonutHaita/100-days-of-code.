import random

choice = "None"

def write_to_terminal(choice):
    Rock = False
    Paper = False
    Scissors = False
    Rock = True if choice == "Rock" else False
    Paper = True if choice == "Paper" else False
    Scissors = True if choice == "Scissors" else False

    if Rock:
        print("Rock")
        print("""
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    """)

    # Paper
    if Paper:
        print("Paper")
        print("""
        _______
    ---'    ____)____
            ______)
            _______)
            _______)
    ---.__________)
    """)

    # Scissors
    if Scissors:
        print("Scissors")
        print("""
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    """)
        
print("Welcome to Rock, Paper, Scissors!")

try:
    choice = input("To play the game write your selection(Rock, Paper or Scissors):\n")
except ValueError:
    print("Invalid input! Try again!")
print("Your selection:")
write_to_terminal(choice)

options = ["Rock", "Paper", "Scissors"]
random_selection = random.choice(options)
print("Computer's choice:")
write_to_terminal(random_selection)
