#!/usr/bin/python
# coding=utf-8

"""This is Udacity Code your own quiz project."""
# multiple level of game difficulty
# User decides how many wrong guesses before they lose
# Game type: Fill in the blanks
# Game level: 1 ~ 4 with 5 question in each level

num_question_per_level = 4
min_number = 1
max_game_level = 4
max_question = 4


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
    # prints dashes equal to length of variable message
    print "| " + message + " |"
    print "+-" + bar(len(message)) + "-+"


def ask_question(question, target_range):
    """Do ask the generic question and return an integer."""
    # re-use the function to ask question
    # validates input to required parameter
    answer_to_question = raw_input(question)
    # check if input is a digit
    while not answer_to_question.isdigit():
        printbox(answer_to_question + " is not a digit")
        pause("Press Enter to continue....")
        # User will need to press enter to re-enter answer to question
        answer_to_question = raw_input(question)
        answer_to_question = int(answer_to_question)
        # Converts variable to integer, required for next segment
    # Check if input is within the min max range
    while answer_to_question not in range(min_number, target_range):
        printbox("Out of range")
        pause("Press Enter to continue....")
        # User will need to press enter to re-enter answer to question
        answer_to_question = raw_input(question)
        answer_to_question = int(answer_to_question)
        # Converts to integer required for checking range
    return answer_to_question


def game_settings():
    """Return the game level and mistakes allowed."""
    print "Choose the game level"
    game_level = ask_question("Choose game level from" + str(min_number) +
                              " to " + str(max_game_level) + " : ", (max_game_level + 1))
    print "Total number of question is " + str(num_question_per_level) + " times the game difficulty"
    number_of_mistakes = ask_question("How many mistake(s) allowed before the game ends? ", (num_question_per_level * game_level))
    return game_level, number_of_mistakes
