import random
import time
# There is an issue when u get the right letter in the right spot, but then guess a word with that letter in a different spot
def main():
    """
    Main function for the Wordle game.

    This function controls the flow of the game, including welcoming the player,
    getting the target word, handling user input, and scoring the guess.
    """
    while True:
        welcome_message()
        target_word = acquire_target_word()
        count = 6
        while count > 0:
            user_guess = user_input()
            count -= 1
            score_guess(target_word, user_guess)
            if count > 1:
                time.sleep(1)
                print("You have", count, "guesses remaining")
            elif count == 1:
                time.sleep(1)
                print("THIS IS YOUR LAST GUESS, make it count...\n\n")
                time.sleep(2)

        else:
            time.sleep(1)
            print("Sorry, you have reached the maximum number of guesses.\n\n")
            time.sleep(1)
            print("The word was: ", target_word)
            try_again = input("Would you like to try again with another word? (y/n): ").lower()
            if try_again != "y":
                time.sleep(1)
                print("Maybe next time...")
                time.sleep(1)
                break
    return count

def acquire_target_word():

    """
    Read a random target word from the word bank file.

    Returns:
        str: A randomly chosen target word.
    """
    with open("word-bank/target_words.txt", "r") as file:
        lines = file.readlines()
        target_word = random.choice(lines).strip()
        return target_word

def welcome_message():
    """
    Display the welcome message and explain the game rules.

    This function prompts the user to start the game and optionally explains
    the rules of the Wordle game.
    """
    play_choice = input("\n\nWelcome to Wordle, would you like to play? (y/n): ").lower()
    if play_choice == "y":
        intro_choice = input("\nWould you like me to explain the rules? (y/n): ").lower()
        if intro_choice == "y":
            print("\nThe objective is to guess a random 5 letter 'target' word")
            time.sleep(1.5)
            print("You have 6 guesses and each guess must be a valid word in English")
            time.sleep(1.5)
            print("When you guess there is 3 possible outcomes for each letter of your guess")
            time.sleep(1.5)
            print("\tThe letter is not in the target word, you will score 0")
            time.sleep(1.5)
            print("\tThe letter is in the target word but not in the correct position, you will score 1")
            time.sleep(1.5)
            print("\tThe letter is in the target word and in the correct position, you will score 2\n")
    elif play_choice == "n":
        time.sleep(1)
        print("Maybe next time...")
        exit()
    else:
        time.sleep(1)
        print("Please enter a valid answer, 'y' or 'n'.")

def user_input():
    """
    Get the user's guess for the target word.

    This function prompts the user to enter a guess, validates the input,
    and returns the user's guess.

    Returns:
        str: The user's guess for the target word.
    """
    with open("word-bank/all_words.txt", "r") as file:
        lines = [word.strip() for word in file.readlines()]
        
    while True:
        time.sleep(1)
        user_guess = input("\nPlease enter your guess: ")
        user_guess = user_guess.lower()
        if user_guess.isalpha():
            if len(user_guess) != 5:
                print("Your guess has to be 5 letters long, please enter a word that is 5 letters long.")
                continue
            if user_guess in lines:
                return user_guess
            else:
                print("Your guess is not in our list of words. Please enter another word.")
        else:
            print("Your guess has at least one character that is not a letter, please enter a word with only letters.")

def score_guess(target_word, user_guess):
    """
    Compare the user's guess to the target word and score it.

    Args:
        target_word (str): The target word to guess.
        user_guess (str): The user's guess for the target word.

    Prints:
        list: The score for each letter of the user's guess.
        str: A message indicating whether the user guessed the word or not.
    """
    score_list = []
    target_word_count = {}
    for char in target_word:
        target_word_count[char] = target_word_count.get(char, 0) + 1

    for i, guess_char in enumerate(user_guess):
        if guess_char == target_word[i]:
            score_list.append(2)
        elif guess_char in target_word and target_word_count[guess_char] > 0:
            score_list.append(1)
            target_word_count[guess_char] -= 1
        else:
            score_list.append(0)
    time.sleep(1)
    print("Score:", score_list)
    if score_list != [2, 2, 2, 2, 2]:
        print("You did not get the word")
    else:
        print("Congratulations! You guessed the word!\n\n")
        time.sleep(1)
        print("***...YOU  WIN...***\n\n")
        time.sleep(1)
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again == "y":
            time.sleep(1)
            main()
        elif play_again == "n":
            time.sleep(1)
            exit()
        else:
            print("Please enter a valid answer, 'y' or 'n'.")

main()