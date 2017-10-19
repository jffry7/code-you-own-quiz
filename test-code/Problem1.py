#!/usr/bin/python
# coding=utf-8


# Define a procedure, find_last, that takes as input two strings,
# a search string and a target string,
# and returns the last position in the search string where the target
# string appears, or -1 if there are no occurrences.
# Example: find_last('aaaa', 'a') returns 3.
# Make sure your procedure has a return statement.
# Here are test cases for you to test out:


def find_last(search_string, target_string):
    # First check to see whether the target string is even inside the search string
    if search_string.find(target_string) == -1:
        return -1
    current_location = 0
    # While the current_location is greater than -1
    while current_location >= 0:
        last_location = current_location
        # Continue to search for the next target string
        current_location = search_string.find(target_string, current_location + 1)
    return last_location


# Another method is to reverse the strings and search for the first occurrence
def find_last(search_string, target_string):
    # Use string splicing to reverse the strings
    last_location = search_string[::-1].find(target_string[::-1])
    if last_location < 0:
        return last_location
    else:
        return len(search_string) - len(target_string) - last_location


print find_last('aaaa', 'a')
# -> 3
print find_last('aaaaa', 'aa')
# -> 3

print find_last('aaaa', 'b')
# -> -1

print find_last("111111111", "1")
# -> 8

print find_last("222222222", "")
# -> 9

print find_last("", "3")
# -> -1

print find_last("", "")
# -> 0
