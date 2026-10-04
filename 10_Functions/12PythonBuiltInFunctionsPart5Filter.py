# ------------------------------------------------------
# Python Built In Functions Part 5 Filter (VI)
# --------------------------------------------
# Filter
# Filter take a function + iterator
# Filter run a function on every element
# The function can be pre-defined function or lambda function
# Filter out all elements for which the function return true
# The function need to return boolean value
# ------------------------------------------------------
# Notes:
#   - Will only print when the condition is true
#   - 0 = False
# ------------------------------------------------------


# Use filter with pre-defined function
# Example (1)
def test_numbers(num):
    return num > 10

Numbers = [0, 0, 10, 22, 34, 45, 5, 6, 0]

data_nums = filter(test_numbers, Numbers)

print(data_nums)  # <filter object at 0x79172447caf0>

for num in filter(test_numbers, Numbers):
    print(num)


print("==============================")


# Example (2)
def test_names(name):
    return name.startswith('O')

Strings = ["Omar", "Osama", "Ahmed", "Khaled", "Wael", "Sameh", "Othman"]

data_strn = filter(test_names, Strings)

print(data_strn)  # <filter object at 0x779f60c7d300>

for strn in filter(test_names, Strings):
    print(strn)


print("==============================")


# Example (3)
# Use filter with lambda function

LambdaStrings = ["Omar", "Osama", "Ahmed", "Khaled", "Wael", "Sameh", "Othman", "Amir"]

data_rings = filter( lambda strn : strn.startswith("A"), LambdaStrings)

for str in data_rings:
    print(str)