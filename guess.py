import random
import time

# ---------- Settings ----------
DEBUG_SECRET = None   # For testing, set to a number such as 42. Set back to None before your final commit.
TIME_LIMIT = 60       # Seconds allowed in Time Challenge mode
LOW = 1               # Hardcoded lower limit
HIGH = 50             # Hardcoded upper limit

print("Welcome to the Number Guessing Game")

# ---------- Choose a level ----------
# Goal: keep asking until the player picks a valid level, then set the range and attempt limit.

# ---------- Choose a mode ----------
# Goal: keep asking until the player picks Classic or Time Challenge.

# ---------- Set up the round ----------
# Goal: pick the secret number (use DEBUG_SECRET when it is not None) and start the clock.
secret_number = random.randint(1, 50)

# ---------- Guess loop ----------
# Goal: keep asking for guesses until the player wins, runs out of attempts, or runs out of time.
attempts = 0
while True:
    while True:
        # Get user input
        user_guess = input(f"Please enter a number between {LOW}-{HIGH}:\n")

        # Input validation
        if not user_guess.isdigit() or int(user_guess) < LOW or int(user_guess) > HIGH:
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
        print(f"The entered number is TOO LOW!")
    else:
        print(f"The entered number is TOO HIGH!")



# ---------- End of round ----------
# Goal: show the result that matches how the round ended.