#!/usr/bin/python3

keyword = 'python'

with open('textfiles/auth.log','r') as f:
	text = f.read()
	if keyword in text:
		print(f'{keyword} is present.') 
	else:
		print(f'{keyword} is not present.')
