# ------------------------------------------------------
# Python Built In Functions Part 7
# --------------------------------
# enumerate()
# help()
# reversed()
# ------------------------------------------------------
# Notes:
# ------------------------------------------------------


# enumerate(iterable, start=0)
List = ["00", "01", "02", "03", "04", "05", "06"]

ListCounter = enumerate(List, 10)

for counter, num in ListCounter:
    print(f"{counter} - {num}")

print(type(ListCounter))  # <class 'enumerate'>


print("=======================")


# help()
# print(help(print))
# print(help(enumerate))


print("=======================")


# reversed(iterable)
String = "Robototype"
print(reversed(String))

for char in reversed(String):
    print(char)