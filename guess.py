import random
import time

# ---------- Settings ----------
DEBUG_SECRET = None   # For testing, set to a number such as 42. Set back to None before your final commit.
TIME_LIMIT = 60       # Seconds allowed in Time Challenge mode

print("Welcome to the Number Guessing Game")

# ---------- Choose a level ----------
# Goal: keep asking until the player picks a valid level, then set the range and attempt limit.
while True:
    print("Please pick a difficulty level:\n")
    print("1 - EASY - 10 attempts to choose from 1 to 50")
    print("2 - MEDIUM - 8 attempts to choose from 1 to 100")
    print("3 - HARD - 10 attempts to choose from 1 to 500\n")
    selected_level = input("Please enter the digit 1, 2 or 3 to choose the level:\n")

    if not selected_level.isdigit() or int(selected_level) < 1 or int(selected_level) > 3:
        print("Invalid input!")
    else:
        selected_level = int(selected_level)
        print(f"You chose level {selected_level}")
        print("------------------------------------------------------------------------------")
        break

if selected_level == 1:
    low, high, max_attempts = 1, 50, 10
elif selected_level == 2:
    low, high, max_attempts = 1, 100, 8
else:
    low, high, max_attempts = 1, 500, 10

# ---------- Choose a mode ----------
# Goal: keep asking until the player picks Classic or Time Challenge.
while True:
    print("Please pick a mode:\n")
    print("1 - CLASSIC - You have a limited number of attempts to guess the secret number.")
    print("2 - TIME CHALLENGE - You have a limited amount of time to guess the secret number.\n")
    selected_mode = input("Please enter the digit 1 or 2 to choose the mode:\n")

    if not selected_mode.isdigit() or int(selected_mode) < 1 or int(selected_mode) > 2:
        print("Invalid input!")
    else:
        selected_mode = int(selected_mode)
        print(f"You chose mode {selected_mode}")
        print("------------------------------------------------------------------------------")
        break

# ---------- Set up the round ----------
# Goal: pick the secret number (use DEBUG_SECRET when it is not None) and start the clock.
if DEBUG_SECRET is not None:
    secret_number = DEBUG_SECRET
else:
    secret_number = random.randint(low, high)

# ---------- Guess loop ----------
# Goal: keep asking for guesses until the player wins, runs out of attempts, or runs out of time.
attempts = 0
while attempts < max_attempts:
    while True:
        # Get user input
        user_guess = input(f"Please enter a number between {low}-{high}:\n")

        # Input validation
        if not user_guess.isdigit() or int(user_guess) < low or int(user_guess) > high:
            print("Invalid input")
        else:
            user_guess = int(user_guess)
            break
    
    # Increment the attempt count
    attempts += 1

    # Compare the guessed number with the secret number
    if user_guess == secret_number:
        print(f"{user_guess} is the correct number! You guessed it in {attempts} attempts. Well done!")
        break
    elif user_guess < secret_number:
        print(f"The entered number is TOO LOW! You have {max_attempts - attempts} attempts remaining.\n")
    else:
        print(f"The entered number is TOO HIGH! You have {max_attempts - attempts} attempts remaining.\n")

if user_guess != secret_number:
    print(f"You've used all your attempts. The correct number was {secret_number}. Better luck next time!")

# ---------- End of round ----------
# Goal: show the result that matches how the round ended.