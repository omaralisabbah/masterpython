#------------------------------------------------------
# Strings Methods Part 4
#-----------------------
# String 
#------------------------------------------------------


# replace (old_value, new_value, count)
var = "Numbers, One, Two, Three, and One ..."
print(var.replace("One", "1"))
print(var.replace("One", "1", 1))
print(var.replace("One", "1", 2))


print("-------------------------------------")


# join (iterable)
list = ["Omar", "Ali", "Sabbah"]
print("-".join(list))
print(" ".join(list))
print("".join(list))
print(type("".join(list)))