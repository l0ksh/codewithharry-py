#!/usr/bin/python3

list1 = ['tree','branch','wood','stem']

print(list1)
word = input("Enter the word: ")

for i in list1:
	if i == word:
		list1.remove(word)

print(list1)
