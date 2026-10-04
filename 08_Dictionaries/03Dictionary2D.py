#------------------------------------------------------
# 2D Dictionaries in Python
#-----------------------
# 2D dictionaries are dictionaries that contain other dictionaries as values.
# This allows you to create more complex data structures, such as a collection of people, each with their own set of attributes.
#------------------------------------------------


# First 2D dictionary example
# Creating a 2D dictionary to store information about multiple people
people = {
    "person1": {
        "name": "Alice",
        "age": 30,
        "city": "New York"
    },
    "person2": {
        "name": "Bob",
        "age": 25,
        "city": "Los Angeles"
    },
    "person3": {
        "name": "Charlie",
        "age": 35,
        "city": "Chicago"
    }
}

print(people)  # Print the entire 2D dictionary

# Accessing values in a 2D dictionary
# You can access values in a 2D dictionary using their keys.
print(people["person1"]["name"])  # Output: Alice
print(people["person2"]["age"])   # Output: 25
print(people["person3"]["city"])  # Output: Chicago

print(len(people))  # Output: 3, the number of people in the dictionary
print(len(people["person1"]))  # Output: 3, the number of attributes for person1


print("--------------------------------")


# Second 2D dictionary example
# Creating a 2D dictionary to store information about multiple products

product1 = {
    "name": "Laptop",
    "price": 1000,
    "stock": 50
}

product2 = {
    "name": "Smartphone",
    "price": 500,
    "stock": 100
}

product3 = {
    "name": "Tablet",
    "price": 300,
    "stock": 75
}

products = {
    "product1": product1,
    "product2": product2,
    "product3": product3
}

print(products)  # Print the entire 2D dictionary