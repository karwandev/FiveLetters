import random
with open("word_list.txt", "r", encoding="utf-8") as file:
    content = file.read().splitlines()

secret_word = random.choice(content)

lives = 6
version = "1.01"

def game():
    lives_remaining = lives
    print(f"Game Started\nRules: you have {lives_remaining} lives to guess the 5-letter word.")
    # Keep each guess's letters and feedback so earlier rows stay visible on later turns.
    guess_history = []
    while lives_remaining > 0:
        display = ["_", "_", "_", "_", "_"]
        guess = input("Enter a 5-letter guess: ").strip().casefold()
        if len(guess) != 5:
            print("Your guess must be 5 letters. No life lost.")
            continue

        for i in range(5):
            if guess[i] == secret_word[i]:
                display[i] = "🟢"
            elif guess[i] in secret_word:
                display[i] = "🟨"
            else:
                display[i] = "⬜"

        # Match each letter's cell width to its square so the feedback sits beneath it.
        letters_row = "".join(f" {letter.upper()} " for letter in guess)
        feedback_row = "".join(f"{feedback} " for feedback in display)
        guess_history.append(f"{letters_row}\n{feedback_row}")
        # Redraw all rows after each guess so previous feedback remains on the board.
        print("\n".join(guess_history))

        if guess == secret_word:
            print("You guessed the word! You win!")
            return

        # Only valid guesses that do not solve the word use a life.
        lives_remaining -= 1
        print(f"Lives remaining: {lives_remaining}")

    print(f"You're out of lives! The word was {secret_word.upper()}.")


def lobby():
    while True:
        welcome = input("Hello, welcome to MyWordle by Karwan, start game?\n1. yes\n2. No\n").casefold()
        if welcome in {"1", "yes"}:
            print("started")
            game()
            break

        elif welcome in ("2", "no"):
            print("Game Not Started. but you can alwasy start.")
        elif welcome in ("3", "credits"):
            print(version)


lobby()
