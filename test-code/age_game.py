#!/usr/bin/python
# coding=utf-8


def split_number(number_value):
    number_value = str(1015 - number_value)
    user_number = number_value[0]
    user_age = number_value[1:]
    return "your lucky number is " + user_number + " and your age is " + user_age


user_name = raw_input("Who are you? ")
print "Think of a number from 1 to 9 then multiply it by 5."
print "the add 50"
print "multiply it by 20"
print "finally subtract the answer from the year you were born"
user_input_number = int(raw_input("Let me evaluate: "))
print "Hello", user_name, "!!!"
print split_number(user_input_number)
