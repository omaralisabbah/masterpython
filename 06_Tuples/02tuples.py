#------------------------------------------------------
# Tuples in Python
#-----------------
# Tuples are a collection of ordered, immutable elements.
# They are similar to lists, but unlike lists, tuples cannot be changed after they are created.
# Tuples are defined by enclosing the elements in parentheses ().
#
# Tuples elements are not unique
# Tuples can contain elements of different data types, including numbers, strings, and even other tuples.
# 
# Tuples are often used to group related data together, and they can be used as keys in dictionaries because they are hashable.
# 
# Tuple with one element requires a trailing comma, e.g., (1,)
#
# Tuple Destructuring (Unpacking) 
#------------------------------------------------------


my_first_tuple = (1, 2, 3, 4, 5)
my_second_tuple = ("apple", "banana", "cherry")

print("First Tuple:", my_first_tuple)
print("Second Tuple:", my_second_tuple)

print(type(my_first_tuple))
print(type(my_second_tuple))


print("---------------------------------------")


# Accessing Tuple Elements
print("Accessing Tuple Elements:")
print("First element of my_first_tuple:", my_first_tuple[0])
print("Last element of my_second_tuple:", my_second_tuple[-1])


print("---------------------------------------")


# Immutability of Tuples
print("Immutability of Tuples:")
try:
    my_first_tuple[0] = 10  # This will raise an error
except TypeError as e:
    print("Error:", e)


print("---------------------------------------")


# Tuples elements are not unique
third_tuple = (1, "hello", 3.14, (1, 2, 3))
print("Third Tuple:", third_tuple)
print(third_tuple[-1])  # Accessing the last element, which is another tuple
print(type(third_tuple[-1]))  # Type of the last element


print("---------------------------------------")


# Tuple with one element
single_element_tuple = (42,)
print("Single Element Tuple:", single_element_tuple)
print(type(single_element_tuple))
print("Length of Single Element Tuple:", len(single_element_tuple))

not_single_element_tuple = (42)
print("Not Single Element Tuple:", not_single_element_tuple)
print(type(not_single_element_tuple))


print("---------------------------------------")


# Tuples concatenation and repetition
print("Tuples Concatenation and Repetition:")
tuple_a = (1, 2, 3)
tuple_b = (4, 5, 6)
concatenated_tuple = tuple_a + tuple_b
repeated_tuple = tuple_a * 3
print("Concatenated Tuple:", concatenated_tuple)
print("Repeated Tuple:", repeated_tuple)


print("---------------------------------------")


# Tuple, list, and string repeatition
print("Tuple, List, and String Repetition:")
tuple_example = (1, 2, 3)
list_example = [1, 2, 3]
string_example = "abc"
print("Tuple Repetition:", tuple_example * 2)
print("List Repetition:", list_example * 2)
print("String Repetition:", string_example * 2)


print("---------------------------------------")


# count() and index() methods
print("count() and index() methods:")
sample_tuple = (1, 2, 3, 2, 4, 2)
print("Sample Tuple:", sample_tuple)
count_of_2 = sample_tuple.count(2)
index_of_3 = sample_tuple.index(3)
print("Count of 2 in Sample Tuple:", count_of_2)
print("Index of 3 in Sample Tuple:", index_of_3)


print("---------------------------------------")


# Tuple Destructuring (Unpacking)
print("Tuple Destructuring (Unpacking):")
person_info = ("Alice", 30, "Engineer")
name, age, profession = person_info
print("Name:", name)
print("Age:", age)
print("Profession:", profession)


print("---------------------------------------")


# Tuple unpacking with asterisk (*) for remaining elements
numbers = (1, 2, 3, 4, 5)
first, second, *rest = numbers
print("First:", first)
print("Second:", second)
print("Rest:", rest)  # This will be a list containing the remaining elements


print("---------------------------------------")


# Ignoring elements during unpacking
print("Ignoring elements during unpacking:")
data = (10, 20, 30, 40, 50)
first, _, third, *rest = data  # Using underscore to ignore the second element
print("First:", first)
print("Third:", third)
print("Rest:", rest)  # This will be a list containing the remaining elements