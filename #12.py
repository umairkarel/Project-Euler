def check(n):
	count = 0
	for i in range(1, int(sqrt(n))+1):
		if n%i == 0:
			if n/i == i:
				count += 1
			else:
				count += 2
	return count > 500
n = 105
i = 15
while not check(n):
	i += 1
	n = int(i*(i+1)/2)
print(n)