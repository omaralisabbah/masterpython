#------------------------------------------------------
# Files Handling in Python Part 2
#--------------------------------
# "a" = append
# "r" = read
# "w" = write
# "x" = create
# "r" = raw string
#--------------------------------
# Search about absloute path vs relative path
#------------------------------------------------------


myFile = open("/home/ingenium/github/masterpython/Part01_ThePythonLanguage/11.Files/file.txt", "r")

# print(myFile)  # Pringing file data object (name, mode and encoding)
# print(myFile.name)
# print(myFile.mode)
# print(myFile.encoding)


# print(myFile.read())  # default -1 that means read everything
# print(myFile.read(7))  # Number of characters


# print(myFile.readline(10))  # read lines
# print(myFile.readline())  # watch out
# print(myFile.readline())


# print(myFile.readlines(50))  # limiting by the number of characters
# print(type(myFile.readlines()))  # list


for line in myFile:
    print(line)
    if line.startswith("11"):
        break

# Closing file
myFile.close()