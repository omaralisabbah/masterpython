#--------------------------------------------------------------------
# Function Recursion
#--------------------------------
# To understand the recursion, first you need to understand recursion
#--------------------------------------------------------------------


# word : [Goaaaaaaaaaaaaaaaal]
variable = "Goaaaaaaaaaaaaaaaal"

# print(variable[1:])

def remove_repeated_char(word):

    if len(word) == 1:
        return word

    if word[0] == word[1]:
        return remove_repeated_char(word[1:])

    return word[0] + remove_repeated_char(word[1:])  # Stach [ Goal ]

   
print(remove_repeated_char("Goaaaaaaaaaaaaaaaal"))


print("==============")


# For Explanation
word = "Auutooomotivee"
def remove_repeated_char_explained(word):

    if len(word) == 1:
        return word

    print(f"Callback after the last one: [{word}]")

    if word[0] == word[1]:
        print(f"Condition is true: [{word}]")
        return remove_repeated_char_explained(word[1:])

    print(f"Print before return: [{word}]")
    return word[0] + remove_repeated_char_explained(word[1:])  # Stach [ Goal ]


print(remove_repeated_char_explained("Auutooomotivee"))