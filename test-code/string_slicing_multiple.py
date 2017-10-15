#!/usr/bin/python
# coding=utf-8

"""
req D100 missing docstring.

D200 more than one line required
"""
# Use string slicing to store everything before "NOUN" in substring1,
# everything after "NOUN" and before "VERB" in substring2,
# and everything after "VERB" in substring3.
sentence = "A NOUN went on a walk. It can VERB really fast."
substring1 = sentence[:sentence.find("NOUN")]
substring2 = sentence[sentence.find(" ", sentence.find("NOUN")): sentence.find("VERB")]
substring3 = sentence[sentence.find(" ", sentence.find("VERB")):]
noun_replacement = "dog"  # your noun here
verb_replacement = "walk"  # your verb here

new_sentence = substring1 + noun_replacement + substring2 + verb_replacement + substring3
# your code here
print new_sentence
