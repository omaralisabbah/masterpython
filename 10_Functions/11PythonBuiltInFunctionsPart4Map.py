# ------------------------------------------------------
# Python Built In Functions Part 4 Map
# ------------------------------------
# Map
# Map take a function + iterator
# Called Map because it map the function on every element
# The function can be pre-defined function or lambda function
# ------------------------------------------------------
# Notes: When you need a function to do something, but you do not need it on your system
# ------------------------------------------------------


# Use map with pre-defined function
def text_format(text):
    return f"- {text} -"

List = ["01", "02", "03", "04", "05", "06"]

data = map(text_format, List)

print(data)  # <map object at 0x70b283db7e40>

for text in map(text_format, List):
    print(text)

print("======")

for text in list(map(text_format, List)):
    print(text)


print("==============================")


# Use map with lambda function
for tex in list(map((lambda tex : f"- {tex} -"), List)):
    print(tex)
