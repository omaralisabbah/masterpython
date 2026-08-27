# type() function is used to check the data type of a variable.
# All Data types in Python are classes, and variables are instances (objects) of these classes.


print(type(10))  # Output: <class 'int'>
print(type(100))  # Output: <class 'int'>
print(type(-55))  # Output: <class 'int'>

print(type(10.7))  # Output: <class 'float'>
print(type(100.0))  # Output: <class 'float'>
print(type(-55.5))  # Output: <class 'float'>

message = "Hello, Python World (Message (1))"

print(type("Hello, Python World!"))  # Output: <class 'str'> Strings are sequences of characters, and they are enclosed in either single quotes (' ') or double quotes (" ").
print(message)

print(type([1, 2, 3]))  # Output: <class 'list'> Lists are ordered collections of items, and they are enclosed in square brackets ([ ]).
print(type((1, 2, 3)))  # Output: <class 'tuple'> Tuples are ordered collections of items, and they are enclosed in parentheses (( )).
print(type({1, 2, 3}))  # Output: <class 'set'> Sets are unordered collections of unique items, and they are enclosed in curly braces ({ }).
print(type({1: 2, 3: 4}))  # Output: <class 'dict'> Dictionaries are unordered collections of key-value pairs, and they are enclosed in curly braces ({ }).

print(type(True))  # Output: <class 'bool'> Boolean values can be either True or False.
print(type(False))  # Output: <class 'bool'>

print(type(None))  # Output: <class 'NoneType'> None is a special constant in Python that represents the absence of a value or a null value.
message = "Hello, Python World (Message (2))"
print(message)


