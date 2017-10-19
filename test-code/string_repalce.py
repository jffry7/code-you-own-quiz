#!/usr/bin/python
# coding=utf-8

# Let's go over another string method: string.replace. Use this method
# to replace the instance of NOUN with "duck" and VERB with "waddle" in the string
# sentence. For more information, visit http://www.tutorialspoint.com/python/string_replace.htm.

sentence = "A NOUN went on a walk. They can VERB really well."
sentence = sentence.replace("NOUN", "duck")
sentence = sentence.replace("VERB", "waddle")
print sentence
