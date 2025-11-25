import random
def play_guessing_game():
    lower_bound = 1
    upper_bound = 100
    secret_number = random.randint(lower_bound, upper_bound)
    attempts = 0
    max_attempts = 7 # Adjust for desired difficulty
    guessed_correctly = False
    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")
    print(f"You have {max_attempts} attempts to guess it.")
    while attempts < max_attempts:
        try:
            player_input = input("What's your guess? ")
            guess = int(player_input)
            attempts += 1
            if not (lower_bound <= guess <= upper_bound):
                print(f"Please enter a number between {lower_bound} and {upper_bound}.")
                continue # Don't count this as an attempt if out of bounds
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                guessed_correctly = True
                break # Exit loop on correct guess
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue # Don't count this as an attempt for invalid input
    if guessed_correctly:
        print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
    else:
        print(f"Game over! You ran out of attempts.")
        print(f"The secret number was {secret_number}.")
# Call the function to start the game
play_guessing_game()
