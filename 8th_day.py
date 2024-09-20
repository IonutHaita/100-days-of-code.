# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How are you today {name} ?")

# greet_with_name("Angela")

# def time_in_weeks(age):
#     time_left = 90 - age
#     time_in_weeks = time_left * 52
#     t_left = str(time_in_weeks)
#     print("You have " + t_left + " weeks left.")

# time_in_weeks(56)

# def greet_with(name, location):
#     print(f"Hello {name} from {location}")    

# greet_with("Angela", "Romania")
    
# greet_with(location = "Romania", name = "Angela")

def calc_love_score(name1, name2):
    occurence1 = 0
    occurence2 = 0
    names = name1 + name2
    for letters in "TRUE":
        for letter in names:
            if letters == letter:
                occurence1 += 1
    for letters in "LOVE":
        for letter in names:
            if letters == letter:
                occurence2 += 1
    occ1 = str(occurence1)
    occ2 = str(occurence2)
    print(occ1 + occ2)

calc_love_score("TARA", "TONY")