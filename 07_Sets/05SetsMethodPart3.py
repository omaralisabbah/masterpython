#------------------------------------------------------
# Sets Methods Part 3
#--------------------
# issubset() - Returns True if all elements of the set are present in another set, otherwise returns False.
# issuperset() - Returns True if the set contains all elements of another set, otherwise returns False.
# isdisjoint() - Returns True if two sets have no elements in common, otherwise returns False.
#------------------------------------------------------


# issubset() - Returns True if all elements of the set are present in another set, otherwise returns False.
setU = {1, 2, 3}
setV = {1, 2, 3, 4, 5}
is_subset = setU.issubset(setV)
print("Is set U a subset of set V?", is_subset)  # Output: Is set U a subset of set V? True
print("Is set V a subset of set U?", setV.issubset(setU))  # Output: Is set V a subset of set U? False


print("------------------------------------------------------")


# issuperset() - Returns True if the set contains all elements of another set, otherwise returns False.
setW = {1, 2, 3, 4, 5}
setX = {1, 2, 3}
is_superset = setW.issuperset(setX)
print("Is set W a superset of set X?", is_superset)  # Output: Is set W a superset of set X? True
print("Is set X a superset of set W?", setX.issuperset(setW))  # Output: Is set X a superset of set W? False


print("------------------------------------------------------")


# isdisjoint() - Returns True if two sets have no elements in common, otherwise returns False.
setY = {1, 2, 3}
setZ = {4, 5, 6}
is_disjoint = setY.isdisjoint(setZ)
print("Are set Y and set Z disjoint?", is_disjoint)  # Output: Are set Y and set Z disjoint? True
print("Are set Y and set U disjoint?", setY.isdisjoint(setU))  # Output: Are set Y and set U disjoint? False