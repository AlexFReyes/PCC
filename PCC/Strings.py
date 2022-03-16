print('Please enter your name.')
name = input().lower()
print(name.title())
#.title will change a string so that each individual word's first letter is capitalized and the rest are lowercase
#.x means python will execute a method on a piece of data
# Every method is followed by a set of ().
#.upper and .lower make strings all upper or lowercase respectively

#.split function will convert strings to arrays based on the argument. If there is no argument it will split on spaces.
first_last = name.split()
first_name = first_last[0]
last_name = first_last[-1]
# Using variables in strings f"" will allow you to insert variables into strings
full_name = f'Your first name is {first_name.title()}, and your last name is{last_name.title()}.'
print(full_name)