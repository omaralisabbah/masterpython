#------------------------------------------------------
# Strings Formatting The New Ways
#--------------------------------
# {:s}
# {:d}
# {:f}
# %
#------------------------------------------------------
# URL: https://pyformat.info/
#------------------------------------------------------

from multiprocessing.managers import ValueProxy


name = "Robotoype"
age = 1
rank = 1


print("My name is: " + name)
# print("My name is: " + name + "and my age is: " + age)  # Type Error

print("My name is: {}" .format("Robototpe"))
print("My name is: {}" .format(name))

print("My name is: {} and my age is: {}" .format(name, age))
print("My name is: {:s} and my age is: {:d} and my rank is: {:f}" .format(name, age, rank))


print("-------------------------------------")


n = "Omar"
l = "Python"
p = 10

print("My name is {:s}, I'm {:s} Self-Taught with +{:d} Years Experience" .format(n, l, p))


print("-------------------------------------")


num = 3
print("Number to be printed is: {:d}" .format(num))
print("Number to be printed is: {:f}" .format(num))
print("Number to be printed is: {:.3f}" .format(num))


print("-------------------------------------")

# Truncate String
long_string = "to insert a variable into the string that comes before"
print("Long string message is: {:s}" .format(long_string))
print("Long string message is: {:.20s}" .format(long_string))


print("-------------------------------------")


# Format Money (No all marks can be applied)
money = 3118844664
print("My balance in my bank account: {}" .format(money))
print("My balance in my bank account: {:d}" .format(money))
print("My balance in my bank account: {:,d}" .format(money))
print("My balance in my bank account: {:_d}" .format(money))


print("-------------------------------------")


# rearrange items
x, y, z = "Do", "Not", "Think"
print("Print them: {} {} {}".format(x, y, z))  #
print("Print them: {1} {2} {0}".format(x, y, z))  #
print("Print them: {2} {1} {0}".format(x, y, z))  #

a, b, c = 9, 11, 3
print("Print them: {} {} {}".format(a, b, c))  #
print("Print them: {1:d} {2:d} {0:d}".format(a, b, c))  #
print("Print them: {2:f} {0:f} {1:f}".format(a, b, c))  #
print("Print them: {2:.2f} {0:.3f} {1:.4f}".format(a, b, c))  #


print("-------------------------------------")


# Format in versions 3.6+
varx = "omarx"
vary = 3
print("Print them: {varx} and {vary}")  # 
print(f"Print them: {varx} and {vary}".format(varx, vary))  #