print("Welcome to Python Pizza Deliveries!")
size  = input("What size Pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your Pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

if size == "S":
    total_price = 15
    print("You have selected Small Pizza")
elif size == "M":
    total_price = 20
    print("You have selected Medium Pizza")
elif size == "L":
    total_price = 25
    print("You have selected Large Pizza")
else:
    print("Invalid input for size, try again!")

if pepperoni == "Y" and size == "S":
    total_price += 2
    print("Adding Pepperoni to Small Pizza adds $2 on your total price")
if pepperoni == "Y" and size == "M" or pepperoni == "Y" and size == "L":
    total_price += 3
    print("Adding Pepperoni on a Medium or Large size Pizza adds $3 on your total")

if extra_cheese == "Y":
    total_price += 1
    print("Adding extra cheese on your Pizza adds $1 on your total")

print(f"You have to pay a grand total of ${total_price}")
