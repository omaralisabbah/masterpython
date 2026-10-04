#------------------------------------------------------
# Strings Methods Part 1
#-----------------------
# Strings methods are built-in functions that allow you to manipulate and work with strings in Python.
# They provide various functionalities such as searching, formatting, and modifying strings.
#------------------------------------------------------

# len()
# Returns the length of a string
a = "I Love Python!"
print(len(a))

# strip(), lstrip(), rstrip()
# These methods remove whitespace (or specified characters) from the beginning and end of a string.
x = "   Welcome, to python strip    !"
print(x.strip())
print(x.rstrip())
print(x.lstrip())

y = "@@@@@Welcome, to python strip######!"
print(y.strip("@"))
print(y.rstrip("#"))
print(y.lstrip("#@"))


print("-------------------------------")


# title()
# Converts the first character of each word to uppercase
z = "03 Strings methods part1"
print(z.title())


# capitalize()
# Converts the first character of the string to uppercase and the rest to lowercase
z = "03 Strings methods part1"
print(z.capitalize())


# zfill()
# Pads the string with zeros on the left, to fill a specified width
A, B, C = "1", "12", "115",

print(A)
print(B)
print(C)

print(A.zfill(2))
print(B.zfill(3))
print(C.zfill(4))


# upper()
# Converts all characters in the string to uppercase
name = "omar"
print(name.upper())

# lower()
# Converts all characters in the string to lowercase
name = "omar"
print(name.lower())