#------------------------------------------------------
# Dictionary Methods Part 1
#--------------------------
# clear() method removes all items from the dictionary.
# copy() method returns a shallow copy of the dictionary.
# update() method updates the dictionary with elements from another dictionary or from an iterable of key-value pairs.
# keys() method returns a view object that displays a list of all the keys in the dictionary.
# fromkeys() method creates a new dictionary with keys from the given iterable and values set to the specified value.
# values() method returns a view object that displays a list of all the values in the dictionary.
#------------------------------------------------------


# clear() method removes all items from the dictionary.
user_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

print("Original Dictionary:", user_dict)
user_dict.clear()  # This will clear all items from the dictionary.
print("Dictionary after clear():", user_dict)


print("------------------------------------------------------")


# copy() method returns a shallow copy of the dictionary.
original_dict = {
    "name": "Alice",
    "age": 25,
    "city": "Los Angeles"
}

copied_dict = original_dict.copy()  # This will create a shallow copy of the dictionary.
print("Original Dictionary:", original_dict)
print("Copied Dictionary:", copied_dict)


print("------------------------------------------------------")


# update() method updates the dictionary with elements from another dictionary or from an iterable of key-value pairs.
dict1 = {
    "name": "Bob",
    "age": 35
}
dict2 = {
    "city": "Chicago"
}

print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)

dict1.update(dict2)  # This will update dict1 with elements from dict2.
print("Dictionary 1 after update():", dict1)
dict1.update({"age": 36})  # This will update the value of the key "age" in dict1.
print("Dictionary 1 after updating age:", dict1)


print("------------------------------------------------------")


# keys() method returns a view object that displays a list of all the keys in the dictionary.
sample_dict = {
    "name": "Charlie",
    "age": 28,
    "city": "Miami"
}
print("Keys in the dictionary:", list(sample_dict.keys()))


# fromkeys() method creates a new dictionary with keys from the given iterable and values set to the specified value.
keys = ["name", "age", "city"]
new_dict = dict.fromkeys(keys, "Unknown")  # This will create a new dictionary with keys from the list and values set to "Unknown".
print("New Dictionary from keys:", new_dict)


print("------------------------------------------------------")

# values() method returns a view object that displays a list of all the values in the dictionary.
sample_dict = {
    "name": "David",
    "age": 32,
    "city": "Seattle"
}

print("Values in the dictionary:", list(sample_dict.values()))  