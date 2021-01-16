
def summation(n):
	number = 3
	sumt = 2
	while number < n:
		if isPrime(number):
			sumt += number
		number += 1
	return sumt

def isPrime(num):
	if num%2 == 0:
		return False

	for i in range(3, int(sqrt(num))+1, 2):
		if num%i == 0:
			return False
	return True
print(summation(2000000))