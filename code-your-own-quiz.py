#!/usr/bin/python
# coding=utf-8

"""This is Udacity Code your own quiz project."""
# multiple level of game difficulty
# User decides how many wrong guesses before they lose
# Game type: Fill in the blanks
# Game level: 1 ~ 4 with 5 question in each level
import random


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
    # Infinite loop to validates input to required parameter
    while True:
        answer_to_question = raw_input(question)
        # check if input is a digit and within range min-max
        if answer_to_question.isdigit():
            answer_to_question = int(answer_to_question)
            if answer_to_question in range(min_number, target_range):
                return answer_to_question
            else:
                printbox("Out of range, it needs to be less than " + str(target_range))
                pause("Press Enter to continue....")
                # User will need to press enter to re-enter answer to question
        else:
            printbox(answer_to_question + " is not a digit")
            # Return invalid answer and ask again
            pause("Press Enter to continue....")


def game_settings():
    """Return the game level and mistakes allowed."""
    # Defines user preferred game level
    # Defines user preferred number of guesses
    print "Choose the game level"
    game_level = ask_question("Choose game level from" + str(min_number) +
                              " to " + str(max_game_level) + " : ", (max_game_level + 1))
    # +1 is for range purpose only
    print "Total number of question is " + str(num_question_per_level) + " times the game difficulty"
    number_of_mistakes = ask_question("How many mistake(s) allowed before the game ends? ",
                                      ((num_question_per_level * game_level) + 1))
    # Range is multiple of game level
    return game_level, number_of_mistakes


# ====Global Variable====
num_question_per_level = 4
# Questions per level
min_number = 1
# Used to specify lowest number for range functions
country_capital = {
                    "Australia": "Canberra",
                    "Austria": "Vienna",
                    "Belgium": "Brussels",
                    "Botswana": "Gaborone",
                    "Canada": "Ottawa",
                    "Cyprus": "Nicosia",
                    "Honduras": "Tegucigalpa",
                    "Indonesia": "Jakarta",
                    "Ireland": "Dublin",
                    "Japan": "Tokyo",
                    "North Korea": "Pyongyang",
                    "Latvia": "Riga",
                    "Morocco": "Rabat",
                    "Philippines": "Manila",
                    "Singapore": "Singapore",
                    "Vietnam": "Hanoi"
                    }
# List of country and capital. Can be inceased manually to increase game level
# Increase by 4 or the num_question_per_level to add 1 level
# =======================

# country_keys = []
# for country in dict(country_capital):
#     country_keys.append(country)
# print random.sample(country_capital, 2)
max_game_level = len(country_capital) / num_question_per_level
country_list = []
# Initiate list for countries during game

question_multiplier, number_of_errors = game_settings()
counter = 0
while counter < question_multiplier * num_question_per_level:
    add_country_question = random.sample(country_capital, 1)
    if add_country_question not in country_list:
        country_list.append(add_country_question)
        counter += 1

print country_list
