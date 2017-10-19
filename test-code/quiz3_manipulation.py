#!/usr/bin/python
# coding=utf-8

s = 'test'
print ('a' + s)[1:]  # a+'string' then prints 1-end. it exclude a
print s[0] + s[1:]  # will not work if s=''
print s + ''  # it adds null ''
print s[0:]  # it prints from first char and doesnt cause error for ''
