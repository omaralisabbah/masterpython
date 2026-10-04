#------------------------------------------------------
# If, elif and else
#------------------
# Control Flow
#------------------------------------------------------


uName = "Robototype"
uCountry = "Palestine"
cName = "ROS2"
cPrice = 99.99
cDiscount = 20

if uCountry == "EGYPT":
	print(f"Hello, {uName}, Because you are in in: {uCountry}")
	print(f"The course \"{cName}\", The price will be: ${cPrice - 90}")
elif uCountry == "Palestine":
	print(f"Hello, {uName}, Because you are in in: {uCountry}")
	print(f"The course \"{cName}\", The price will be: ${cPrice - 30}")
else:
	print(f"Hello, {uName}, Because you are in in: {uCountry}")
	print(f"The course \"{cName}\", The price will be: ${cPrice - 10}")