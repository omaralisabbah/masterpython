# ------------------------------------------------------
# Python Built In Functions Part 1
# --------------------------------
# all()
# any()
# bin()
# id()
# ------------------------------------------------------


# all()
# X = [1, 2, 3, 4, 5]
X = [1, 2, 3, 4, 5, []]
if all(X):
    print("All elements is true")
else:
    print("There is at least one elements is false")


print("=========================================")


# any()
if any(X):
    print("If there is at least one element is iterable (true)")
else:
    print("There is no true elements")


print("=========================================")


# bin() - Binary number
print(bin(10))


print("=========================================")


# id() - Address
var01 = 12
var02 = 11

print(id(var01))
print(id(var02))