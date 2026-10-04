#------------------------------------------------------
# Files Handling in Python Part 3
#--------------------------------
# "a" = append
# "r" = read
# "w" = write
# "x" = create
# "r" = raw string
#-----------------
# Write and append
#-----------------
# Watch out when overwriting files
# append is awesome, see how with new line
#------------------------------------------------------


# myFile = open("/home/ingenium/github/masterpython/Part01_ThePythonLanguage/11.Files/file.txt", "w")
# myFile.write("01. Hello, From Python Script")
# myFile.write("02. Second Line")


# myFile = open("/home/ingenium/github/masterpython/Part01_ThePythonLanguage/11.Files/file.txt", "w")
# myFile.write("Holy Moly, Python script" * 1000)


# myList = ["Wael\n", "Ashraf\n", "Ragab\n"]
# myFile = open("/home/ingenium/github/masterpython/Part01_ThePythonLanguage/11.Files/file.txt", "w")
# myFile.writelines(myList)


myFile = open("/home/ingenium/github/masterpython/Part01_ThePythonLanguage/11.Files/file.txt", "a")
myFile.write("Holy Moly, Python script \n" * 10)