# 3-8
locations = ['japan', 'france', 'italy' 'bahamas']
# Print your list in its original order. Don’t worry about printing the list neatly, just print it as a raw Python list.
print(locations)
# Use sorted() to print your list in alphabetical order without modifying the actual list.
print(sorted(locations))
# Show that your list is still in its original order by printing it.
print(locations)
# Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
print(sorted(locations,reverse=True))
# Show that your list is still in its original order by printing it.
print(locations)
# Use reverse() to change the order of your list. Print the list to show that its order has changed.
locations.reverse()
print(locations)
# Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
locations.reverse()
print(locations)
# Use sort() to change your list so it’s stored in alphabetical order. Print thelist to show that its order has been changed.
locations.sort()
print(locations)
# Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.
locations.sort(reverse=True)
print(locations)

# 3-9 Dinner Guests: Working with one of the programs from Exercises 3-4 through 3-7 (page 42), use len() to print a message indicating the number of people you are inviting to dinner.
invites = ['jesus', 'hitler', 'lincoln']
message = f"We are inviting {len(invites)} people to dinner."
print(message)




