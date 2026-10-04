#------------------------------------------------------
# Strings Formatting The Old Way
#--------------------------------
# %s
# %d
# %f
# %
#------------------------------------------------------


name = "Robotoype"
age = 1
rank = 1


print("My name is: " + name)
# print("My name is: " + name + "and my age is: " + age)  # Type Error

print("My name is: %s" % "Robototpe")
print("My name is: %s" % name)

print("My name is: %s and my age is: %d" % (name, age))
print("My name is: %s and my age is: %d and my rank is: %f" % (name, age, rank))


print("-------------------------------------")


n = "Omar"
l = "Python"
p = 10

print("My name is %s, I'm %s Self-Taught with +%d Years Experience" % (n, l, p))


print("-------------------------------------")


num = 3
print("Number to be printed is: %d" % num)
print("Number to be printed is: %f" % num)
print("Number to be printed is: %0.3f" % num)


print("-------------------------------------")

# Truncate String
long_string = "to insert a variable into the string that comes before"
print("Long string message is: %s" % long_string)
print("Long string message is: %0.9s" % long_string)