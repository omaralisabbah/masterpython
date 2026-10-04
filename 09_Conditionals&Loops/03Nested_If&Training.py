#------------------------------------------------------
# Nested If and Training
#-----------------------
# Note: 
#------------------------------------------------------

uName = "Robototype"
uCountry = "Palestine" # EGYPT  # KSA
cName = "ROS2"
cPrice = 99.99
cDiscount = 20
isstudent = "YES"

if uCountry == "EGYPT" or uCountry == "Palestine":
	print(f"Hello, {uName}, Because you are in in: {uCountry}")

	if isstudent == "YES":
		print(f"The course \"{cName}\", The price will be: ${cPrice - 70}")
	else:
		print(f"The course \"{cName}\", The price will be: ${cPrice - 50}")

elif uCountry == "KSA" or uCountry == "Kuwait" or uCountry == "Qatar":
	print(f"Hello, {uName}, Because you are in in: {uCountry}")
	print(f"The course \"{cName}\", The price will be: ${cPrice - 30}")

else:
	print(f"Hello, {uName}, Because you are in in: {uCountry}")
	print(f"The course \"{cName}\", The price will be: ${cPrice - 10}")