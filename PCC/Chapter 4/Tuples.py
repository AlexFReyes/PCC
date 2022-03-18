# Defining a tuple - a list that is immutable (cannot change)
# Parentheses instead of brackets
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# If you want to define a tuple with a signle element you must include a trailing comma
my_t = (3,)

# You can reassign the value of a tuple entirely
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)