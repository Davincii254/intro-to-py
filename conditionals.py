# Conditional Statements
grade = 10
if grade >= 60:
    print("You have passed the exam!")
else:
    print("You have failed the exam!")

age = 13
has_ticket = False

if age>= 18 and has_ticket:
    print("WElcome to kasarani for the match!")
else:
    print("Sorry, you cannot enter the stadium")


rating = 4
if rating == 5:
    print("Excellent services")
elif rating == 4:
    print("Great service!")
elif rating == 3:
    print("It was okay")
elif rating == 2:
    print("Meeehhhh")
elif rating == 1:
    print("Not a good service at all, failure!")


tempereture = int(input("What is the tempereture in degrees Celcius?"))

if tempereture >= 25:
    print("Its a very hot day")
elif tempereture >= 18:
    print("Its mild, carry a chacket")
elif tempereture >= 10:
    print("its a bit chilly, stay indoors")
else: 
    print("Its very very veryyy cold outside")


# for loop
product_code = ["P-101", "P-102", "P-103", "P-104", "P-105"]
target_code = "P-205"

for code in product_code:
    if code == target_code:
        print("Found the product")
    else:
        print("Product not found")
        break 

sentence = "Hello everyone, This is our for loop that we are using as  an exammple for our class session today"
vowel_count = 0
vowels = "aeiouAEIOU"

for char in sentence:
    if char in vowels:
        vowel_count += 1

print(f"The number of vowels is: {vowel_count}")


countdown = 10

while countdown > 0:
    print(countdown)
    countdown -= 1

print("Blast off!!!")

min_length = 5
password = ""

print(f"Please enter a password, it must be at least {min_length} characters long")

while len(password) < min_length:
    password = input("Enter new password ")

print("Password set seccesfully!")