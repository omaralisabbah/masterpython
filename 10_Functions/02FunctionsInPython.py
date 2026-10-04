#------------------------------------------------------
# Functions In Python
#--------------------
# Functions are reusable blocks of code designed to perform a specific task.
# Instead of writing the same logic again and again, we wrap it in a function and simply call it whenever needed.
#
# The most important thing you should know about functions is:
#   - Function Definition (The keyword 'def' is used to define a function in Python.)
#   - Function Usage (calling or invoking)
#
# Functions with Parameters
#   - We can also pass data to functions using parameters
#   - These act as input variables for the function
#   - You can define multiple parameters separated by commas.
#------------------------------------------------------


# Function Definition
def my_first_python_function():
    print("This is my first python function")

# Calling the function by using its name followed by parentheses.
my_first_python_function()

var = my_first_python_function()
print(var)


print("==============================================")


a, b, c = "01", "02", "03"

# print(f"Hola, {a}")
# print(f"Hola, {b}")
# print(f"Hola, {c}")


# Functions with Parameters
def say_Hola(name):
    print(f"Hola, {name} Willkommen!")

say_Hola("Wael")


print("==============================================")


# Functions with Multiple Parameters
def tea_with_recipe(flavor, no_of_cups):
    print(f"Preparing {no_of_cups} cups of {flavor} tea")

tea_with_recipe("Arosa", 3)


print("==============================================")


# Real example
def full_name(first, middle, last):
    print(
        f"Willkommen, {first.strip().capitalize()} {middle.strip().capitalize():.1s}. {last.strip().capitalize()}"
    )

full_name("Omar   ", "        Ali ", "Sabbah")
