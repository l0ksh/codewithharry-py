#!/usr/bin/python3

dist1 = {'jana':'go',
         'lana':'bring',
         'uthana':'lift',
         'ghr':'home'}
items = dist1.keys()

query = input(f'Enter your query from the list  {items} :')

print(dist1.get(f'{query}'))

