#------------------------------------------------------
# Type Conversion
#----------------
# Note: The set conversion
# Check the errors types
#------------------------------------------------------


# str()
strong = 10
print(type(strong))
print(type(str(strong)))

variab = 10.0
print(type(variab))
print(type(str(variab)))


print("------------------------")


# tuple()
example_a = "Omar"
example_b = [12, 124, 15, 65, 16]  # List
example_c = {"Cx", "Cy", "Cz"}  # Set
example_d = {"Cx": 12, "Cy": 41, "Cz": 14}  # Dictionary

print(tuple(example_a))
print(tuple(example_b))
print(tuple(example_c))
print(tuple(example_d))


print("------------------------")


# list()
example_e = "Omar"  # String
example_f = (12, 124, 15, 65, 16)  # Tuple
example_g = {"Cx", "Cy", "Cz"}  # Set
example_h = {"Cx": 12, "Cy": 41, "Cz": 14}  # Dictionary

print(list(example_e))
print(list(example_f))
print(list(example_g))
print(list(example_h))


print("------------------------")


# set()
example_i = "Omar"  # String
example_j = (12, 124, 15, 65, 16)  # Tuple
example_k = ["Cx", "Cy", "Cz"]  # List
example_l = {"Cx": 12, "Cy": 41, "Cz": 14}  # Dictionary

print(set(example_i))
print(set(example_j))
print(set(example_k))
print(set(example_l))


print("------------------------")


# dict()
example_m = "Omar"  # String
example_n = (12, 124, 15, 65, 16)  # Tuple
example_o = ["Cx", "Cy", "Cz"]  # List
example_p = {"Cxx", "Cyy", "Czz"}  # Set

# print(dict(example_m))  # Error: You can not change string to dictionary
# print(dict(example_n))  # Error: Wait
# print(dict(example_o))  # Error: Wait
# print(dict(example_p))  # Error : You can not change Set to dictionary


print("------------------------")


# How to avoid conversion errors
example_n = (("W", 12), ("X", 122), ("Y", 65), ("Z", 1))  # Tuple
example_o = [["First", 1], ["Second", 2], ["Third", 3]]  # List

print(dict(example_n))
print(dict(example_o))