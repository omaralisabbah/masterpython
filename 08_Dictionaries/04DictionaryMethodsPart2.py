#------------------------------------------------------
# Dictionary Methods Part 2
#--------------------------
#
#------------------------------------------------------


# setdefault() method
# The setdefault() method returns the value of a key (if the key is in dictionary). If not, it inserts the key with a specified value.
# Syntax: dict.setdefault(key, default=None)
user_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Using setdefault() to get the value of an existing key
name_value = user_dict.setdefault("name", "Default Name")
print("Value of 'name':", name_value)  # Output: John


print("------------------------------------------------------")


# pop() method
# The pop() method removes the specified key and returns the corresponding value.
# Syntax: dict.pop(key, default=None)
product_dict = {
    "product": "Laptop",
    "price": 1200,
    "brand": "Acer"
}

# Using pop() to remove a key and get its value
removed_value = product_dict.pop("price")
print("Removed value:", removed_value)  # Output: 1200
print("Dictionary after pop():", product_dict)  # Output: {'product': 'Laptop', 'brand': 'Acer'}


print("------------------------------------------------------")


# popitem() method
# The popitem() method removes and returns the last inserted key-value pair as a tuple.
# Syntax: dict.popitem()
settings_dict = {
    "theme": "dark",
    "notifications": True,
    "language": "English"
}

# Using popitem() to remove the last inserted key-value pair
last_item = settings_dict.popitem()
print("Last inserted item removed:", last_item)  # Output: ('language', 'English')
print("Dictionary after popitem():", settings_dict)  # Output: {'theme': 'dark', 'notifications': True}


print("------------------------------------------------------")


# item() method
# The items() method returns a view object that displays a list of a dictionary's key-value pairs.
# Syntax: dict.items()
user_info = {
    "username": "johndoe",
    "email": "johndoe@example.com"
}

# Using items() to get all key-value pairs
for key, value in user_info.items():
    print(f"{key}: {value}")


print("------------------------------------------------------")


# fromkeys() method
# The fromkeys() method returns a new dictionary with keys from the specified iterable and values set to a specified value.
# Syntax: dict.fromkeys(iterable, value)
keys = ["a", "b", "c"]
# Using fromkeys() to create a new dictionary with default values
new_dict = dict.fromkeys(keys, 0)
print("New dictionary created using fromkeys():", new_dict)  # Output: {'a': 0, 'b': 0, 'c': 0}

value = "X"
new_dict_with_value = dict.fromkeys(keys, value)
print("New dictionary created using fromkeys() with custom value:", new_dict_with_value)  # Output: {'a': 'X', 'b': 'X', 'c': 'X'}