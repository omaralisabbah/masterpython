# ------------------------------------------------------
# Python Built In Functions Part 2
# --------------------------------
# sum()
# round()
# range()
# print()
# ------------------------------------------------------
# Notes:
# ------------------------------------------------------

# sum(iterable, start)
listX = [1, 2, 3, 4, 5]
print(sum(listX))
print(sum(listX, 4))

print("=======================")

# round(number, no.of digits)
print(round(14.78))
print(round(14.5))
print(round(14.51))
print(round(14.501))
print(round(14.155256, 2))

print("=======================")

# range(start, end, step)
print(list(range(0)))
print(list(range(11)))
print(list(range(0, 19, 3)))

print("=======================")

# print() - Space is the default separator in print
print("How are you ?")
print("How" "are" "you" "?")
print("How", "are", "you", "?")
print("=============")
print("How are you ?", sep=":")
print("How" "are" "you" "?", sep=":")
print("How", "are", "you", "?", sep=" $ ")

print("=======================")

# end of the print function defualt value is end="\n"
print("This is the first line", end="\n")
print("This is the second line")

print("This is the first line,", end="\t")
print("and this is the second line")
print("But, this is the third line")