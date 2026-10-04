#------------------------------------------------------
# Email Slicing
#--------------
# Note: You can add strip() and Capitalize()
#------------------------------------------------------


email = "ingenium@gmail.com"

print(email[0:5])
print(email.index('@'))
print(email[0:email.index('@')])
print(email[:email.index('@')])


print(20 * "=")


name = input("What\'s your name?")
your_email = input("What\'s your email?")
username = your_email[:your_email.index("@")]
website = your_email[your_email.index("@") + 1:]

print(f"Hello, {name} and your email is: {your_email}")
print(f"Your Username is: {username} and, Your website is: {website}")