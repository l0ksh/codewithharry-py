#!/usr/bin/python3

list1 = ['hari','suman','John','Meena']

name = input("Enter the name to find: ")

for i in list1:
	if i == name :
		print('Name found')
		break
