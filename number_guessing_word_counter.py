
import random
from collections import Counter
import string


# Number Guessing Game
def number_guessing_game():

    print("\n--- NUMBER GUESSING GAME ---")
    print("Guess a number between 1 and 100")

    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    while attempts < max_attempts:

        try:
            guess = int(input("Enter your guess: "))

            if guess < 1 or guess > 100:
                print("Enter a number between 1 and 100!")
                continue

            attempts += 1

            if guess == secret_number:
                score = max(10, 100 - (attempts - 1) * 10)

                print("Congratulations! Correct guess.")
                print("Attempts:", attempts)
                print("Your Score:", score)
                return

            elif guess < secret_number:
                print("Too low! Try a higher number.")

            else:
                print("Too high! Try a lower number.")

            print("Attempts left:", max_attempts - attempts)

        except ValueError:
            print("Invalid input! Enter a number.")

    print("\nGame Over!")
    print("Correct number was:", secret_number)
    print("Your Score: 0")


# Word Counter
def word_counter():

    print("\n--- WORD COUNTER ---")

    filename = input("Enter text file name: ")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()

        if not text.strip():
            print("File is empty!")
            return

        # Convert text to lowercase
        text = text.lower()

        # Remove punctuation
        for symbol in string.punctuation:
            text = text.replace(symbol, "")

        words = text.split()

        word_frequency = Counter(words)

        print("\nTotal Words:", len(words))
        print("Unique Words:", len(word_frequency))

        print("\nMost Common Words:")

        for word, count in word_frequency.most_common(10):
            print(word, ":", count)

    except FileNotFoundError:
        print("File not found! Please check the filename.")

    except OSError:
        print("Unable to read the file!")


# Main Menu
while True:

    print("\n==============================")
    print(" NUMBER GAME & WORD COUNTER")
    print("==============================")

    print("1. Number Guessing Game")
    print("2. Word Counter")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        number_guessing_game()

    elif choice == "2":
        word_counter()

    elif choice == "3":
        print("Thank you! Goodbye.")
        break

    else:
        print("Invalid choice! Select 1 to 3.")
