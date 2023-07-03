#!/usr/bin/python3

keywords = ['mind','hand','host']
replacement = '######'

for keyword in keywords:
	
	with open('textfiles/censored.txt','r') as f:
		text = f.read()
		new_text = text.replace(keyword,replacement)

	with open('textfiles/censored.txt','w') as f:
		f.write(new_text)


'''
The file is first opened in read mode ('r') to read its content.
The replace() method is used to create new_text by replacing the keyword with the replacement value.
The file is then reopened in write mode ('w') to overwrite its content.
The write() method is used to write the new_text back to the file, effectively replacing the original content.
'''
