import random
with open("word_list.txt", "r", encoding="utf-8") as file:
    content = file.read().splitlines()

secret_word = random.choice(content)

lives = 6


def game():
    
    print(f"Game Started\n Rules: you have {lives}, if you reach zero, you are out.\n All letters are exaclty 5 words")
    while True:
        display = ["_", "_", "_", "_", "_"]
        guess = input("Enter a 5 letterd guess: ")
        print(secret_word)
        if len(guess) !=5:
            print("Words needs to be 5!, no lives lost")
        else:
            for i in range(5):
                if guess[i] == secret_word[i]:
                    display[i] = "🟢"
                elif guess[i] in secret_word:
                    display[i] = "🟨"
                else:
                    display[i] = "⬜"

            print(" ".join(display))
            pass


def lobby():
    welcome = input("Hello, welcome to MyWordle by Karwan, start game?\n1. yes\n2. No").casefold()
    if welcome in {"1", "yes"}:
        print("started")
        game()

lobby()
