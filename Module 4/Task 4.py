import random

number_to_guess = random.randint( :1, :10)


print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 10.")
while True:
    guess = input("Guess the number: ")


    try:
        guess = int(guess)
        if guess == number_to_guess:
            print("Congralutations! You guessed the number!")
        elif guess < number_to_guess:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
    except ValueError:
        print("Please enter a valid number.")
        continue
