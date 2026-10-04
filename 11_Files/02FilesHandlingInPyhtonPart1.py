#------------------------------------------------------
# Files Handling in Python Part 1
#--------------------------------
# "a" = append
# "r" = read
# "w" = write
# "x" = create
# "r" = raw string
#--------------------------------
# Search about absloute path vs relative path
#------------------------------------------------------


import os

# print(os.getcwd())  # Main current woring directory

# print(os.path.dirname(os.path.abspath(__file__)))  # Directory for the opened file

os.chdir(os.path.dirname(os.path.abspath(__file__)))  # Change current woring directory

print(os.getcwd())

# print(os.path.abspath(__file__))
file = open("/home/ingenium/github/masterpython/Part01_ThePythonLanguage/11.Files/file.txt")