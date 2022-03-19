# A simple example
import re


cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Conditional tests True False statements
# Ignore case when checking for equality
# 'audi' is not the same as 'Audi'
cars[0].lower() == 'audi'

# Check for inequality
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

# Numerical Comparisons
answer = 17

if answer != 42:
    print('That is not the correct answer. Please try again!')
    
#Check multiple conditions
age = 19

if age < 21 or age <= 21 or age > 21 and age >= 21:
     print('nice')
# Or one must be true and the statement is tru
# And both must be true and the statement is true

# Check if item is not in a list
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

#Boolean
True 
False
