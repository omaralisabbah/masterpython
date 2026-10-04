# ------------------------------------------------------
#  Time and Date Format (Important Topics)
# ----------------------------------------
# strftime()
# Python's datetime module provides the strftime() method,
# which allows you to format date and time objects into strings according to a specified format.
# Python strftime directives are used to format date and time objects into readable strings.
# 
# %Y - Year with century as a decimal number
# %m - Month as a zero-padded decimal number
# %d - Day of the month as a zero-padded decimal number
# %A - Full weekday name
# %B - Full month name
# %I - Hour (12-hour clock) as a zero-padded decimal number
# %M - Minute as a zero-padded decimal number
# %S - Second as a zero-padded decimal number
# %p - Locale’s equivalent of either AM or PM
#
# https://strftime.org/
# ------------------------------------------------------
# Notes: 
# ------------------------------------------------------


import datetime

my_birthday = datetime.datetime(1990, 5, 15)

print(my_birthday)
print(my_birthday.strftime("%Y-%m-%d"))


print("=============================================")


print(my_birthday.strftime("%A, %B %d, %Y"))

print(my_birthday.strftime("%I:%M %p"))

print(my_birthday.strftime("%Y-%m-%d %H:%M:%S"))