#------------------------------------------------------
# Accessing Elements
#-------------------
#
#------------------------------------------------------


first_list = ["first", "second", "third", 1, 0.99, True]

print(first_list)  #
print(first_list[1])  #
print(type(first_list[1]))
print(first_list[-1])  #
print(first_list[-3])  #
print(type(first_list))


print("--------------------------------------")


#Slicing
print(first_list[2:4])  #
print(first_list[:4])  #
print(first_list[3:])
print(type(first_list[3:]))


print("--------------------------------------")


print(first_list[::1])
print(first_list[::2])


print("--------------------------------------")


first_list[1] = 2
print(first_list)

first_list[-1] = False
print(first_list)



print("--------------------------------------")


first_list[0:3] = []
print(first_list)

first_list[0:3] = ["Mu", "ta", "ble"]
print(first_list)


