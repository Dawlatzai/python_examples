user = {'name': 'Dawlatzai','email': 'dawlatzai.ghousi@gmail.com', 'age': 27, 'purchases': [1,2,3,4] }

user['name'] = 'Hedayat'

print(user)

for key in user:
  print(key)


for key, val in user.items():
  print(val)