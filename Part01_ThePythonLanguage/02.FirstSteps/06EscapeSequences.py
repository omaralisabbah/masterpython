
# ------------------------------------------------
# Escape Sequences Characters
# \n - New Line
# \b - Backspace
# \t - Tab
# \' - Single Quote
# \" - Double Quote
# \\ - Backslash
# \r - Carriage Return
# \f - Form Feed
# \v - Vertical Tab
# \ooo - Octal value
# \xhh - Hex value
# \N{name} - Unicode character name
# \uXXXX - Unicode character with 16-bit hex value
# \UXXXXXXXX - Unicode character with 32-bit hex value
# \a - Bell (alert)
# ------------------------------------------------

# New Line
print("Hello, World!\nThis is a new line.")  # Output: Hello, World!

# Backspace
print("Hello, W\borld!")  # Output: Hello, World!

# Tab
print("This is a new\tline.")  # Output: This is a new  line.

# Single Quote
print('It\'s a beautiful day!')  # Output: It's a beautiful day!

# Double Quote
print("He said, \"Hello!\"")  # Output: He said, "Hello!"

# Backslash
print("This is a backslash: \\")  # Output: This is a backslash: \

# Carriage Return
print("Hello, World!\rThis is a carriage return.")  # Output: This is a carriage return.

# Form Feed
print("Hello, World!\fThis is a form feed.")  # Output: This is a form feed.

# Vertical Tab
print("Hello, World!\vThis is a vertical tab.")  # Output: This is a vertical tab.

# Octal value
print("This is an octal value: \101")  # Output: This is an octal value: A

# Hex value
print("This is a hex value: \x41")  # Output: This is a hex value: A

# Unicode character name
print("This is a Unicode character: \N{GREEK CAPITAL LETTER DELTA}")  # Output: This is a Unicode character: Δ

# Unicode character with 16-bit hex value
print("This is a Unicode character: \u03B1")  # Output: This is a Unicode character: α

# Unicode character with 32-bit hex value
print("This is a Unicode character: \U0001F600")  # Output: This is a Unicode character: 😀

# Bell (alert)
print("This is a bell alert: \a")  # Output: This is a bell alert:  (may produce a sound depending on the system)

