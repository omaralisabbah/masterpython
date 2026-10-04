# Example #2: Exceptions trigger the except block and skip any code after the error.

try:
    print(1/0)# This will fail.
    print("I'm code that will never run!")

    # This *would* fail, except we never get here.
    # That's why it's best to use a try block on the fewest lines of code possible.
    print(555/0)
except ZeroDivisionError:
    print("You still can't divide by zero!")
