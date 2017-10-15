#!/usr/bin/python
# coding=utf-8

"""
req D100 missing docstring.

D200 more than one line required
"""
sentence = "A NOUN went on a walk."
substring = sentence[sentence.find(" ", sentence.find("NOUN")):]
print substring
