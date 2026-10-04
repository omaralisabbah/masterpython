#------------------------------------------------------
# Functions Packing and Unpacking Arguments
#--------------------------------
#   - *Args
#   - Unknown Number of Arguments
#   - Function Default Parameters
#   - Keyword Arguments
#   - Arbitrary Arguments (*kwargs)
#   - Keyword Arbitrary Arguments (**kwargs)
#------------------------------------------------------


# Main Idea
print(1, 2, 3, 4, 5)

List = [1, 2, 3, 5, 6]

print(List)
print(*List)


print("==============================================")


def Willkommen(var1, var2, var3, var4):
    variables = [var1, var2, var3, var4]

    for var in variables:
        print(f"Hola, {var}")


Willkommen("AK-47", "AR-15-Tactical", "JamesBond", "John Wick")


print("==============================================")


# But, If you Do not know the number of Arguments
def Willkommen(*variables):

    for var in variables:
        print(f"Hola, {var}")


Willkommen("AK-47", "AR-15-Tactical", "JamesBond", "John Wick01", "John Wick02", "John Wick03", "John Wick04")


print("==============================================")


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def Function(name, age="Unknown", nationality="Unknown"):
    print(f"Hello, {name}, your age is: {age} and your nationality is: {nationality}")

Function("Omar", "22", "EGYPTIAN")
Function("Omar", "22")
Function("Omar")


print("==============================================")


# Keyword Arguments
# You can also pass arguments by naming them explicitly.

def describe_tea(flavor, strength):
    print(f"{flavor} Tea - {strength} strength")

describe_tea(strength="Strong", flavor="Black")


print("==============================================")


# Arbitrary Arguments (*args)
# If you don’t know how many arguments will be passed, use *args.
# It collects all extra arguments into a tuple.

def make_many_teas(*flavors):
    print("Available Tea Flavors:")
    for tea in flavors:
        print("-", tea)

make_many_teas("Masala", "Lemon", "Ginger", "Green")


print("==============================================")


# Keyword Arbitrary Arguments (**kwargs)
# Similar to *args, but used when you want to pass key-value pairs.
# **kwargs collects them into a dictionary.

def tea_order(**details):
    print("Order Details:")
    for key, value in details.items():
        print(f"{key}: {value}")

tea_order(customer="Hitesh", flavor="Green", quantity=2)


print("==============================================")


# If these data is already in a dictionary
tea_dict = {
    "customer": "Hitesh",
    "flavor": "Green",
    "quantity": "3"
}

print(tea_dict)
tea_order(**tea_dict)