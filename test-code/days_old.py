#!/usr/bin/python
# coding=utf-8

days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_it_a_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    return False


# print is_it_a_leap_year(2016)


def year_one(month, day):
    totaldays = days_per_month[month - 1] - day
    # adds number of days for the first month
    if month < 12:
        for counter in range(month, 12):
            # print counter, totaldays  # debug
            totaldays += days_per_month[counter]
            # did not remove the first month since python list starts at 0
            # it starts the add the following month
    return totaldays


def last_year(month, day):
    totaldays = day
    month -= 1
    for counter in range(0, month):
        totaldays += days_per_month[counter]
    return totaldays


def count_days(monthB, dayB, yearB, monthE, dayE, yearE):
    number_of_days = 0
    if yearB == yearE:
        number_of_days = dayE - dayB
    else:
        if monthB <= 2:
            if is_it_a_leap_year(yearB) is True:
                number_of_days = year_one(monthB, dayB) + 1
        else:
            number_of_days = year_one(monthB, dayB)
        # print number_of_days  # debug
        yearB += 1
        # print yearB # debug
        if yearB < yearE:
            for year_counter in range(yearB, yearE):
                if is_it_a_leap_year(year_counter) is True:
                    number_of_days += 366
                else:
                    number_of_days += 365
        if is_it_a_leap_year(yearE) is True:
            if monthE <= 2:
                number_of_days = number_of_days + last_year(monthE, dayE) + 1
        else:
            number_of_days += last_year(monthE, dayE)
    return number_of_days


print count_days(7, 6, 1964, 10, 31, 2017)
