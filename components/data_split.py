#!/usr/bin/python
# coding=utf-8

# friend_names = []


def data_split(data_list):
    return data_list.split()


friend_names = data_split(raw_input("List imaginry friends name: "))

print friend_names
print len(friend_names)

# data_split is redundant and more complex than .split()
# this compenent may not be needed
