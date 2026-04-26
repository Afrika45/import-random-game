import random

def play_game(min_num, max_num):
    number = random.randint(min_num, max_num)
    attempts = 7
    used_attempts = 0

    print(f"\nI'm thinking of a number between {min_num} and {max_num}.")

    while used_attempts < attempts:
        guess = input(f"Attempt {used_attempts + 1}/{attempts} - Enter your guess: ")

        # Handle invalid input
        if not guess.isdigit():
            print("Invalid input! Please enter a valid number.")
            continue

        guess = int(guess)
        used_attempts += 1

        if guess < number:
            print("Too low")
        elif guess > number:
            print("Too high")
        else:
            print(f"Correct! You guessed it in {used_attempts} attempts 🎉")
            return True  # Player won

    # If player fails
    print(f"Game Over! The correct number was {number}.")
    return False  # Player lost


def main():
    min_num = 1
    max_num = 100

    while True:
        play_game(min_num, max_num)

        # Ask to play again
        choice = input("\nDo you want to play again? (yes/no): ").lower()
        if choice != "yes":
            print("Thanks for playing!")
            break

        # Increase difficulty
        max_num += 50
        print("Difficulty increased! New range unlocked.")


if __name__ == "__main__":
    main()