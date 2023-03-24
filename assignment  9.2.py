#Write a txt file which has a word in each line like:
##Legs
#India
#Crow
#Rain
#Write a python code to read the file and store the words in the list
#Write a function to guess a word randomly from the list.
#Now, write a function which asks user to guess the chosen word letter by letter.
#Show "incorrect" message to the wrong guessed letter.
#Display  letters in the clue word that were guessed correctly.
#Let say word is EVAPORATE
#>>> Welcome to Hangman!
#_ _ _ _ _ _ _ _ _
#>>> Guess your letter: S
#Incorrect!
#You left with 5 chances to guess.
#>>> Guess your letter:
#E _ _ _ _ _ _ _ E
#And so on.
#1)Only let the user guess 6 times, and tell the user how many guesses they have left.
#Keep track of the letters the user guessed.
#2) If the user guesses a letter they already guessed, don’t penalize them - let them guess again.
#3)When the player wins or loses, let them start a new game.

import random

def choose_word(word_list):
    return random.choice(word_list)

def play_hangman(word):
    word_completion = '_' * len(word)
    guessed_letters = []
    guessed_words = []
    tries = 6
    print('Welcome to Hangman!')
    print(word_completion)
    while tries > 0 and word_completion != word:
        guess = input('Guess your letter: ').upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print('You already guessed the letter', guess)
            elif guess not in word:
                print(guess, 'is not in the word.')
                tries -= 1
                guessed_letters.append(guess)
            else:
                print('Good job,', guess, 'is in the word!')
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = ''.join(word_as_list)
                print(word_completion)
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print('You already guessed the word', guess)
            elif guess != word:
                print(guess, 'is not the word.')
                tries -= 1
                guessed_words.append(guess)
            else:
                word_completion = word
        else:
            print('Not a valid guess.')
        print('You have', tries, 'tries left.')
    if word_completion == word:
        print('Congratulations, you guessed the word!')
    else:
        print('Sorry, you ran out of tries. The word was', word)

    play_again = input('Do you want to play again? (yes or no)').lower()
    if play_again == 'yes':
        play_hangman(choose_word(word_list))
    else:
        print('Thanks for playing!')
