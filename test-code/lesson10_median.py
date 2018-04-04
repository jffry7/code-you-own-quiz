# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.


def bigger(a, b):
    if a > b:
        return a
    else:
        return b


def biggest(a, b, c):
    return bigger(a, bigger(b, c))


"""Answer submitted
def median(a1, b1, c1):
    if bigger(a1, b1) == a1:
        if bigger(a1, c1) == a1:
            if bigger(b1, c1) == b1:
                return b1
            else:
                return c1
        else:
            return a1
    else:
        if bigger(b1, c1) == b1:
            if bigger(a1, c1) == a1:
                return a1
            else:
                return c1
        else:
            return b1
"""


def median(a, b, c):
    big = biggest(a, b, c)
    if big == a:
        return bigger(b, c)
    elif big == b:
        return bigger(a, c)
    else:
        return bigger(a, b)


print(median(1, 2, 3))
# >>> 2

print(median(9, 3, 6))
# >>> 6

print(median(7, 8, 7))
# >>> 7

print(median(2, 3, 1))
