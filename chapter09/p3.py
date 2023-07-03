#!/usr/bin/python3


for i in range(2,21):
	for j in range(1,11):
		res = i * j
		print(i,'x',j,'=',res)
		with open(f'textfiles/tableof{i}','a') as f:
			f.write(f'{i} x {j} = {res}\n')

#Removed the unnecessary print statement when assigning the value to res.
#Replaced the file open mode from 'w' to 'a' in order to append the results to the file instead of overwriting it.
#Used a with statement when opening the file, which automatically handles the closing of the file.
