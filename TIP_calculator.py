invalid = False

print("Welcome to the TIP calculator!")

amount = input("What was the total amount?\n$")
try:
    int(amount)
except ValueError:
    invalid = True

if not invalid:
    tip = input("How much tip would you like to offer? \n$")
    try:
        int(tip)
    except ValueError:
        invalid = True
if not invalid:
    nr_of_persons = input("How many people split the bill?\n")
    try:
        int(nr_of_persons)
    except ValueError:
        invalid = True
if not invalid:
    amount_per = round((int(amount) + int(tip)) / int(nr_of_persons), 2)

print(f"Each person should pay: ${amount_per}") if not invalid else print("INVALID SELECTION!")