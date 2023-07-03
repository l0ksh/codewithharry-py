#!/usr/bin/python3

f = open("textfiles/poem.txt","r")
text = f.read()

print(text)

keyword = 'twinkle'

if keyword in text:
	print('Twinkle is present')
else:
	print('Twinkle is not present')

f.close()
