guest = ['liam','chelsea','lillie']

message = 'I would like to invte you to dinner '

print(message + guest[0].title())
print(message + guest[1].title())
print(message + guest[2].title())

print(guest[0].title() +" can not make it")

guest[0] = 'rebecca'
print(message + guest[0].title())
print(message + guest[1].title())
print(message + guest[2].title())

print("good nnews i found a bigger table")

guest.insert(0, 'sue')
guest.insert(2, 'eric')
guest.append('kevin')

print(message + guest[0].title())
print(message + guest[1].title())
print(message + guest[2].title())
print(message + guest[3].title())
print(message + guest[4].title())
print(message + guest[5].title())