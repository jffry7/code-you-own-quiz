#!/usr/bin/python
# coding=utf-8

"""
req D100 missing docstring.

D200 more than one line required
"""


def check_py_triplet(a, b, c):
    return a**2 + b**2 == c**2


def find_abc_product():
    total_sum = 1000
    # The maximum number that 'a' can ever be is close to 1/3 of the total sum
    max_a = total_sum/3 - 1

    for a in range(1, max_a + 1):
        b_start = a + 1
        for b in range(b_start, total_sum):
            c_start = b + 1
            for c in range(c_start, total_sum - 1):
                if a + b + c == total_sum and check_py_triplet(a, b, c):
                    return a+b+c


print find_abc_product()
