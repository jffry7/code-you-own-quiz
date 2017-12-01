#!/usr/bin/python
# coding=utf-8


def upper_case(nouns):
    counter = 0
    while counter < len(nouns):
        nouns[counter] = nouns[counter].title()
        counter += 1
    return nouns


friend_names = ["jeff", "tess"]
friend_names = upper_case(friend_names)
print friend_names

# upper_case is useful for uniform proper noun
# this will be used on main program
