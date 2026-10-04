#------------------------------------------------------
# 2D Dictionaries in Python
#-----------------------
# 2D dictionaries are dictionaries that contain other dictionaries as values.
# This allows you to create more complex data structures, such as a collection of people, each with their own set of attributes.
#
# When we studied lists, we focused on the order of elements.
# In a list, order matters — we access values using their index positions (0, 1, 2...).
# Example: items[0] gives the first element.
#
# But what if the *order* doesn’t matter, and instead we care about mapping a specific key to a specific value?
# That’s where dictionaries come in!
#------------------------------------------------------


# First dictionary example
# Creating a dictionary to store information about a person
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Accessing values in a dictionary
# You can access values in a dictionary using their keys.
print(person["name"])  # Output: Alice
print(person["age"])   # Output: 30 
print(person["city"])  # Output: New York
print(person)  # Print a blank line for better readability