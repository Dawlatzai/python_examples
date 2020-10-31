users = ['ALi', 'Khan', 'Jahan', 'Kalan', 'Kalam', 'KhanJan', 'Adam']

print(users[2])
print(users[:4])
print(users[4:])

#Unpacking
items = ['Laptop', 'Phone', 'Joystick']
print(items[0])
laptop, phone, joystick = items
print(laptop)
laptop , *other = items
print(other)

#Add to array items.append()
#Insert to array items.insert(0, value)
#out from an array items.pop()

#Tupples
letter = ('a', 'b', 'b', 'c', 'd')
#Sets , have unique value 
letters = {'a', 'b', 'b', 'c', 'd'}
