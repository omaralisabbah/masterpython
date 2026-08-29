#------------------------------------------------------
# Strings Indexing & Slicing
#---------------------------
# All data in Python is represented as objects. 
# Strings are one of the most commonly used data types in Python, and they are used to represent text. 
# Strings are sequences of characters, and they can be indexed and sliced just like lists.
#------------------------------------------------------
# Object contains elements that can be accessed using an index.
# Python uses zero-based indexing, which means that the first element of a sequence has an index of 0, the second element has an index of 1, and so on.
# Every element in a string has a unique index, starting from 0 for the first character, 1 for the second character, and so on.
# Square brackets [] are used to access the elements of a string using their index.
#------------------------------------------------------


# Indexing (Accessing individual characters in a string)
my_string = "I love Python!"
print(my_string[0])  # Output: I
print(my_string[7])  # Output: P

# Negative indexing allows you to access characters from the end of the string.
# The last character has an index of -1, the second last character has an index of -2, and so on.
print(my_string[-1])  # Output: !
print(my_string[-7])  # Output: P


print("------------------------------------------------------")


# Slicing (Extracting a portion of a string)
# Slicing allows you to extract a portion of a string by specifying a start index and an end index.
# The syntax for slicing is string[start:end], where start is the index of the first character you want to include in the slice,
# and end is the index of the first character you want to exclude from the slice.
# The slice will include all characters from the start index up to, but not including, the end index.
# If you omit the start index, the slice will start from the beginning of the string.
# If you omit the end index, the slice will go to the end of the string. You can also use negative indices in slicing.
my_string = "I love Python!"
print(my_string[2:6])  # Output: love
print(my_string[:6])   # Output: I love
print(my_string[7:])   # Output: Python!


print("------------------------------------------------------")


# Full slice (copying the entire string)
# You can create a copy of the entire string using slicing. This is done by omitting both the start and end indices in the slice.
# The resulting slice will contain all characters from the original string.
# This can be useful if you want to create a new string that is a copy of the original string,
# or if you want to create a new string that is a modified version of the original string.
# Note that strings are immutable in Python, which means that you cannot change the characters in a string once it has been created.
# However, you can create a new string that is a modified version of the original string by using slicing and concatenation.
print(my_string[:])  # Output: I love Python!


print("------------------------------------------------------")


# Slicing with step (Extracting characters at regular intervals)
# You can also specify a step value in the slice, which allows you to extract characters at regular intervals from the string.
# The syntax for slicing with a step is string[start:end:step],
# where step is the number of characters to skip between each character in the slice.
# The resulting slice will contain every step-th character from the original string,
# starting from the start index and ending at the end index (or the end of the string if the end index is omitted).
# If you omit the step value, it defaults to 1, which means that every character in the specified range will be included in the slice. 
# If you specify a negative step value, the slice will be created in reverse order, starting from the end index and moving towards the start index.
print(my_string[::1])  # Output: I love Python!
print(my_string[0::1])  # Output: I love Python!
print(my_string[::])  # Output: I love Python!
print(my_string[::2])  # Output: Ilv yhn
print(my_string[::-1])  # Output: !nohtyP evol I
print(my_string[1:10:2])  # Output:  oePt
print(my_string[::3])  # Output: Io tn