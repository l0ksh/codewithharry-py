#!/usr/bin/python3

dict1 = {}

for i in range(4):
    name = input('Enter your name: ')
    lang = input('Enter your fav language: ')

    dict1.update({name:lang})

print(dict1)
