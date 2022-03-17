# Changing an element in a list
motorcycles = ["honda", "yamaha", "suzuki"]
motorcycles[0] = "ducati"
print(motorcycles)
# Add an element to the end of a list or to an empty list
motorcycles.append("honda")
print(motorcycles)
# Inserting elements into a list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0,'harley davidson')
print(motorcycles)
# Removing an element from a list
# del method
del motorcycles[0]
print(motorcycles)
# pop() method stores and deletes the last element in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)
# pop() items from any position in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")
# Remove an item by value - remove()
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
# Use a removed item
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

