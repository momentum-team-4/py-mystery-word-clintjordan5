file = open("words.txt")
text = file.read().split()
# print(text)

import string
import random
# print(text)
# imports random words from text file

# set range of word length, convert to uppercase
level_one = [
    word.upper()
    for word in text
    if 4 <= len(word) <= 6
]
# 4 to 6 letters

level_two = [
    word.upper()
    for word in text
    if 6 <= len(word) <= 8
]
# 6 to 8 letters

level_three = [
    word.upper()
    for word in text
    if 8 <= len(word) <= 10
]
# 8 to 10 letters


def get_word_difficulty():
    difficulty = input('Select Difficulty (1 - One, 2 - Two, 3 - Three): ')
    if difficulty == '1':
        word = random.choice(level_one)
    elif difficulty == '2':
        word = random.choice(level_two)
    elif difficulty == '3':
        word = random.choice(level_three)
    else:
        return get_word_difficulty
    print(f'Word has {len(word)} letters.')
    return word
# https://docs.python.org/3/tutorial/controlflow.html
# using elif and else if


attempt_list = []
# called in function below


def get_attempt_list(attempt_list):
    attempt = input('Choose a letter: ').upper()
    attempt_list.append(attempt)
    return attempt_list
# able to see in output


def hangman_word(word, attempt_list):
    return (letter if letter in attempt_list else '_' for letter in word)
# builds the  _ _ _ _


def wrong_letters(word, attempt_list):
    return sorted(set(
        letter
        for letter in attempt_list
        if not letter in word
    ))
# https://docs.python.org/3/library/functions.html#sorted


def play_game(word):
    attempt_list = []
    while True:
        attempts_left = 8 - len(wrong_letters(word, attempt_list))
        # takes 8 attempts and subtracts length of wrong attempts
        print(f'Hangman: {" ".join(hangman_word(word, attempt_list))}')
        print(f'Wrong Letters: {" ".join(wrong_letters(word, attempt_list))}')
        print(f'There are {attempts_left} attempts left.')
        # can see in terminal output

        if '_' not in hangman_word(word, attempt_list):
            print(f'Correct, you got {word}')
            play_again()
            return
        if attempts_left == 0:
            print(f'Wrong, correct answer is {word}.')
            play_again()
            return
        attempt_list = get_attempt_list(attempt_list)
# shows correct word once out of attempts

def play_again():
    if input('Play Again? (y/n): ') == 'y':
        new_word = get_word_difficulty()
        play_game(new_word)
        return


if __name__ == '__main__':
    word = (get_word_difficulty())
    play_game(word)
