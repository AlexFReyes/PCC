# Python variables are read from top to bottom so if a global variable is changed at the end of a script then its final value is the most recent one
# Variable names can only contain letters, numbers, and underscores. 
# Variables can't start with numbers
# Spaces can't be used in variable names so _ are often used in their place
# Upper case letters in variable names have special meanings.
message = 'Hello World!'
print(message)
message = 'Hellow Python Crash Course World!'
print(message)

# Correct the error (mesage -> message)
message = "Hello Python Crash Course reader!"
print(message)

# Multiple Assignment - assign values to multiple variables in a single line of code
x, y, z = 0, 0, 0

# Constants - Variables that are capitalized are treated as constants throughout the life of a program
MAX_CONNECTIONS = 5000