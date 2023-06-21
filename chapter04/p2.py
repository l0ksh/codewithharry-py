#!/usr/bin/python3

list1 = []
for i in range(6):
    marks = input(f'Enter the marks of student {i + 1}: ')
    list1.append(marks)

list1.sort()
print(list1)
