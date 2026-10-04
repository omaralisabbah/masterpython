#------------------------------------------------------
# Modifying Elements
#-------------------
#
#------------------------------------------------------

# append() - adds an element to the end of the list
first_list = ["first", "second", "third"]

first_list.append("fourth")
print(first_list)  # ['first', 'second', 'third', 'fourth']
print(first_list[1])  # 'second'
print(type(first_list[1]))  # <class 'str'>
print(first_list[-1])  # 'fourth'
first_list.append(0.99) 
first_list.append(True)
print(first_list)  # ['first', 'second', 'third', 'fourth', 0.99, True]
print(type(first_list))  # <class 'list'


print("--------------------------------------")


second_list = ["fifth", "sixth", "seventh"]
# extend() - adds elements from another list to the end of the list
first_list.extend(second_list)
print(first_list)  # ['first', 'second', 'third', 'fourth', 0.99, True, 'fifth', 'sixth', 'seventh']
print(first_list[5])  # True
print(type(first_list[1]))  # <class 'str'>
print(first_list[-1])  # 'seventh'


print("--------------------------------------")


# extend() - adds elements from another list to the end of the list
first_list = ["first", "second", "third"]
first_list.extend(["fourth", 0.99, True])
print(first_list)  # ['first', 'second', 'third', 'fourth', 0.99, True]
print(first_list[1])  # 'second'
print(type(first_list[1]))  # <class 'str'>
print(first_list[-1])  # True   


print("--------------------------------------")


#remove() - removes the first occurrence of a specified value
first_list = ["first", "second", "third", "fourth", 0.99, True]
first_list.remove("second")
print(first_list)  # ['first', 'third', 'fourth', 0.99, True]
print(first_list[1])  # 'third'
print(type(first_list[1]))  # <class 'str'>
print(first_list[-1])  # True


print("--------------------------------------")


# sort() - sorts the list in ascending order
first_list = [3, 1, 4, 2, 5]
first_list.sort()
print(first_list)  # [1, 2, 3, 4, 5]
print(first_list[1])  # 2
print(type(first_list[1]))  # <class 'int'>
print(first_list[-1])  # 5

first_list.sort(reverse=True)
print(first_list)  # [5, 4, 3, 2, 1]


print("--------------------------------------")


second_list = ["banana", "apple", "cherry"]
second_list.sort()
print(second_list)  # ['apple', 'banana', 'cherry']

second_list.extend([True, False, 6, 3.14])
second_list.reverse()
print(second_list)  # [3.14, 6, False, True, 'cherry', 'banana', 'apple']