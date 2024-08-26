total_price = 0
invalid = False

print("Welcome to Python Pizza Deliveries!")
size  = input("What size Pizza do you want? S, M or L: ")
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
    invalid = True

if not invalid:
    pepperoni = input("Do you want pepperoni on your Pizza? Y or N: ")
    if pepperoni == "Y" and size == "S":
        total_price += 2
        print("Adding Pepperoni to Small Pizza adds $2 on your total price")
    elif pepperoni == "Y" and size == "M" or pepperoni == "Y" and size == "L":
        total_price += 3
        print("Adding Pepperoni on a Medium or Large size Pizza adds $3 on your total")
    elif pepperoni == "N":
        total_price = total_price
    else:
        invalid = True

if not invalid:
    extra_cheese = input("Do you want extra cheese? Y or N: ")
    if extra_cheese == "Y":
        total_price += 1
        print("Adding extra cheese on your Pizza adds $1 on your total")
    elif extra_cheese == "N":
        total_price = total_price
    else:
        invalid = True

print(f"You have to pay a grand total of ${total_price}") if not invalid else print("INVALID SELECTION!")
