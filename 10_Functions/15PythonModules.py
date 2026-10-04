# ------------------------------------------------------
# Python Modules (Built In Modules)
# ---------------------------------
# Module is a file contain a set of functions
# You can import module in your app to help you
# You can import multiple modules
# You can create your own modules
# ------------------------------------------------------
# Notes:
# ------------------------------------------------------


# Import main module
import random

# Printing random module os path
print(random)

# using function random form random module
print(f"Print random float number {random.random()}")

# Showing module's functions
print(dir(random))


print("=============================================")


# printing just a function from a module
from random import randint, random

# Calling just by the name of the function
print(f"Printing random integer {randint(100, 1000)}")