#------------------------------------------------------
# Files Handling in Python Part 4 Important info
#-----------------------------------------------
# "a" = append
# "r" = read
# "w" = write
# "x" = create
# "r" = raw string
# "a" = append
# trancate
#-----------------
# Write and append
#-----------------
# Watch out when overwriting files
# append is awesome, see how with new line
#------------------------------------------------------


import os

# myFile = open("/home/ingenium/github/masterpython/Part01_ThePythonLanguage/11.Files/file.txt", "a")
# myFile.truncate(5)


# myFile = open("/home/ingenium/github/masterpython/Part01_ThePythonLanguage/11.Files/file.txt", "a")
# print(myFile.tell())  # Cousor Postion


# myFile = open("/home/ingenium/github/masterpython/Part01_ThePythonLanguage/11.Files/file.txt", "r")
# myFile.seek(3)  # Change Cousor Postion
# print(myFile.read())


os.remove("/home/ingenium/github/masterpython/Part01_ThePythonLanguage/11.Files/file.txt")  # Remove the file