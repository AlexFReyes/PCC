# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.
print('3-4')
invites = ['jesus', 'hitler', 'lincoln']
for x in invites:
    print(f"Hello Mr. {x.title()} \n\tYou are cordially invited to dinner at the Reyes Estate.")

# 3-5
print('\n\n3-5\n'+invites[1])
flakers = invites.pop(1)
invites.insert(1,'Miyozaki')
for x in invites:
    print(f"Hello Mr. {x.title()} \n\tYou are cordially invited to dinner at the Reyes Estate.")

# 3-6
print('\n\n3-6')
for x in invites:
    print(f"Hello Mr. {x.title()} \n\tWe have happened into more space and would like to inform you that there will be three new guests dining with you this evening.\n\tThey are as follows:\n\t\tMr. Josef Stalin\n\t\tMr. Ameliano Bones\n\t\tMr. Horthwell Trombley\n\t We look forward to your company.")
invites.insert(0,'stalin')
invites.insert(3,'bones')
invites.append('trombley')
for x in invites:
    print(f"Hello Mr. {x.title()} \n\tYou are cordially invited to dinner at the Reyes Estate.")

# 3-7
print('\n\n3-7')
print('Apologies to all! We will only be able to host two guests this evening.')
for i in range(len(invites)-1):
    cut_invitee = invites.pop()
    print(f'\tDear Mr. {cut_invitee.title()},\n\t\tI regret to inform you that we will not have space for you to dine with us at the Reyes Estate dinner tonight.\n\t\tSincerest regrets,\n\t\tSir Goldwell')
for x in invites:
    print(f'\tDear Mr. {x.title()},\n\tI am pleased  to inform you that you will be dining with us at the Reyes Estate dinner tonight if you so choose.\n\tGraciously,\n\tSir Goldwell')
del invites[0]
print(invites)





