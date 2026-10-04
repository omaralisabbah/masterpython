#------------------------------------------------------
# Ternary Conditional Operator
#-----------------------------
# Note: condition if True | if condtion | else | condition if False
#------------------------------------------------------


Country = "EGYPT" # EGYPT  # KSA
Temp = 29
cPrice = 99.99
cDiscount = 20
isstudent = "YES"

if Country == "EGYPT": print(f"Hello, The Weather in: {Country} is: {Temp}")
elif Country == "Palestine": print(f"Hello, The Weather in: {Country} is: {Temp}")
else: print(f"Hello, The Weather in: {Country} is: {Temp}")


print("=" * 20)

# Ternary Conditional Operator
price = 20
print("Price is High " if price > 20 else "Price is Good")