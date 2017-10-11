#!/usr/bin/python
# coding=utf-8

"""
req D100 missing docstring.

D200 more than one line required
"""
import re
print('Hello world!')
# Python Program to convert temperature in celsius to fahrenheit


for test_string in ['555-1212', 'ILL-EGAL']:
    if re.match(r'^\d{3}-\d{4}$', test_string):
        print test_string, 'is a valid US local phone number'
    else:
        print test_string, 'rejected'
