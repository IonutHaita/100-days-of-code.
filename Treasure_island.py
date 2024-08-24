print("Welcome to Treasure island!")
print("Your mission is to find the treasure")

direction = input("You're at a cross road. Which path do you want to take? Left or Right\n")
if direction != "Left" and direction != "Right":
    print("Invalid input! Try again!")
good_dir_choice = True if direction == "Left" else False

good_choice = False
if good_dir_choice:
    print("You've come to a lake. There is an island in the middle of the lake.")
    choice = input("Type Wait to wait for a boat or Swim to try and swim across.\n")
    if choice != "Wait" and choice != "Swim":
        print("Invalid input! Try again!")
    good_choice = True if choice == "Wait" else False

if good_dir_choice and not good_choice:
    print("You lost! Try again!")
decision = False
if good_dir_choice and good_choice:
    print("You arrive on the island unharmed. There is a house with three doors.")
    last_choice = input("One red, one yellow and one blue. Which colour do you choose? Type Red, Yellow or Blue\n")
    if last_choice != "Red" and last_choice != "Yellow" and last_choice != "Blue":
        print("Invalid input! Try again!")
    if last_choice == "Yellow":
        decision = True
        print("Congratulations, you are saved!")
    elif last_choice == "Red" or last_choice == "Blue":
        print("You lost! Try again!")

