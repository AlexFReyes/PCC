# 4-10
colors = ['red', 'blue', 'green', 'yellow', 'white']
print('The first three items in the list are:')
print(colors[0:3])
print('Three items from the middle of the list are:')
print(colors[1:4])
print('The last three items from the list are:')
print(colors[-3:])

# 4-11
pizzas = ['meatlovers', 'pepperoni', 'cheese', 'chipotle chicken and bacon']
friend_pizzas = pizzas[:]

pizzas.append('bbq chicken')
friend_pizzas.append('sausage')

print('My favorite pizzas are:')
for pizza in pizzas:
    print(pizza)
print("My friends' favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

# 4-12
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print('My favorite foods are:')
for food in my_foods:
    print(food)

print("\nMy friend's facorite foods are:")
for food in friend_foods:
    print(food)
   