# Exercise
# Write a Python function guess_the_number(target) that implements a simple number-guessing game. The function should:
#
# Take an integer target (the number to guess) as input.
# Continuously prompt the user to enter a guess using input().
# Provide feedback for each guess:
# If the guess is too high, print "Too high!".
# If the guess is too low, print "Too low!".
# If the guess is correct, print "Correct!" and stop the loop.
# The function should ensure the user only enters integers, prompting them again if they enter invalid input.


# Example
# guess_the_number(42)
# Output:
# Enter your guess: 50
# Too high!
# Enter your guess: 30
# Too low!
# Enter your guess: 42
# Correct!
#
#
#
# def guess_the_number(target):
#     while True:
#         guess = input("Insert a number")
#         if guess.isdigit():
#             guess = int(guess)
#             if guess > target:
#                 print("Too high")
#             elif guess < target:
#                 print("Too Low")
#             else:
#                 print("Correct")
#                 break
#         else:
#             print("Insert a number, not a word")





def guess_the_number(target):
    while True:
        try:
            guess = int(input("Insert a number"))
            if guess > target:
                print("Too high")
            elif guess < target:
                print("Too Low")
            else:
                print("Correct")
                break
        except:
            print("Insert a valid number")

guess_the_number(47)