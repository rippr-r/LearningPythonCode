## Made by following https://www.youtube.com/watch?v=4TZ1K8EHT2M

import random

attempts = 8

word_list = [
    "python", "javascript", "hangman", "challenge", "programming",
    "development", "function", "variable", "iteration", "condition"
]

def choose_word():
    return random.choice(word_list)

word = choose_word()

word_display = ['_' for _ in word]

print("Welcome to Hangman!")
print("Guess the word, one letter at a time.")

while attempts > 0 and '_' in word_display:
    print("\nWord: " + ' '.join(word_display))
    guess = input("Enter a letter: ").lower()
    if guess in word:
        for index, letter in enumerate(word):
            if letter == guess:
                word_display[index] = guess
    else:
        print("Incorrect guess.")
        attempts -= 1

if '_' not in word_display:
    print(f"\nCongratulations! You've guessed the word: {word}")
    print(' '.join(word_display))
else:
    print(f"\nGame Over! The word was: {word}")
