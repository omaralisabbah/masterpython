#------------------------------------------------------
# Practical Membership OperatoControl
#------------------------------------
# in
# not in
#------------------------------------------------------


# List contains admins
admins = ["Omar", "Samy", "Maged", "Belal", "Waheed", "Esraa"]

# print(admins.index("Maged"))
# print(admins)
# admins[1] = "Elzero"
# print(admins)

# Login
name = input("Please enter your name ").strip().capitalize()

if name in admins:
    print(f"Hello, {name} Welcome back!")
    option = input("Delete or Update your name ?").strip().capitalize()

    # Update Option
    if option == 'Update' or option == 'U':
        newName = input("Your new name please ").strip().capitalize()
        admins[admins.index(name)] = newName
        print("Name Updated!")
        print(admins)

    # Delete Option
    elif option == 'Delete' or option == 'D':
        admins.remove(name)
        print("Name Deleted!")
        print(admins)

    else:
        print("Wrong option!!")
        
else:
    status = input("You are not an admin, Wanna add your self?! (Yes, No)").strip().capitalize()

    if status == 'Yes' or status == 'Y':
        print("You have been added <3")
        admins.append(name)
        print(admins)

    else:
        print("It's not your place!")


print(30 * '=')