#!/usr/bin/python3

list1 = []

for i in range(4):
    var = input(f'Enter {int(i)+1} number: ')
    list1.append(var)

#print(list1.sort())

greatest = list1[0]
if ( list1[1] > greatest ):
    greatest = list1[1]
if ( list1[2] > greatest ):
    greatest = list1[2]
if (list1[3] > greatest ):
    greatest = list1[3]

print(f'{greatest} is the greatest among 4 numbers.')
