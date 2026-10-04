#------------------------------------------------------
# Lambda Function
#--------------------------------
# Lambda Functions (Anonymous Functions)
# These are small one-line functions without a name.
# Commonly used for short operations.
# You can use it for returning data from another function
#------------------------------------------------------


def Funco(name) : return f"Welcome, {name}"

Hello = lambda name : f"Welcome, {name}"

print(Funco("Omar"))
print(Hello("Omar"))


print("===========================")


print(Funco.__name__)
print(Hello.__name__)


print("===========================")


square = lambda n: n ** 2
print("Square of 5 is: ", square(5))

add_nums = lambda a, b: a + b
print("Sum using lambda: ", add_nums(3, 4))


print("===========================")


def Func(name, age) : return f"Welcome, {name} your age is: {age}"

Hola = lambda name, age : f"Welcome, {name} your age is: {age}"

print(Func("Omar", 22))
print(Hola("Omar", 22))

print(Func.__name__)
print(Hola.__name__)
print(type(Hola))