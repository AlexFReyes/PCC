# Loop through an entire list
magicians = ['alice', 'david', 'carolina']
# Magician could be any variable name, but it's good practice to name it something useful in relation to the lsit
for magician in magicians:
    print(magician.title())
# Doing more work within a for loop
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}\n")
# Code that is not indented after a for loop will execute after the loop has finished all its cycles
print("Thank you, everyone. That was a great magic show!")
# Make sure any code you want looped is indented after the first for loop
# All for loops must ahve their first line end with a colon :

