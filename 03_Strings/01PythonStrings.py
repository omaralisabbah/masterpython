#------------------------------------------------------
# Strings in Python
#-------------------
# 
#------------------------------------------------------

# strings are sequences of characters enclosed in single quotes (' ') or double quotes (" ").
python_string = "Python is a programming language"
string_with_numbers = "Python 3.9"

# Strings can also contain special characters, such as punctuation marks, symbols, and whitespace.
string_with_special_chars = "Python'@3.9!'"
string_with_special_chars_2 = 'Python "@3.9!"'

# Strings can also be enclosed in triple quotes (''' ''' or """ """) to create multi-line strings or docstrings.
triple_quoted_string = """This is a triple-quoted string.
It can span multiple lines.
You can use it for docstrings or multi-line comments."""

triple_quoted_string_2 = '''This is another triple-quoted string.
It can also span multiple lines.
You can use it for docstrings or multi-line comments.'''

# Strings can also contain backslashes (\) to escape special characters or to create raw strings.
string_with_backslash = "This is a string with a backslash \\ in it."

# Strings can also be created as raw strings by prefixing the string with an 'r' or 'R', which tells Python to treat backslashes as literal characters.
string_with_backslash_2 = r"This is a raw string with a backslash \ in it."

print(python_string)
print(string_with_numbers)

print(string_with_special_chars)
print(string_with_special_chars_2)

print(triple_quoted_string)
print(triple_quoted_string_2)

print(string_with_backslash)
print(string_with_backslash_2)