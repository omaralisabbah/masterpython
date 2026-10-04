#------------------------------------------------------
# Loops Break and Continue
#-------------------------
# 
#------------------------------------------------------


numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}


for num in numbers:
    if num == 7:
        continue
    print(num)


print("==")


for num in numbers:
    if num == 7:
        break
    print(num)


print("==")


# Pass if you need to run the code and there is a junck of code not implemented
for num in numbers:
    pass