#!/usr/bin/python
# coding=utf-8

sentence = "A NOUN went on a walk."
substring = sentence[sentence.find(" ", sentence.find("NOUN")):]
print substring
