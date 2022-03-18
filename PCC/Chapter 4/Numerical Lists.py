# Using the range() function
# The range function begins counting at the first value and stops non inclusive at the last
for value in range(1,5):
    print(value)
# If you pass range() a single argument it will start at 0
for value in range(5):
    print(value)
# Use range to make a list of numbers
numbers = list(range(1,6))
print(numbers)
# Make a list of even numbers
even_numbers = list(range(2, 11, 2))
print(even_numbers)
# Create a list of squared integers
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)
# Statistics with lists of numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))
# List comprehension - combine the for loop and the creation of new elements into one line
squares = [value**2 for value in range(1,11)]
print(squares)
