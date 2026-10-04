#------------------------------------------------------
# For Loop Training
#------------------
# range()
# dictionary
#------------------------------------------------------


range_of_numbers = range(1, 101)

for number in range_of_numbers:
    print(number)
	
else:
	print("Loop is finished!")


print(20 * '=')


dict_resources = {
      "Huge": "100%",
      "Big": "90%",
      "Large": "80%",
      "Midum": "70%",
      "Small": "60%",
}

print(dict_resources["Big"])
print(dict_resources.get("Midum"))


print(20 * '=')


for dict in dict_resources:

	# print(dict)
    print(f"Resource Class {dict} is: {dict_resources[dict]}")