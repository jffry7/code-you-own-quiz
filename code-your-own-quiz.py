#!/usr/bin/python
# coding=utf-8

"""This is Udacity Code your own quiz project."""
# multiple level of game difficulty
# User decides how many wrong guesses before they lose
# Game type: Fill in the blanks
# Game level: 1 ~ 4 with 5 question in each level

num_question_per_level = 4


def pause(pause_message):
    """Add pause to the game with correct message."""
    printbox(pause_message)
    raw_input()


def bar(n, ch="-"):
    """Horizontal bar on text."""
    # lesson 9 udacity
    return ch * n


def printbox(message):
    """Box bar around text."""
    # lesson 9 udacity
    print "+-" + bar(len(message)) + "-+"
    print "| " + message + " |"
    print "+-" + bar(len(message)) + "-+"


def game_difficulty():
    """Do check validity of game level and returns it."""
    print "Choose the game dificulty"
    print "Total number of question is 4 times the game difficulty"
    game_level = raw_input("Choose from 1 to 4: ")
    if game_level.isdigit():
        game_level = int(game_level)
        if game_level in range(1, 5):
            return game_level
        else:
            printbox("Out of range")
            pause("Press Enter to input game difficulty")
            game_difficulty()
    printbox("Invalid input")
    pause("Press Enter to input game dificulty")
    game_difficulty()


def mistake_question():
    mistakes = raw_input("How many mistake(s) before the game ends? ")
    return mistakes


def number_of_mistakes(game_level, num_quest):
    """DO check max number of mistake."""
    max_num_mistake = (num_quest * game_level) + 1
    mistakes = mistake_question()
    while not mistakes.isdigit():
        printbox("Invalid input")
        pause("Press Enter to input number of mistake(s)")
        mistakes = mistake_question()
    mistakes = int(mistakes)
    while mistakes not in range(1, max_num_mistake):
        print "range", mistakes
        printbox("Invalid input")
        pause("Press Enter to input number of mistake(s)")
        mistakes = mistake_question()
    return mistakes


"""if mistakes.isdigit():
        mistakes = int(mistakes)
        if mistakes in range(1, max_num_mistake):
            print "inside", mistakes
            return mistakes
        else:
            printbox("Out of range")
            pause("Press Enter to input number of mistake(s)")
            number_of_mistakes(game_level, num_quest)
    else:
        printbox("Invalid input")
        pause("Press Enter to input number of mistake(s)")
        number_of_mistakes(game_level, num_quest)"""


print number_of_mistakes(game_difficulty(), num_question_per_level)
