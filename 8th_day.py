# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How are you today {name} ?")

# greet_with_name("Angela")

def time_in_weeks(age):
    time_left = 90 - age
    time_in_weeks = time_left * 52
    t_left = str(time_in_weeks)
    print("You have " + t_left + " weeks left.")

time_in_weeks(56)