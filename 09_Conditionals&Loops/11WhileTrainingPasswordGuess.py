#------------------------------------------------------
# While Training Password Guess
#------------------------------
# 
#------------------------------------------------------


tries = 3 

main_pass = "pass"

inputPassword = input("Write your password: ")

while inputPassword != main_pass:
    tries -= 1
    print(f"Wrong Password, { 'Last' if tries == 0 else tries} Tries left.")
    inputPassword = input("Write your password: ")

    if tries == 0:
        print("You are out of Tries.")
        break

else:
    print("Password is correct, Willkommen <3")