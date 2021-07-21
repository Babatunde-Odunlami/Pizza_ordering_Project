# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
word1 = "true"
word2 = "love"
#setting inputted namesto lowercase
name1_case = name1.lower()
name2_case = name2.lower()
#concatenating both name1_case
name_cased = name1_case + name2_case
print(
    name_cased)
#checking and summing frequency of each letter in true in the names
count1 = 0
for each_letter in word1:
	letter_count1 = name_cased.count(each_letter)
	count1 = count1 + letter_count1
	print (count1)
count2 = 0
for each_letter in word2:
	letter_count2 = name_cased.count(each_letter)
	count2 = count2 + letter_count2
print(letter_count2)
#converting counts to string and concatenating
str_score = str(count1) + str(count2)
score = int(str_score)
#commenting on love percentage
if score <= 50 and score >=40:
		print(f"Your score is {score}, you are alright together.")
elif score <10 or score > 90:
	print(f"Your score is {score}, you go together like coke and mentos.")
else:
	print(f"Your love score is {score}%")
