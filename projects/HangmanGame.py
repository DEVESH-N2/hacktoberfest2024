import random

words = ["python", "hangman", "challenge", "programming"]
word = random.choice(words)
guessed = "_" * len(word)
attempts = 6

while attempts > 0 and "_" in guessed:
    print("Word:", guessed)
    guess = input("Guess a letter: ").lower()
    if guess in word:
        guessed = "".join([c if c == guess else g for c, g in zip(word, guessed)])
    else:
        attempts -= 1
        print(f"Wrong! Attempts left: {attempts}")

if "_" not in guessed:
    print("Congratulations! You guessed the word:", word)
else:
    print("Game over! The word was:", word)
