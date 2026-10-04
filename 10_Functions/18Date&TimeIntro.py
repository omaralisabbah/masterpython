# ------------------------------------------------------
# Date and Time Introduction (Important Topics)
# ---------------------------------------------
# This script demonstrates the usage of the datetime module in Python,
# which provides classes for manipulating dates and times.
# 
# ------------------------------------------------------
# Notes: 
# ------------------------------------------------------


import datetime

print(dir(datetime))
print(dir(datetime.datetime))

# Printing the current date and time
print(datetime.datetime.now())


print("=============================================")


# Printing the current year
print(datetime.datetime.now().year)

# Printing the current month
print(datetime.datetime.now().month)

# Printing the current day
print(datetime.datetime.now().day)


print("=============================================")


# Printing the start and the end of a date
print(datetime.datetime.min)
print(datetime.datetime.max)


print("=============================================")


# Printing the current time
# print(dir(datetime.datetime.now().time()))
print(datetime.datetime.now().time())
print(datetime.datetime.now().time().hour)
print(datetime.datetime.now().time().minute)
print(datetime.datetime.now().time().second)


print("=============================================")


# Printing the start and the end of time
print(datetime.time.min)
print(datetime.time.max)


print("=============================================")


# Printing a specific date and time
print(datetime.datetime(2024, 6, 18, 12, 30, 45))
print(datetime.datetime(2024, 6, 18, 12, 30, 45).year)
print(datetime.datetime(2024, 6, 18, 12, 30, 45).month)
print(datetime.datetime(2024, 6, 18, 12, 30, 45).day)
print(datetime.datetime(2024, 6, 18, 12, 30, 45).hour)
print(datetime.datetime(2024, 6, 18, 12, 30, 45).minute)
print(datetime.datetime(2024, 6, 18, 12, 30, 45).second)


print("=============================================")


# Birthday Example
my_birthday = datetime.datetime(1990, 5, 15, 10, 30, 0)
print("My Birthday:", my_birthday)

# Printing my age based on my birthday
current_date = datetime.datetime.now()
age = current_date.year - my_birthday.year - ((current_date.month, current_date.day) < (my_birthday.month, my_birthday.day))
print("My Age:", age)

# Alternative way to calculate age using timedelta
print("My Age (Alternative):", (current_date - my_birthday).days // 365)  # Approximate age in years