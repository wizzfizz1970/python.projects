guest = ['liam','chelsea','lillie']

message = 'I would like to invte you to dinner '

print(message + guest[0].title())
print(message + guest[1].title())
print(message + guest[2].title())

message2 = '\nSorry you cannot make it '

print(guest[0].title() + message2)

guest[0] = 'rebecca'
print(message + guest[0].title())
print(message + guest[1].title())
print(message + guest[2].title())

print("\ngood nnews i found a bigger table\n")

guest.insert(0, 'sue')
guest.insert(2, 'eric')
guest.append('kevin')

print(message + guest[0].title())
print(message + guest[1].title())
print(message + guest[2].title())
print(message + guest[3].title())
print(message + guest[4].title())
print(message + guest[5].title())

print("\nTable is to small ownly two people can come.\n")

print(message2 + guest.pop())
print(message2 + guest.pop())
print(message2 + guest.pop())
print(message2 + guest.pop())

message3 = "\nYou are still invited "
print(message3 + guest[0].title())
print(message3 + guest[1].title())

del guest[0]
del guest[0]

print(guest)
