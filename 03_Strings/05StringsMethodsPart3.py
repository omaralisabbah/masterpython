#------------------------------------------------------
# Strings Methods Part 3
#-----------------------
# String 
#------------------------------------------------------


# index (substring, start, end)
a = "I Love Python!"
print(a.index("P"))  #
print(a.index("ve", 0, 10))  # Index of "ve" in the string
# print(a.index("ve", 0, 5))  # Error because "ve" is not in the range 0 to 5


print("-----------------------------------")


# find (substring, start, end)
b = "I Love Python!"
print(b.find("P"))  #
print(b.find("ve", 0, 10))  # 
# print(a.index("ve", 0, 4))  # -1 if not exist (Error!)


print("-----------------------------------")


# rjust, ljust (width, fill char)
c = "Python"
print(c.rjust(10))  # Space
print(c.rjust(10, "#"))  # Hashes

print(c.ljust(10))  # Space
print(c.ljust(10, "#"))  # Hashes


print("-----------------------------------")


# splitlines()
e = """ First line,
Second line,
Third line"""
print(e)
print(e.splitlines())
print(type(e.splitlines()))


print("-----------------------------------")


# splitlines()
f = """ First line,\nSecond line,\nThird line"""
print(f)
print(f.splitlines())
print(type(f.splitlines()))


print("-----------------------------------")


# splitlines()
g = """ First line,
\nSecond line,
\nThird line"""
print(g)
print(g.splitlines())  # Watch out
print(type(g.splitlines()))


print("-----------------------------------")


# expandtabs()
h = "Visual\tStudio\tCode\tFrom\tMicrosoft"
print(h)
print(h.expandtabs(20))


print("-----------------------------------")


# istitle()
xy = "I use vim in visual studio code in 2026"
xz = "I Use Vim In Visual Studio Code In 2026"
yz = "I Use VIM In Visual Studio Code In 2026"
print(xy.istitle())
print(xz.istitle())
print(yz.istitle())


print("-----------------------------------")


# isspace()
space = "   "
spacex = ""
print(space.isspace())
print(spacex.isspace())


print("-----------------------------------")


# islower()
varOne = "I use vim in visual studio"
varTwo = "code in 2026"
print(varOne.islower())
print(varTwo.islower())


print("-----------------------------------")


# isidentifier()
seven_bullets = "seven_bullets"
seven_rounds = "7sevenrounds"
give_me_a_gun = "give-me-a-gun"
print(seven_bullets.isidentifier())
print(seven_rounds.isidentifier())
print(give_me_a_gun.isidentifier())


print("-----------------------------------")


# isalpha()
bullets = "seven_bullets"
print(bullets.isalpha())
bullets = "seven7bullets"
print(bullets.isalpha())
bullets = "sevenbullets"
print(bullets.isalpha())


print("-----------------------------------")


# isalnum()
bullets = "seven_bullets"
print(bullets.isalnum())
bullets = "seven7bullets"
print(bullets.isalnum())