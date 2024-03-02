# Wordle Solver

This Python script is a simple Wordle game solver. Wordle is a popular word guessing game where players have to guess a 5-letter word within six attempts.

## How to Use

1. Run the script.
2. When prompted, enter your guess (a 5-letter word).
3. Then, enter the results of your guess using the following codes:
   - 0: The letter is not in the word (grey in Wordle)
   - 1: The letter is in the word but in the wrong position (orange in Wordle)
   - 2: The letter is in the word and in the correct position (green in Wordle)

The script will then provide a list of possible words based on your input.

## Code Explanation

The script reads a list of words from a text file named "words.txt". It then prompts the user for their guess and the results of their guess. Based on this input, the script updates three lists:

- `wrongs`: Letters that are not in the word
- `possible_letters`: Letters that are in the word but not in the right position
- `rights`: Letters that are in the word and in the correct position

The script then iterates over the list of words, checking each word against these three lists. If a word passes all checks, it is added to a list of possible words (`temp_suggestion`), which is then printed to the console.
