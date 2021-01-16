from math import factorial
def latticePaths(n):
	return int(factorial(2*n) / (factorial(n)**2))	

print(latticePaths(20))