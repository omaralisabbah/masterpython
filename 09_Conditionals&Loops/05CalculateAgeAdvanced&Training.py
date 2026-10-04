#------------------------------------------------------
# Calculate Age Advanced and Training
#------------------------------------
# Note: 
#------------------------------------------------------

# Comment
print('=' * 90)
print(" You can enter the word or the first char of the time format needed ".center(90,'='))
print('=' * 90)

age = input("Enter your age: ").strip()
unit = input("Choose time unit: Months, Weeks and Days ").strip().lower()

months = int(age) * 12
weeks = months * 4
days = int(age) * 365

if unit == 'months' or unit == 'm':
    print("You choosed the unit months: ")
    print(f"You lived for {months:,}  months.")

elif unit == 'weeks' or unit == 'w':
	print("You choosed the unit weeks: ")
	print(f"You lived for {weeks:,}  weeks.")

elif unit == 'days' or unit == 'd':
	print("You choosed the unit days: ")
	print(f"You lived for {days:,}  days.")