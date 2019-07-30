
import random
iter = 0
# A list of words that
potential_words = ["jail", "forest", "composure", "cart", "hawk", "koala"]

word = random.choice(potential_words)

# Use to test your code:
# print(word)

# Converts the word to lowercase
word = word.lower()

# Make it a list of letters for someone to guess
current_word = [] # TIP: the number of letters should match the word

for let in word:
    current_word.append("_")
print(current_word)

# Some useful variables
guesses = []
maxfails = 7
fails = 0

while fails < maxfails:
    guess = input("Guess a letter: ")
    # check if the guess is valid: Is it one letter? Have they already guessed it?
    if "_" not in current_word:
        print("you win.")

    guesses. append(guess)
    iter = 0
    for let in word:
        if let == guess:
            current_word[iter] = guess
        iter += 1
    else:
        fails
        print(current_word)
        # check if the guess is correct: Is it in the word? If so, reveal the letters!
        fails = fails+1
        print("You have " + str(maxfails - fails) + " tries left!")
