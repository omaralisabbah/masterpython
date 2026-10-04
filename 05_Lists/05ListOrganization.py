#------------------------------------------------------
# List Organization
#------------------
#
#------------------------------------------------------


# clear() - removes all elements from the list
first_list = ["first", "second", "third"]
first_list.clear()
print(first_list)  # []


print("--------------------------------------")


# copy() - returns a shallow copy of the list
first_list = ["first", "second", "third"]
second_list = first_list.copy()

print(first_list)  # ['first', 'second', 'third']
print(second_list)  # ['first', 'second', 'third']

# Shallow copy means that the new list is a separate object, but the elements themselves are still references to the same objects in memory.
# Therefore, if you modify an element in one list, it will not affect the other list.

first_list.append("fourth")
print(first_list)  # ['first', 'second', 'third', 'fourth']
print(second_list)  # ['first', 'second', 'third']


print("--------------------------------------")


# count() - returns the number of occurrences of a specified element in the list
first_list = ["first", "second", "third", "first"]
count_first = first_list.count("first")
print(count_first)  # 2


print("--------------------------------------")


# index() - returns the index of the first occurrence of a specified element in the list
first_list = ["first", "second", "third", "first"]
index_first = first_list.index("first")
print(index_first)  # 0 - The index of the first occurrence of "first" is 0


print("--------------------------------------")


# insert() - inserts an element at a specified index in the list
first_list = ["first", "second", "third"]
first_list.insert(1, "inserted")
print(first_list)  # ['first', 'inserted', 'second', 'third']
first_list.insert(-1, "inserted")
print(first_list)  # ['first', 'inserted', 'second', 'inserted', 'third']


print("--------------------------------------")


# pop() - removes and returns the element at a specified index in the list
first_list = ["first", "second", "third"]
popped_element = first_list.pop(1)
print(popped_element)  # 'second'
print(type(popped_element))  # <class 'str'>
print(first_list)  # ['first', 'third']