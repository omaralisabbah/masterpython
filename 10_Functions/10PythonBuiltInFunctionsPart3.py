# ------------------------------------------------------
# Python Built In Functions Part 3
# --------------------------------
# abs()
# pow()
# min()
# max()
# slice()
# ------------------------------------------------------
# Notes:
# ------------------------------------------------------

# abs()
print(abs(110))
print(abs(-10))
print(abs(-0.99))

print("=======================")

# pow(base, exp, mod) - Power
print(pow(2, 8))  # 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2
print(pow(2, 9))
print(pow(2, 10))
print(pow(2, 10, 6))  # (2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2) % 4

print("=======================")

# min(item, item, ... or iterator) - But not two different types
print(min(1, 14, 15, 15, -5))
print(min("1", "14", "15", "15", "-5"))
print(min(1, 14, 17, 15, -5))

print("=======================")

# max(item, item, ... or iterator) - But not two different types
print(max(1, 14, 15, 15, -5))
print(max("1", "14", "15", "15", "-5"))
print(max(1, 14, 17, 15, -5))

print("=======================")

# slice()
list = ["A", "B", "C", "D", "E"]
print(list[:])
print(list[:3])
print(list[2:5])

print("===============")

print(list[slice(3)])
print(list[slice(3, 5)])