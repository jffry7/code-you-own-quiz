#!/usr/bin/python
# coding=utf-8


def pause(pause_message):
    u"""Add pause to the game."""
    printbox(pause_message)
    raw_input()


def bar(n, ch="-"):
    u"""Horizontal bar on text."""
    # lesson 9 udacity
    return ch * n


def printbox(message):
    u"""Box bar around text."""
    # lesson 9 udacity
    print "+-" + bar(len(message)) + "-+"
    print "| " + message + " |"
    print "+-" + bar(len(message)) + "-+"


def split_number(number_value, year_value):
    u"""Split xyz to x and yz."""
    # process the user output
    number_value = str(year_value - 1000 - number_value)
    # subtract value from control and coverts to string
    # user_number = number_value[0]  # first string value
    # user_age = number_value[1:]  # last 2 string value
    # modified to return 2 values
    return number_value[0], number_value[1:]


user_name = raw_input("Who are you? ")
# Added the year factor as it will vary if played years after it was created
current_year = int(raw_input("What is the current year? "))
# Start of the game
print "Press Enter to proceed."
pause("You may need a calculator")
first_message = ", think of a number from 1 to 9"
print bar(len(user_name.title()) + len(first_message))  # 31 is the len() of next line
# Add bar separator for the instruction set
print user_name.title() + first_message
print "then multiply it by 5"
print "then add 50"
print "multiply it by 20"
pause("Press ENTER when ready...")
print "Lastly, your birth year minus the answer above"
print
user_input_number = abs(int(raw_input("What is the final answer: ")))
# output the processed numbers
print
user_number, user_age = split_number(user_input_number, current_year)
printbox(user_name.title() + "'s lucky number is " + user_number)
printbox(" and is " + user_age + " yrs old")
# print "+-" + bar(len(split_number(user_input_number, current_year))) + "-+"
# print "| " + split_number(user_input_number, current_year) + " |"
# print "+-" + bar(len(split_number(user_input_number, current_year))) + "-+"
# print user_name.titlre() + "'s lucky number is", split_number(user_input_number, current_year)
