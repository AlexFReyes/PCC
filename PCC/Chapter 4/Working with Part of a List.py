# Slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
# You can slice any section of a list
print(players[2:4])
# If you omit the first argument for slicing it will start from 0
print(players[:3])
# The same occurs if you omit the last argument but opposite
print(players[3:])
# You can use negatives - last 3 in a list
print(players[-3:])
# Loop through a slice
print('The last three players to be added to the team were:')
for player in players[-3:]:
    print('\t'+player.title())
# Copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print('My favorite foods are:')
print(my_foods)

print("\nMy friend's facorite foods are:")
print(friend_foods)





