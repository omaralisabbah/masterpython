#------------------------------------------------------
# Boolean Operators
#------------------
# [and] Logical AND
# [or] Logical OR
# [not] Logical NOT 
#------------------------------------------------------


name = " "
print(name.isspace())


print("---------------------------")

# 
print(100 < 12)
print(100 > 12)


print("---------------------------")

# True values
print(bool("True"))
print(bool(True))
print(bool(100))
print(bool(-1))


print("---------------------------")

# False values
print(bool(False))
print(bool(None))
print(bool(""))
print(bool(''))
print(bool(0))
print(bool(()))
print(bool({}))


print("---------------------------")


# [and] Logical AND Operator
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

print("------")

age = 24
country = "EGYPT"

print(age > 18 and country == "EGYPT")  # True


print("---------------------------")


# [or] Logical OR Operator
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

print("------")

age = 24
country = "EGYPT"

print(age > 25 or country == "EGYPT")  # True


print("---------------------------")


# [not] Logical NOT Operator
age = 24
country = "EGYPT"

print(not(age > 25 or country == "EGYPT"))  # False