#------------------------------------------------------
# For Loop and Else
#------------------
# for item in iterable_object :
# 	Do Something
#------------------------------------------------------


resources = [1, 2, 3, 4, 5, 6, 7]

for item in resources:
    print(item * 2)
    if item % 2 == 0:
          print(f"The item {item} is even.")
    else:
          print(f"The item {item} is odd.")

else:
	print("Loop is finished!")



print(20 * '=')

name = "Robototype"

for letter in name:
	print(f"[{letter.upper()}]")

