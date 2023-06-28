#!/usr/bin/python3

l1 = ['Harry','Soham','Sachin','Rahul']

'''
for i in l1:
	if i.startswith('S'):
		print('Goodevening,',i)
'''
index = 0

while index < len(l1):
	if l1[index].startswith('S'):
		print('Goodevening,',l1[index])
	index += 1
