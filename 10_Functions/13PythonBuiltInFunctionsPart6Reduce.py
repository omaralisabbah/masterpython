# ------------------------------------------------------
# Python Built In Functions Part 6 Reduce
# ---------------------------------------
# Reduce
# Reduce take a function + iterator
# Reduce run a function on the first and second element and give result
# then run the function on the result and the third element
# then run the function on the result and the fourth element and so on
# Till the one element is left and this is the result of the reduce
# The function can be pre-defined function or lambda function
# ------------------------------------------------------
# Notes:
# ------------------------------------------------------


from functools import reduce

# Use filter with pre-defined function
def sum_of_nums(num01, num02):
    return num01 + num02


numbers = [10, 22, 34, 45, 5, 6]

res = reduce(sum_of_nums, numbers)

print(res)  # (((((10 + 22) + 34) + 45) + 5) + 6)


print("=======================")


# Use filter with lambda function
res = reduce( lambda num01, num02: num01 + num02, numbers)

print(res)