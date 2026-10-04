#------------------------------------------------------
# Loop and Dictionary
#--------------------
# 
#------------------------------------------------------


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


for name, rank in peoples.items():
	# print(name)
	print(f"Rank for {name} is: {rank}")


print(50 * "=")


dict_resources = {
	"classA": {
		"Huge": "100%",
        "Big": "90%"
    },
	"classB": {
            "Large": "80%",
            "Midum": "70%"
    },
    "classC": {
        "Small": "60%",
        "Tiny": "50%"
    }
      
      
}


for classX, value in dict_resources.items():
    # print(f"Rank for {clas} is: {value}")
	print(f"Rank for {classX} is: ")
	
	for key, val in value.items():
		 print(f"- {key} && {val}")
           