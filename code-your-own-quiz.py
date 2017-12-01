#!/usr/bin/python
# coding=utf-8

"""This is Udacity Code your own quiz project."""
# multiple level of game difficulty
# User decides how many wrong guesses before they lose
# Game type: Fill in the blanks
# Game level: 1 ~ 4 with 5 question in each level


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
    valid_levels = ["1", "2", "3", "4"]
    for val_level in valid_levels:
        print game_level, val_level
        if game_level == val_level:
            return game_level
    printbox("Invalid input")
    pause("Press Enter to input game dificulty")
    game_difficulty()


print game_difficulty()
