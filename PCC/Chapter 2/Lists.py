# List - a collection of items in a particular order
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)
# Lists start at 0, selecting an item from a list add [x] to the end of a var
print(bicycles[0])
# You can use methods on elements from lists, or lists as a whole if you convert them to a string first
print(str(bicycles).title())
print(bicycles[0].title())
# Acessing -1 in a list will access the last thing in the list, more negatives will move further up the end
print(bicycles[-1])
print(bicycles[-2])
# You can use items from a list as infividual variables and fstrings
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
