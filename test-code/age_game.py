#!/usr/bin/python
# coding=utf-8
import msvcrt as m
# from https://docs.python.org/2/library/msvcrt.html


def pause():
    u"""Add pause to the game."""
    print
    print "press ENTER when ready..."
    print
    m.getch()


def split_number(number_value):
    u"""Split xyz to x and yz."""
    # process the user output
    number_value = str(1015 - number_value)
    # subtract value from control and coverts to string
    user_number = number_value[0]  # first string value
    user_age = number_value[1:]  # last 2 string value
    return user_number + " and is " + user_age + " yrs old"


# ask for user identity
user_name = raw_input("Who are you? ")
# start of the game
print "You will need a calculator"
pause()
print user_name.title(), "think of a number from 1 to 9"
pause()
print "then multiply it by 5"
pause()
print "then add 50"
pause()
print "multiply it by 20"
pause()
print "finally subtract the answer from the year you were born"
user_input_number = int(raw_input("What is the final answer: "))
# output the processed numbers
print
print user_name.title() + "'s lucky number is", split_number(user_input_number)
