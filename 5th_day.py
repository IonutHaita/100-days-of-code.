# #for loops in lists
# student_scores = [120, 150, 123, 145, 154, 167, 134, 178, 156]
# total1 = 0
# total = 0
# for score in student_scores:
#     total += score
# print(total)

# total1 = sum(student_scores)
# print(total1)

# max_score = 0
# score = 0
# for score in student_scores:
#     if score > max_score:
#         max_score = score
# print(f"{max_score} is the highest score.")

#for loops in range
for number in range(1, 10):
    print(number)

for number in range(1, 12, 3):
    print(number)

sum=0
for number in range(1, 101):
    sum += number
print(sum)
#Exercise:
# The FizzBuzz challenge: print numbers from 1 to 100. If the number is divisible by 3 print Fizz instead of the no., 
# if it's divisible by 5 print Buzz and if the number is divisible by both 3 and 5(i.e. 15) print FizzBuzz
for number in range(1, 101):
    if number % 3 == 0 and number % 5 != 0:
        print("Fizz")
    elif number % 5 == 0 and number % 3 != 0:
        print("Buzz")
    elif number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    else:
        print(number)