#------------------------------------------------------
# Sets in Python
#-----------------
# Sets are unordered collections of unique elements.
# They are defined using curly braces {} or the set() function.
# Sets are mutable, meaning you can add or remove elements from them.
# However, since they are unordered, they do not support indexing or slicing.
#
#------------------------------------------------------

my_first_set = {1, 2, 3, 4, 5}
print("My first set:", my_first_set)

my_second_unordered_set = {"apple", 0.99, 3, 4, 5} 
print("My second set:", my_second_unordered_set)
# print("My second set:", my_second_unordered_set[0]) # This will raise an error because sets do not support indexing.


print("--------------------------------")


# Slicing can not be performed on sets because they are unordered collections.
my_third_set = {1, 2, 3, 4, 5}
# print(my_third_set[0:3]) # This will raise an error because sets do not support slicing.


print("--------------------------------")

 # This will raise an error because sets cannot contain mutable elements like lists.
# my_fourth_set = {"apple", "banana", 100, 0.99, True, [1, 2, 3]} # Error: unhashable type: 'list'

my_fourth_set = {"apple", "banana", 100, 0.99, True, (1, 2, 3)} # This is valid because tuples are immutable
print("My fourth set:", my_fourth_set)


print("--------------------------------")


my_fifth_set = {1, 2, 3, 4, "apple", "banana", 100, 0.99, True, (1, 2, 3)}
print("My fifth set:", my_fifth_set)