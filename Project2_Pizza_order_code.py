# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
Small_Pizza = 15
Medium_Pizza = 20
Large_Pizza = 25
bill = 0
small = 2
large = medium = 3
extra_cheese = 1
#for small sized pizza
if size == "S":
	if add_pepperoni == "Y":
		if extra_cheese == "Y":
			bill = Small_Pizza + small + extra_cheese
		else:
			bill =Small_Pizza + small
	else:
		bill = Small_Pizza
	print(f"The total cost of your order is ${bill}.\n")
#for medium sized pizza
elif size == "M":
	if add_pepperoni == "Y":
		if extra_cheese == "Y":
			bill = Medium_Pizza + medium + extra_cheese
		else:
			bill =Medium_Pizza + medium
	else:
		bill = Medium_Pizza
	print(f"The total cost of your order is ${bill}.\n")
#for large sized pizza
elif size == "L":
	if add_pepperoni == "Y":
		if extra_cheese == "Y":
			bill = Large_Pizza + large + extra_cheese
		else:
			bill =Large_Pizza + large
	else:
		bill = Large_Pizza
	print(f"The total cost of your order is ${bill}.\n")
else:
	print(new_order = input("Do you want to to order another pizza? Enter y for 'yes' or n for 'no' \n"))
