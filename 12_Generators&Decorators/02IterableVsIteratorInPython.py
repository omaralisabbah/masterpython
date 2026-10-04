# ------------------------------------------------------
#  Iterable versus Iterator in Python
# -----------------------------------
# Iterable:
# In Python, an iterable is an object that can return an iterator,
# while an iterator is an object that represents a stream of data.
# [1] An iterable is an object that can be iterated (looped) over.
# [2] It implements the __iter__() method, which returns an iterator object.
# [3] Examples of iterable objects include lists, tuples, strings, dictionaries, and sets.
# ------------------------------------------------------
# Iterator:
# [1] Objects that implement the iterator protocol, which consist of the methods __iter__() and __next__().
# [2] Iterators are used to traverse through elements of a collection.
# [3] They maintain their state and know which element to yield next.
# [4] When all elements have been traversed, they raise a StopIteration exception.
# [5] Iterators can be created from iterable objects using the iter() function.
# [6] For loops in Python automatically create an iterator from an iterable object and use it to iterate over the elements.
# ------------------------------------------------------
# Notes: 
# ------------------------------------------------------


# Example of Iterable and Iterator in Python
# Example 1: Using a string (iterable) and iterating over it
String = "Hello, World!"  # This is an iterable object (a string)

for char in String:  # You can iterate over the string using a for loop
    print(char, end=" ")  # Output: H e l l o ,   W o r l d !


print("\n================================")

# Example 2: Using a list (iterable) and creating an iterator from it
my_list = [1, 2, 3, 4, 5]  # This is an iterable object (a list)
my_iterator = iter(my_list)  # This creates an iterator from the iterable

for num in my_iterator:  # You can iterate over the iterator using a for loop
    print(num, end=" ")  # Output: 1 2 3 4 5


print("\n================================")


# Example of non-iterable object
# Example 3: Using an integer (non-iterable) and trying to create an iterator from it
my_integer = 10  # This is a non-iterable object (an integer)
try:
    my_iterator = iter(my_integer)  # This will raise a TypeError
except TypeError as e:
    print(f"Error: {e}")  # Output: Error: 'int' object is not iterable


print("================================")


my_own_string = "World!"  # This is an iterable object (a string)
iterator = iter(my_own_string)  # This creates an iterator from the iterable

print(next(iterator))  # Output: W
print(next(iterator))  # Output: o
print(next(iterator))  # Output: r
print(next(iterator))  # Output: l
print(next(iterator))  # Output: d
print(next(iterator))  # Output: !
print(next(iterator))  # Output: StopIteration exception will be raised