#------------------------------------------------------
# Nested For Loop
#----------------
# 
#------------------------------------------------------


persons = ["Khaled", "Kamal", "Osama", "Zaid"]
ranks = ["Excellent", "Very Good", "Good", "Accepted"]

for name in persons:
	print(f"{name} Rank is: ")

	for grade in ranks:
		print(f"- {ranks}")


print(50 * "=")


peoples = {
	"Khaled" : {
		"Excellent" : ">=90%",
		"Very Good" : "90% <= & >= 80%",
		"Good" : "80% <= & >= 70%"
	},
	"Kamal" : {
		"Excellent" : ">=90%",
		"Good" : "80% <= & >= 70%",
		"Very Good" : "90% <= & >= 80%"
	},
	"Osama" : {
		"Very Good" : "90% <= & >= 80%",
		"Excellent" : ">=90%",
		"Good" : "80% <= & >= 70%"
	},
	"Zaid" : {
		"Good" : "80% <= & >= 70%",
		"Excellent" : ">=90%",
		"Very Good" : "90% <= & >= 80%"
	}
}


# print(peoples["Osama"])
# print(peoples["Khaled"]["Excellent"])


print(50 * "=")


for name in peoples:
	# print(name)
	print(f"Rank for {name} is: {peoples[name]}")

	for rank in peoples[name]:
		print(rank)