# 3-1. Names: Store the names of a few of your friends in a list called names. Print each person’s name by accessing each element in the list, one at a time.
names = ['hannah', 'josh', 'dunkey', 'tyler', 'nathan', 'nut']
# Print all items in a list
for x in names:
    print(x)
# Print all items in a list using length of list
for i in range(len(names)):
    print(names[i])

#3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the person’s name.
for x in names:
    message = f"Hey {x.title()},\n\tI wanted to let you know that I love you and that you mean the world to me."
    print(message)

# 3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”
fav_mod_transport = ['Landyacht Battleaxe Longboard', 'Commencal HT Mountainbike', '2015 Honda Civic EX']
for x in fav_mod_transport:
    message_2 = f"I would love to own a {x.title()}."
    print(message_2)