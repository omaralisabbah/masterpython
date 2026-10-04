# -------------------------------------------
# Strings Concatenation
# ---------------------------
# 
# -------------------------------------------

my_string = "Hello, "
my_string += "World!"
print(my_string)

msg = "I love"
language = "Python!"
# Concatenating strings using the + operator
concatenated_string = msg + " " + language
print(concatenated_string)  # Output: I love Python! Python

x = "I love"
y = "Python!"
# Concatenating strings using the join() method
concatenated_string = " ".join([x, y])
print(concatenated_string)  # Output: I love Python!