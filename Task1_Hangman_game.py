import random  

words = ["banana", "apple", "mango", "orange", "pineapple"]

secret_word = random.choice(words)

guessed_letters = []

max_wrong = 6
wrong_count = 0

print("Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have", max_wrong, "wrong guesses allowed.\n")

while wrong_count < max_wrong:

    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "  
        else:
            display += "_ "          

    print("Word:", display)
    print("Wrong guesses left:", max_wrong - wrong_count)
    print("Letters guessed so far:", guessed_letters)

    if "_" not in display:
        print("\n You Win! The word was:", secret_word)
        break

    # Ask the player to guess a letter
    guess = input("Enter a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!\n")

    # Check if the guess is correct
    elif guess in secret_word:
        guessed_letters.append(guess)
        print("Correct!\n")

    # Wrong guess
    else:
        guessed_letters.append(guess)
        wrong_count += 1
        print("Wrong!\n")

# If player used all wrong guesses
if wrong_count == max_wrong:
    print("Game Over! The word was:", secret_word)