import random

print("Ill guess your number")

top_range = input("Type a number: ")

while True:
    try:
        top_range = int(top_range)
        break
    except ValueError:
        top_range = input("Type a NUMBER! ")
if top_range <= 0:
    print(" Pick a number bigger than 0")
    quit()
random_num = random.randint(1, top_range)
guesses = 0
while True:

    try:
        user_guess = int(input("Make a guess: "))
    except ValueError:
        print(" Guess should be a number!!!")
        continue
    if user_guess < 1 or user_guess > top_range:
        print(" Guess should be between 1 and", top_range)
        continue
    guesses += 1
    difference = abs(random_num - user_guess)
    if user_guess < random_num:
        print(" You are below the number")
    elif user_guess > random_num:
        print(" You are over the number")
    if user_guess == random_num:
        print(" You guessed the number!")
        break
    if difference <= 5:
        print(" You are very close")
    elif difference <= 10:
        print(" You are close")

print("You got it in",guesses,"guesses")