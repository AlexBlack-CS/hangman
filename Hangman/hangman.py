""" File: hangman.py
    Programmer: Alexander Black
    Description: This program is to play a game of hangman
"""
from random import choice

def main():
    """ Main function containing outline calls to play hangman """
    play_hangman()


#PLACE YOUR OTHER FUNCTION defINITIONS HERE

def load_words(filename):
    words = []
    with open(filename, 'r') as file:
        for line in file:
            words.append(line.strip())
    return words

def get_valid_guess(guessed_letters):
    while True:
        guess = input("Enter a letter: ").lower()
        if len(guess) == 1 and guess not in guessed_letters and guess in "abcdefghijklmnopqrstuvwxyz":
            return guess
        print("Invalid input. Enter a single, unused letter.")

def display_status(word, guessed_letters, remaining_guesses):
    display_word = ''
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += '_'
    print("\nWord: " + display_word)
    print("Guessed letters: " + ', '.join(sorted(guessed_letters)))
    print("Remaining incorrect guesses: " + str(remaining_guesses))

def play_hangman():
    words = load_words("dictionary.txt")
    word = choice(words)
    guessed_letters = set()
    remaining_guesses = int(input("Enter allowed incorrect guesses: "))
    
    while remaining_guesses > 0:
        display_status(word, guessed_letters, remaining_guesses)
        guess = get_valid_guess(guessed_letters)
        guessed_letters.add(guess)
        
        if guess not in word:
            remaining_guesses -= 1
            print("Incorrect guess!")
        
        correct = True
        for letter in word:
            if letter not in guessed_letters:
                correct = False
                break
        
        if correct:
            print("Congratulations! You guessed the word: " + word)
            return
    
    print("Game over! The word was: " + word)

if __name__ == "__main__":
    main()

