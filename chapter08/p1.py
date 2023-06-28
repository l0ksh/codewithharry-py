#!/usr/bin/python3

def greatest(v1, v2 ,v3):

	if v1 >= v2 and v1 >= v3:
		greatest = v1
	elif v2 >= v1 and v2 >= v3:
		greatest = v2
	else:
		greatest = v3
	
	return greatest

a = greatest(1,2,1)

print(a)

