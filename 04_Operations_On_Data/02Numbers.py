#------------------------------------------------------
# Numbers
#--------
# Integer
# Float
# Complex
# Numbers type conversion
#------------------------------------------------------


# Integer
print(type(1))
print(type(331))
print(type(-111))

print("-------------")

# Float
print(type(1.51))
print(type(0.99))
print(type(-5.596))
print(type(-0.99))

print("-------------")

# Complex
complex_number = 31+14j
print(type(complex_number))
print("Real part is: {}".format(complex_number.real))
print("Imaginary part is: {}".format(complex_number.imag))

print("-------------")

# Numbers type conversion
print(99)
print(float(99))
print(complex(99))

print("------")

print(99.54)
print(int(99.54))
print(complex(99.54))

print("------")

print(12+25j)
# print(int(12+25j))  # Error: you can not convert complex number 