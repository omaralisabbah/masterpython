#------------------------------------------------------
# Function Scope
#--------------------------------
# If you declare a variable outside the function, 
# it can be accessed inside using the global keyword.
#
# These are small one-line functions without a name.
# Commonly used for short operations.
#
# If you want to overwrite on a global variable form function inside use 'global' keyword
#
# Note: Try to toggle the global keyword to see the differences
#------------------------------------------------------

# Local Variables
def local_example():
    message = "This is local to the function"
    print(message)

local_example()
# print(message)  # Error: message is not defined

print("=============================================")


# Global Variables
x = "GlobalX"

def global_example():
    global x
    x = "FuncGlobalX"
    print("Inside function:", x)

global_example()
print("Outside function:", x)


print("=============================================")


# Good Example
variable = 404  # Global Scope

def func01():
    global variable
    variable = 101  # what happens in vegas stays in vegas
    print(f"Printing variable from function [01] scope {variable}")

func01()
print(f"Printing variable from Global scope {variable}")


print("======================")


def func02():
    variable = 99  # what happens in vegas stays in vegas
    print(f"Printing variable from function [02] scope {variable}")

print(f"Printing variable from Global scope {variable}")
func01()
func02()