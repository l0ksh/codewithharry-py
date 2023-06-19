#!/usr/bin/python3

name = input('Enter your name: ')
date = input('Enter date: ')
template = f'''Dear <|{name}|>,\n You are selected !\n <|{date}|> '''
print(template)
