# dictionary.py

friend = {'James':'Sisavath','Jo':'Sipasuet','Noy':'Sivilay'}
friend_list = ['Sisavath','Sipasuet','Sivilay']

print(friend['Noy'])
print(friend_list[-1])

friend['Lanoy'] = 'Sivilay'


friend['May'] = 'soulin'
del friend['May']
print(friend)

print('--------items--------')
for k,v in friend.items():
	print(k,v)

print('--------items--------')
for k in friend.keys():
	print(k)

print(friend.keys())

print(list(friend.keys()))

print('--------items--------')
for v in friend.keys():
	print(v)