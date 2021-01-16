
def divisorSum(num):
	s = 1
	for i in range(2, int(num**0.5)+1):
		if num%i == 0:
			s += i
			s += num//i
	return s
# print(divisorSum(220))
def amicable_pairs(number):
	result = 0
	pairs = []
	for i in range(1, number+1):
		y = divisorSum(i)
		if divisorSum(y) == i and i != y:
			if (y,i) not in pairs:
				pairs.append((i,y))
				print(i,y) 
			result += i
	return(result)

print(amicable_pairs(10000))
