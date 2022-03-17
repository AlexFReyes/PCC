# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.
print('3-4')
invites = ['jesus', 'hitler', 'lincoln']
for x in invites:
    print(f"Hello Mr. {x.title()}, \n\n\tYou are cordially invited to dinner at the Reyes Estate.\n")

# 3-5
print('\n\n3-5\n'+invites[1])
invites.remove('hitler')
invites.insert(1,'miyozaki')
for x in invites:
    print(f"Hello Mr. {x.title()}, \n\n\tYou are cordially invited to dinner at the Reyes Estate.\n")

# 3-6
print('\n\n3-6')
for x in invites:
    print(f"Hello Mr. {x.title()}, \n\n\tWe have happened into more space and would like to inform you that there will be three new guests dining with you this evening.\n\tThey are as follows:\n\t\tMr. Josef Stalin\n\t\tMr. Ameliano Bones\n\t\tMr. Horthwell Trombley\n\t We look forward to your company.\n")
invites.insert(0,'stalin')
invites.insert(3,'bones')
invites.append('trombley')
for x in invites:
    print(f"Hello Mr. {x.title()}, \n\n\tYou are cordially invited to dinner at the Reyes Estate.\n")

# 3-7
print('\n\n3-7')
print('Apologies to all! We will only be able to host two guests this evening.')
for i in range(len(invites)-2):
    cut_invitee = invites.pop()
    print(f'\tDear Mr. {cut_invitee.title()},\n\n\t\tI regret to inform you that we will not have space for you to dine with us at the Reyes Estate dinner tonight.\n\n\t\tSincerest regrets,\n\t\tSir Goldwell\n')
for x in invites:
    print(f'\tDear Mr. {x.title()},\n\n\tI am pleased to inform you that you will be dining with us at the Reyes Estate dinner tonight if you so choose.\n\n\tGraciously,\n\tSir Goldwell\n')
del invites[0]
del invites[0]
print(invites)