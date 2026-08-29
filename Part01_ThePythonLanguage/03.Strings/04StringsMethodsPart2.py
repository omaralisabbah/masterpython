#------------------------------------------------------
# Strings Methods Part 2
#-----------------------
# Strings methods are built-in functions that allow you to manipulate and work with strings in Python.
# They provide various functionalities such as searching, formatting, and modifying strings.
#------------------------------------------------------


# split()
# Splits a string into a list of substrings based on a delimiter, with a maximum number of splits
a = "I Love Python! and C/C++"
print(a.split())  #

# split()
b = "I-Love-Python!-and-C/C++"
print(b.split("-"))

# split()
c = "I-Love-Python!-and-C/C++"
print(c.split("-", 2))


# rsplit()
# Starting from the right, with a maximum number of splits
d = "I-Love-Python!-and-C/C++"
print(d.rsplit("-", 2))

# rsplit()
# Starting from the left, with a maximum number of splits
d = "I-Love-Python!-and-C/C++"
print(d.rsplit("-", 3))


print("-------------------------------------------")


# center()
e = "Omar"
print(e.center(10))  # Spaces Default
print(e.center(8, '#'))  # Hashes
print(e.center(8, '@'))  # @


print("-------------------------------------------")


# count()
f = "I am going to learn python, becaues I want to learn ROS2"
print(f.count("g"))  # Spaces Default
print(f.count("I", 0, 25))  # Hashes


print("-------------------------------------------")


# swapcase()
g = "I am going to learn python, becaues I want to learn ROS2"
h = "I am going to learn python, becaues I want to learn ROS2"
print(g.swapcase())  # 
print(h.swapcase())  # 


print("-------------------------------------------")


# startswith()
i = "I am going to learn python, Becaues I want to learn ROS2"
print(i.startswith("I"))  # 
print(i.startswith("B"))  # 
print(i.startswith("R"))  # 



print("-------------------------------------------")


# endswith()
j = "I am going to learn python, becaues I want to learn ROS2"
print(i.endswith("2"))  # 
print(i.endswith("s"))  # 
print(i.endswith("e", 2, 8))  # 