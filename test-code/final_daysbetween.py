#!/usr/bin/python
# coding=utf-8

"""Credit goes to Websten from forums."""
# Use Dave's suggestions to finish your daysBetweenDates
# procedure. It will need to take into account leap years
# in addition to the correct number of days in each month."""

days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_it_a_leap_year(year):
    """Do check for leapyear."""
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    return False


def nextDay(year, month, day):
    """Do Simple version: assume every month has 30 days."""
    if month == 2 and is_it_a_leap_year(year) is True:
        days_in_month = days_per_month[month - 1] + 1
    else:
        days_in_month = days_per_month[month - 1]
    if day < days_in_month:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1


def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Do True year1-month1-day1 is before year2-month2-day2.returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Do assert and compute for days in between dates."""
    # program defensively! Add an assertion if the input is not valid!
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days


def test():
    """Do set of sample/test cases."""
    test_cases = [((2012, 1, 1, 2012, 2, 28), 58),
                  ((2012, 1, 1, 2012, 3, 1), 60),
                  ((2011, 6, 30, 2012, 6, 30), 366),
                  ((2011, 1, 1, 2012, 8, 8), 585),
                  ((1900, 1, 1, 1999, 12, 31), 36523)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"


test()
