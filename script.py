# NUmbers
num_int = 100
num_float = 2.73495

# Strings
greeting = "Howdy"
name = 'Chege'

# Booleans
is_valid = True
is_empty = False 

# Collection
fruits = ["Apple", "Banana", "Cherry", "Quava"] #List
coordinates = (10, 20) # Tuple
person = {"name": "David", "City" : "Nairobi", "age": "20"} # Dictionary



# Operators
a = 14
b = 6 
print( a + b )
print(a - b )
print(a % b )
print(a ** b )
print(a // b )

# Assignment Operators
score = 100
score += 50
print(score)

counter = 10
counter *= 2
print(counter)


#Basic Comparisons
x = 10
y = 20

print(x == y)
print(x != y)
print(x < y)
print(x > y)

#Chained Comparisons
tempereture = 19
is_comfortable = 20 <= tempereture <= 30
print(is_comfortable)

user_age = 20
is_adult = user_age >= 18
print(is_adult)


#Input and Output
name = input("Please enter your name: ")
age = input("Please enter your age: ")
print("Hello, " + name + "!. You are" + age + "years old.")


num1_str = input("Enter the first number:")
num2_str = input("Enter the second number:")

# convert the string to integers
num1 = int(num1_str)
num2 = int(num2_str)

sum_of_numbers = num1 + num2
print("The sum of the numbers are:", sum_of_numbers)